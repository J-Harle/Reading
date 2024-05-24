import re
from collections import defaultdict
import itertools

def UserInputs():
    k = int(input("How many amino acids are in the structure?: "))
    N = int(input("How many amino acids would you like to include in the interaction?: "))
    UnCorrFileName = input("Which file would you like to open? (Do not include .com): ")
    FileName = f"{UnCorrFileName}.com"
    Mem = str(int(input("How much memory would you like to use (In GB)?: ")))
    Cores = str(int(input("How many cores would you like to use?: ")))
    Functional = input("Which functional would you like to use?: ")
    BasisSet = input("Which basis set would you like to use?: ")
    if BasisSet.strip() == "":
        BasisSet = "" #Allows for PM6 to be used
    Solvent = input("Which solvent would you like to use? If none, leave blank: ")
    CorrSolvent = f"SCRF=(Solvent={Solvent})" if Solvent.lower() != "none" else ""
    OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")
    if OtherInput.strip() == "":
        OtherInput = ""
    return k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent

def ReadingFile(FileName, k):
    ligand = []
    fragment_list = defaultdict(list)

    with open(FileName, 'r') as file:
        for line in file:
            if "(Fragment=1)" in line:
                ligand.append(line)
            for i in range(3, k+3, 1): # k+3 as first fragment is ligand and there is no fragment 2
                fragment = f"Fragment={i}"
                if fragment in line:
                    fragment_list[i - 1].append(line)

    # Create copies of ligand and fragment lists then line.replace
    bq_ligand = ligand.copy()
    blank_ligand = ligand.copy()
    bq_fragment_list = defaultdict(list)
    blank_fragment_list = defaultdict(list)
    
    for i in range(1, k+3):
        bq_ligand = [line.replace(f"(Fragment={i})", "-Bq") for line in bq_ligand]
        blank_ligand = [line.replace(f"(Fragment={i})", " ") for line in blank_ligand]
        bq_fragment_list[i - 1] = [line.replace(f"(Fragment={i})", "-Bq") for line in fragment_list[i - 1]]
        blank_fragment_list[i - 1] = [line.replace(f"(Fragment={i})", " ") for line in fragment_list[i - 1]]

    return ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list

def GenerateCombinations(Fragments, K):
    FragmentCombinations = itertools.combinations(Fragments, K)
    return FragmentCombinations

def Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list):
    k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
    counter = 1  
    
    for combo in FragmentCombinations:
        TotalCharge = 0
        TotalMultiplicity = 1

        for section in range(1, 2**N):  # Assuming 15 sections
            section_charge = 0
            section_multiplicity = 1

            # Check each fragment in the combination for the current section
            for fragment_index in combo:
                for line in blank_fragment_list[fragment_index - 1]:
                    if "--Link1--" in line:
                        break  # Move to the next section
                    if "Cu-Bq" in line:
                        section_charge = 0
                        section_multiplicity = 1
                        break  # No need to check further, found Cu-Bq
                    elif "Cu" in line:
                        section_charge = 2
                        section_multiplicity = 2
                        break  # No need to check further, found Cu

            TotalCharge = max(TotalCharge, section_charge)
            TotalMultiplicity = max(TotalMultiplicity, section_multiplicity)
        OutputFile = f"{counter}-New.com"  
        with open(OutputFile, "w") as outputfile: 
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

            LigandHeader = BaseHeader + ["0 1\n"]
            
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
          
        counter += 1

user_inputs = UserInputs()
k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list = ReadingFile(FileName, k)
FragmentCombinations = GenerateCombinations(fragment_list.keys(), N)
Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list)
