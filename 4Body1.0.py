
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
    CorrSolvent = "SCRF=(Solvent=" + Solvent + ")" if Solvent else None
    OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")
    return k, N, FileName, Mem, Cores, Functional, BasisSet, Solvent

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

    # Create copies of ligand a fragment lists then line.replace
    bq_ligand = ligand.copy()
    blank_ligand = ligand.copy()
    bq_fragment_list = fragment_list.copy()
    blank_fragment_list = fragment_list.copy()
    
    for i in range(1, k+3):
        bq_ligand = [line.replace("(Fragment=" + str(i) + ")", "-Bq") for line in bq_ligand]
        blank_ligand = [line.replace("(Fragment=" + str(i) + ")", " ") for line in blank_ligand]
        bq_fragment_list[i - 1] = [line.replace("(Fragment=" + str(i) + ")", "-Bq") for line in bq_fragment_list[i - 1]]
        blank_fragment_list[i - 1] = [line.replace("(Fragment=" + str(i) + ")", " ") for line in blank_fragment_list[i - 1]]

    return ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list

def GenerateCombinations(Fragments, K):
    FragmentCombinations = itertools.combinations(Fragments, K)
    return FragmentCombinations

def Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list):
    k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
    counter = 1  
    
    for combo in FragmentCombinations:
        OutputFile = f"{combo[0]}_{combo[1]}-New.com"  # Naming convention for files
        
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
            
            # Write the headers and fragments to the file
            if N == 1:
                w(TotalHeader)
                w(blank_ligand)
                for fragment in combo:
                    w(blank_fragment_list[fragment - 1])
                w("\n--Link1--\n")
                w(FragmentHeader)
                w(bq_ligand)
                for fragment in combo:
                    w(blank_fragment_list[fragment - 1])
                w("\n--Link1--\n")
                w(LigandHeader)
                w(blank_ligand)
                for fragment in combo:
                    w(bq_fragment_list[fragment - 1])
                w("\n")
            
            elif N == 2:
                # Generate combinations of 2 fragments for each combination of 3 fragments
                fragment_pairs = itertools.combinations(combo, 2)
                for pair in fragment_pairs:
                    # Total headers for each combination of 2 fragments
                    w(TotalHeader)
                    w(blank_ligand)
                    for fragment in combo:
                        w(blank_fragment_list[fragment - 1])
                    w("\n--Link1--\n")
                    
                    # Ligand + Frag1(Bq) + Frag2
                    w(LigandHeader)
                    w(blank_ligand)
                    w(bq_fragment_list[pair[0] - 1])
                    w(blank_fragment_list[pair[1] - 1])
                    w("\n--Link1--\n")
                    
                    # Ligand + Frag1 + Frag2(Bq)
                    w(LigandHeader)
                    w(blank_ligand)
                    w(blank_fragment_list[pair[0] - 1])
                    w(bq_fragment_list[pair[1] - 1])
                    w("\n--Link1--\n")
                    
                    # Ligand + Frag1(Bq) + Frag2(Bq)
                    w(LigandHeader)
                    w(blank_ligand)
                    w(bq_fragment_list[pair[0] - 1])
                    w(bq_fragment_list[pair[1] - 1])
                    w("\n--Link1--\n")
                    
                    # Ligand(Bq) + Frag1 + Frag2
                    w(FragmentHeader)
                    w(bq_ligand)
                    for fragment in combo:
                        w(blank_fragment_list[fragment - 1])
                    w("\n--Link1--\n")
                    
                    # Ligand(Bq) + Frag1(Bq) + Frag2
                    w(FragmentHeader)
                    w(bq_ligand)
                    w(bq_fragment_list[pair[0] - 1])
                    w(blank_fragment_list[pair[1] - 1])
                    w("\n--Link1--\n")
                    
                    # Ligand(Bq) + Frag1 + Frag2(Bq)
                    w(FragmentHeader)
                    w(bq_ligand)
                    w(blank_fragment_list[pair[0] - 1])
                    w(bq_fragment_list[pair[1] - 1])
                    w("\n--Link1--\n")
                    
                    counter += 1
       
user_inputs = UserInputs()
k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list = ReadingFile(FileName, k)
FragmentCombinations = GenerateCombinations(fragment_list.keys(), N)
Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list)

