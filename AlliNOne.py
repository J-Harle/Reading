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
        OutputFile = f"{counter}-New.com"

        with open(OutputFile, 'w') as outputfile:
            w = outputfile.write
            # Based on N, choose the appropriate output format
            if N == 3:
                headers = [
                    (TotalHeader, blank_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]),
                    (LigandHeader, blank_ligand + [bq_fragment_list[combo[0] - 1]] + [fragment for i in combo[1:] for fragment in blank_fragment_list[i]]),
                    (LigandHeader, blank_ligand + [bq_fragment_list[combo[1] - 1]] + [fragment for i in combo[2:] for fragment in blank_fragment_list[i]]),
                    (LigandHeader, blank_ligand + [fragment for i in combo[:2] for fragment in blank_fragment_list[i]] + [bq_fragment_list[combo[2] - 1]]),
                    (LigandHeader, blank_ligand + [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [blank_fragment_list[combo[2] - 1]]),
                    (LigandHeader, blank_ligand + [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]]),
                    (LigandHeader, blank_ligand + [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]]),
                    (LigandHeader, blank_ligand + [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]]),
                    (FragmentHeader, bq_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]),
                    (FragmentHeader, bq_ligand + [bq_fragment_list[combo[0] - 1]] + [fragment for i in combo[1:] for fragment in blank_fragment_list[i]]),
                    (FragmentHeader, bq_ligand + [bq_fragment_list[combo[1] - 1]] + [fragment for i in combo[2:] for fragment in blank_fragment_list[i]]),
                    (FragmentHeader, bq_ligand + [fragment for i in combo[:2] for fragment in blank_fragment_list[i]] + [bq_fragment_list[combo[2] - 1]]),
                    (FragmentHeader, bq_ligand + [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [blank_fragment_list[combo[2] - 1]]),
                    (FragmentHeader, bq_ligand + [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]]),
                    (FragmentHeader, bq_ligand + [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])
                ]
            elif N == 2:
                headers = [
                    (TotalHeader, blank_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]),
                    (LigandHeader, blank_ligand + [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]]),
                    (LigandHeader, blank_ligand + [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]]),
                    (LigandHeader, blank_ligand + [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]]),
                    (FragmentHeader, bq_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]),
                    (FragmentHeader, bq_ligand + [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]]),
                    (FragmentHeader, bq_ligand + [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]])
                ]
            elif N == 1:
                headers = [
                    (TotalHeader, blank_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]),
                    (FragmentHeader, bq_ligand + [fragment for i in combo for fragment in blank_fragment_list[i]]),
                    (LigandHeader, blank_ligand + [bq_fragment_list[i - 1] for i in combo])
                ]

            for header, content in headers:
                w(header)
                w(''.join(content))

        # Check the generated file for specific amino acid pairs and remove coordinates if needed
        with open(OutputFile, "r") as infile:
            lines = infile.readlines()

        coords_to_remove = {
            "ala_ser": ["ALA_SER_COORD1", "ALA_SER_COORD2"],
            "ser_val": ["SER_VAL_COORD1", "SER_VAL_COORD2"],
            "his_gly3": ["HIS_GLY3_COORD1", "HIS_GLY3_COORD2"]
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
