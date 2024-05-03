from collections import defaultdict
import itertools

def UserInputs():
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
    return N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent

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
    bq_fragment_list = {key: [line.replace("(Fragment=" + str(key) + ")", "-Bq") for line in fragment_list[key]] for key in fragment_list}
    blank_fragment_list = {key: [line.replace("(Fragment=" + str(key) + ")", " ") for line in fragment_list[key]] for key in fragment_list}

    return ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list

def generate_interactions(Fragments, N):
    # Generate all combinations with the desired length
    combos = itertools.combinations(Fragments, N)
    
    # Initialize sets to store unique interactions
    FourBodyInteractions = set()
    ThreeBodyInteractions = set()
    PairwiseInteractions = set()
    
    for combo in combos:
        # This is hard coded to generate 4 body interactions, but is easily scalable
        four_body_combos = list(itertools.combinations(combo, N))
        FourBodyInteractions.update(four_body_combos)
        
        for four_body_combo in four_body_combos:
            # Generate all 3-body interactions for the current 4-body combination
            three_body_combos = list(itertools.combinations(four_body_combo, N-1))
            ThreeBodyInteractions.update(three_body_combos)
            
            # Generate all 2-body interactions for the current 4-body combination
            pairwise_combos = list(itertools.combinations(four_body_combo, N-2))
            PairwiseInteractions.update(pairwise_combos)
    
    return FourBodyInteractions, ThreeBodyInteractions, PairwiseInteractions


def Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list):
    N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
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
                "Josh Harle - MSc Project Code\n",
                "\n"
            ]
            TotalHeader = BaseHeader + [f"{TotalCharge} {TotalMultiplicity}\n"]

            LigandHeader = BaseHeader + [f"{LigandCharge} {LigandMultiplicity}\n"]
            
            FragmentHeader = BaseHeader + [f"{FragmentCharge} {FragmentMultiplicity}\n"]
            
            w = outputfile.writelines
            counter += 1

user_inputs = UserInputs()
N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list = ReadingFile(FileName, k)
FragmentCombinations = generate_interactions(fragment_list.keys(), N)
Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list)
