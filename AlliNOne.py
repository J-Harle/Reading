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
        BasisSet = ""  # Allows for PM6 to be used
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
            for i in range(3, k + 3):  # k + 3 because fragments start from 3 and index 1 is ligand
                fragment = f"Fragment={i}"
                if fragment in line:
                    fragment_list[i - 1].append(line)

    # Create modified versions of ligand and fragments
    bq_ligand = [line.replace(f"(Fragment={i})", "-Bq") for i in range(1, k + 3) for line in ligand]
    blank_ligand = [line.replace(f"(Fragment={i})", " ") for i in range(1, k + 3) for line in ligand]
    
    bq_fragment_list = {i: [line.replace(f"(Fragment={i + 1})", "-Bq") for line in fragment_list[i]] for i in fragment_list}
    blank_fragment_list = {i: [line.replace(f"(Fragment={i + 1})", " ") for line in fragment_list[i]] for i in fragment_list}

    return ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list

def GenerateCombinations(Fragments, K):
    return itertools.combinations(Fragments, K)

def Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list):
    k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
    counter = 1

    for combo in FragmentCombinations:
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

        with open(OutputFile, 'w') as outputfile:
            w = outputfile.write
            if N == 3:
                w("".join(TotalHeader + blank_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]) + "\n")
                w("".join(LigandHeader + [bq_fragment_list[combo[0] - 1]] + [fragment for i in combo[1:] for fragment in blank_fragment_list[i]]) + "\n")
                # Repeat similar logic for other cases as needed
            elif N == 2:
                w("".join(TotalHeader + blank_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]) + "\n")
                w("".join(LigandHeader + [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]]) + "\n")
                # Repeat similar logic for other cases as needed
            elif N == 1:
                w("".join(TotalHeader + blank_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]) + "\n")
                w("".join(FragmentHeader + bq_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]) + "\n")
                w("".join(LigandHeader + [bq_fragment_list[i - 1] for i in combo]) + "\n")

        # Check the generated file for specific amino acid pairs and remove coordinates if needed
        with open(OutputFile, "r") as infile:
            lines = infile.readlines()

        coords_to_remove = {
            "ala_ser": [
                "H    0   -6.55416120   -6.05342200    0.67196340 L",
                "O    0   -7.54013160   -5.79834050    0.49075190 L",
                "H    0   -8.14204880   -5.89238440    1.23267610 L"
            ],
            "ser_val": [
                "H    0   -3.02666380   -6.78932410    0.80612210 L",
                "H    0   -4.03060530   -7.09699790    0.36810310 L",
                "O    0   -3.99861870   -6.18252120    0.65846340 L"
            ],
            "his_gly3": [
                "O     0   10.29649250   -2.41901770   -0.2378918 L",
                "H     0   10.36614620   -1.71366010   0.88536300 L",
                "H     0    9.84058420   -2.7485774    -0.7157113 L"
            ],
        }

        has_ala = any(coord in line for coord in coords_to_remove["ala_ser"] for line in lines)
        has_ser = any(coord in line for coord in coords_to_remove["ser_val"] for line in lines)
        has_val = any(coord in line for coord in coords_to_remove["ser_val"] for line in lines)
        has_his = any(coord in line for coord in coords_to_remove["his_gly3"] for line in lines)
        has_gly3 = any(coord in line for coord in coords_to_remove["his_gly3"] for line in lines)

        if has_ala and has_ser:
            lines = [line for line in lines if not any(coord in line for coord in coords_to_remove["ala_ser"])]
        if has_ser and has_val:
            lines = [line for line in lines if not any(coord in line for coord in coords_to_remove["ser_val"])]
        if has_his and has_gly3:
            lines = [line for line in lines if not any(coord in line for coord in coords_to_remove["his_gly3"])]

        with open(OutputFile, "w") as outfile:
            outfile.writelines(lines)

        counter += 1


# Main execution
user_inputs = UserInputs()
k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list = ReadingFile(FileName, k)
FragmentCombinations = GenerateCombinations(fragment_list.keys(), N)
Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list)
