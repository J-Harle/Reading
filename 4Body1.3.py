from collections import defaultdict
import itertools

def UserInputs():
    k = int(input("How many amino acids are in the structure?: "))
    N = int(input("How many amino acids would you like to include in the interaction?: "))
    UnCorrFileName = input("Which file would you like to open? (Do not include .com): ")
    FileName = UnCorrFileName + ".com"
    Mem = str(int(input("How much memory would you like to use (In GB)?: ")))
    Cores = str(int(input("How many cores would you like to use?: ")))
    Functional = input("Which functional would you like to use?: ")
    BasisSet = input("Which basis set would you like to use?: ")
    Solvent = input("Which solvent would you like to use? If none, leave blank: ")
    CorrSolvent = f"SCRF=(Solvent={Solvent})" if Solvent.lower() != "none" else ""
    OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")
    return k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent

def ReadingFile(FileName, k):
    ligand = []
    fragment_list = defaultdict(list)

    with open(FileName, 'r') as file:
        for line in file:
            if "(Fragment=1)" in line:
                ligand.append(line)
            for i in range(3, k+3, 1): # k+3 as first fragment is ligand and there is no fragment 2
                fragment = "Fragment=" + str(i)
                if fragment in line:
                    fragment_list[i - 1].append(line)

    bq_ligand = [line.replace("(Fragment=" + str(i) + ")", "-Bq") for line in ligand]
    blank_ligand = [line.replace("(Fragment=" + str(i) + ")", " ") for line in ligand]
    bq_fragment_list = [line.replace("(Fragment=" + str(i) + ")", "-Bq") for line in fragment_list]
    blank_fragment_list = [line.replace("(Fragment=" + str(i) + ")", " ") for line in fragment_list]

    return ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list

def generate_interactions(Fragments, N):
    # Generate all combinations with the desired length
    combos = itertools.combinations(Fragments, N)
    
    # Initialize sets to store unique interactions
    FourBodyInteractions = set()
    ThreeBodyInteractions = set()
    PairwiseInteractions = set()
    
    for combo in combos:
        four_body_combos = list(list(itertools.combinations(combo, 3)))
        FourBodyInteractions.update(four_body_combos)
        
        for four_body_combo in four_body_combos:
            # Generate all 3-body interactions for the current 4-body combination
            three_body_combos = list(list(itertools.combinations(four_body_combo, 2)))
            ThreeBodyInteractions.update(three_body_combos)
            
            # Generate all 2-body interactions for the current 4-body combination
            pairwise_combos = list(list(itertools.combinations(four_body_combo, 1)))
            PairwiseInteractions.update(pairwise_combos)
    
    # Create copies of the interactions lists with fragment numbers replaced with '-Bq'
    FourBodyBq = [line.replace("(Fragment=" + str(i) + ")", "-Bq") for line in FourBodyInteractions]
    ThreeBodyBq = [line.replace("(Fragment=" + str(i) + ")", "-Bq") for line in ThreeBodyInteractions]
    PairwiseBq = [line.replace("(Fragment=" + str(i) + ")", "-Bq") for line in PairwiseInteractions]
    
    return FourBodyInteractions, ThreeBodyInteractions, PairwiseInteractions, FourBodyBq, ThreeBodyBq, PairwiseBq


def Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list):
    k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
    counter = 1  
    for combo in FragmentCombinations:
        OutputFile = f"{counter}-New.com"  
        with open(OutputFile, "w") as outputfile: 
            FragmentCharge = 0 
            LigandCharge = 0    
            FragmentMultiplicity = 1
            LigandMultiplicity = 1
            TotalCharge = FragmentCharge + LigandCharge
            TotalMultiplicity = max(FragmentMultiplicity, LigandMultiplicity)
            
            BaseHeader = [
                f"%chk={counter}-New.chk\n",
                f"%mem={Mem}GB\n",
                f"%nprocshared={Cores}\n",
                f"#{Functional} {BasisSet} {CorrSolvent}\n",
                "\n",
                "MSc Project Code\n",
                "\n"
            ]

            TotalHeader = BaseHeader + [f"{TotalCharge} {TotalMultiplicity}\n"]

            LigandHeader = BaseHeader + [f"{LigandCharge} {LigandMultiplicity}\n"]
            
            FragmentHeader = BaseHeader + [f"{FragmentCharge} {FragmentMultiplicity}\n"]
            
            w = outputfile.writelines
            
            # Ligand + Frag1 + Frag2 + Frag3
            w(TotalHeader)
            w(blank_ligand)
            for fragment in combo:
                w(blank_fragment_list[fragment - 1])
            w("\n--Link1--\n")
            
            # Ligand + Frag1(Bq) + Frag2 + Frag3
            w(LigandHeader)
            w(blank_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(blank_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand + Frag1 + Frag2(Bq) + Frag3
            w(LigandHeader)
            w(blank_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(blank_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand + Frag1 + Frag2 + Frag3(Bq)
            w(LigandHeader)
            w(blank_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(bq_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand + Frag1(Bq) + Frag2(Bq) + Frag3
            w(LigandHeader)
            w(blank_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(blank_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand + Frag1(Bq) + Frag2 + Frag3(Bq)
            w(LigandHeader)
            w(blank_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(bq_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand + Frag1 + Frag2(Bq) + Frag3(Bq)
            w(LigandHeader)
            w(blank_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(bq_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand + Frag1(Bq) + Frag2(Bq) + Frag3(Bq)
            w(LigandHeader)
            w(blank_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(bq_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1 + Frag2 + Frag3
            w(FragmentHeader)
            w(bq_ligand)
            for fragment in combo:
                w(blank_fragment_list[fragment - 1])
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1(Bq) + Frag2 + Frag3
            w(FragmentHeader)
            w(bq_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(blank_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1 + Frag2(Bq) + Frag3
            w(FragmentHeader)
            w(bq_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(blank_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1 + Frag2 + Frag3(Bq)
            w(FragmentHeader)
            w(bq_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(bq_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")

            # Ligand(Bq) + Frag1(Bq) + Frag2(Bq) + Frag3
            w(FragmentHeader)
            w(bq_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(blank_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1(Bq) + Frag2 + Frag3(Bq)
            w(FragmentHeader)
            w(bq_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(bq_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1 + Frag2(Bq) + Frag3(Bq)
            w(FragmentHeader)
            w(bq_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(bq_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")

            # Ligand(Bq) + Frag1(Bq) + Frag2(Bq) + Frag3(Bq)
            w(FragmentHeader)
            w(bq_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(bq_fragment_list[combo[2] - 1])
            w("\n--Link1--\n")
            
            # Also need to do both 2 body interactions for each Fragment:
            for fragment in combo:
                w(TotalHeader)
                w(blank_ligand)
                w(blank_fragment_list[fragment - 1])
                w("\n--Link1--\n")
                w(FragmentHeader)
                w(bq_ligand)
                w(blank_fragment_list[fragment - 1])
                w("\n--Link1--\n")
                w(LigandHeader)
                w(blank_ligand)
                w(bq_fragment_list[fragment - 1])
                w("\n")
            
        counter += 1

user_inputs = UserInputs()
k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list = ReadingFile(FileName, k)
FragmentCombinations = GenerateCombinations(fragment_list.keys(), N)
Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list)
