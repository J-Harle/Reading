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
            for i in range(3, k+3):  # k+3 as first fragment is ligand and there is no fragment 2
                fragment = f"Fragment={i}"
                if fragment in line:
                    fragment_list[i - 1].append(line)

    # Create copies of ligand and fragment lists then line.replace
    bq_ligand = ligand.copy()
    blank_ligand = ligand.copy()
    bq_fragment_list = {i: fragment_list[i].copy() for i in fragment_list}
    blank_fragment_list = {i: fragment_list[i].copy() for i in fragment_list}
    
    for i in range(1, k+3):
        bq_ligand = [line.replace(f"(Fragment={i})", "-Bq") for line in bq_ligand]
        blank_ligand = [line.replace(f"(Fragment={i})", " ") for line in blank_ligand]
        bq_fragment_list[i - 1] = [line.replace(f"(Fragment={i})", "-Bq") for line in bq_fragment_list[i - 1]]
        blank_fragment_list[i - 1] = [line.replace(f"(Fragment={i})", " ") for line in blank_fragment_list[i - 1]]

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
            if N == 3:
                w(outputfile, TotalHeader, ''.join(blank_ligand), [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [bq_fragment_list[combo[0] - 1]] + [fragment for i in combo[1:] for fragment in blank_fragment_list[i-1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [bq_fragment_list[combo[1] - 1]] + [fragment for i in combo[2:] for fragment in blank_fragment_list[i-1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [fragment for i in combo[:2] for fragment in blank_fragment_list[i-1]] + [bq_fragment_list[combo[2] - 1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [blank_fragment_list[combo[2] - 1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [bq_fragment_list[combo[0] - 1]] + [fragment for i in combo[1:] for fragment in blank_fragment_list[i-1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [bq_fragment_list[combo[1] - 1]] + [fragment for i in combo[2:] for fragment in blank_fragment_list[i-1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [fragment for i in combo[:2] for fragment in blank_fragment_list[i-1]] + [bq_fragment_list[combo[2] - 1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [blank_fragment_list[combo[2] - 1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])

            elif N == 2:
                w(outputfile, TotalHeader, ''.join(blank_ligand), [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]])

            elif N == 1:
                w(outputfile, TotalHeader, ''.join(blank_ligand), [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                w(outputfile, FragmentHeader, ''.join(bq_ligand), [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                w(outputfile, LigandHeader, ''.join(blank_ligand), [bq_fragment_list[i-1] for i in combo])


        # Check the generated file for specific amino acid pairs and remove coordinates if needed
        with open(OutputFile, "r") as infile:
            lines = infile.readlines()

        coords_to_remove = {
            "ala_ser": ["ALA_SER_COORD1", "ALA_SER_COORD2"],
            "ser_val": ["SER_VAL_COORD1", "SER_VAL_COORD2"],
            "his_gly3": ["HIS_GLY3_COORD1", "HIS_GLY3_COORD2"]
        }

        has_ala = any(coords_to_remove["ala_ser"][0] in line for line in lines)
        has_ser = any(coords_to_remove["ala_ser"][1] in line or coords_to_remove["ser_val"][0] in line for line in lines)
        has_val = any(coords_to_remove["ser_val"][1] in line for line in lines)
        has_his = any(coords_to_remove["his_gly3"][0] in line for line in lines)
        has_gly3 = any(coords_to_remove["his_gly3"][1] in line for line in lines)

        if has_ala and has_ser:
            for coord in coords_to_remove["ala_ser"]:
                lines = [line for line in lines if coord not in line]
        if has_ser and has_val:
            for coord in coords_to_remove["ser_val"]:
                lines = [line for line in lines if coord not in line]
        if has_his and has_gly3:
            for coord in coords_to_remove["his_gly3"]:
                lines = [line for line in lines if coord not in line]

        with open(OutputFile, "w") as outfile:
            outfile.writelines(lines)

        counter += 1

# Main execution
user_inputs = UserInputs()
k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list = ReadingFile(FileName, k)
FragmentCombinations = GenerateCombinations(fragment_list.keys(), N)
Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list)
