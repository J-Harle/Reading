from collections import defaultdict
import itertools

def user_inputs():
    k = 14
    N = int(input("How many amino acids would you like to include in the interaction?: "))
    UnCorrFileName = input("Which file would you like to open? (Do not include .com): ")
    FileName = UnCorrFileName + ".com"
    Mem = str(int(input("How much memory would you like to use (In GB)?: ")))
    Cores = str(int(input("How many cores would you like to use?: ")))
    Functional = input("Which functional would you like to use?: ")
    BasisSet = input("Which basis set would you like to use?: ")
    Solvent = input("Which solvent would you like to use? If none, leave blank: ")
    CorrSolvent = f"SCRF=(Solvent={Solvent})" if Solvent and Solvent.lower() != "none" else None
    OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")
    return N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent, OtherInput

def reading_file(FileName, k):
    ligand = []
    fragment_list = defaultdict(list)

    with open(FileName, 'r') as file:
        for line in file:
            if "(Fragment=1)" in line:
                ligand.append(line)
            for i in range(2, k+3):
                fragment = f"Fragment={i}"
                if fragment in line:
                    fragment_list[i - 1].append(line)

    bq_ligand = [line.replace(f"(Fragment={i})", "-Bq") for i in range(1, k+3) for line in ligand]
    blank_ligand = [line.replace(f"(Fragment={i})", " ") for i in range(1, k+3) for line in ligand]
    
    bq_fragment_list = {i: [line.replace(f"(Fragment={i+1})", "-Bq") for line in fragment_list[i]] for i in range(1, k+2)}
    blank_fragment_list = {i: [line.replace(f"(Fragment={i+1})", " ") for line in fragment_list[i]] for i in range(1, k+2)}

    return ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list

def generate_combinations(fragments, K):
    return itertools.combinations(fragments, K)

def write_header(outputfile, header, ligand, fragments):
    outputfile.writelines(header)
    outputfile.write(ligand + "\n")
    for fragment in fragments:
        outputfile.write(fragment + "\n")

def headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list):
    N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent, OtherInput = user_inputs
    counter = 1  

    coords_to_remove = {
        "ala_ser": [
            "H    0   -6.55416120   -6.05342200    0.67196340 L",  # Ala coordinates
            "O    0   -7.54013160   -5.79834050    0.49075190 L",  # Ser coordinates
            "H    0   -8.14204880   -5.89238440    1.23267610 L" 
        ],
        "ser_val": [
            "H    0   -3.02666380   -6.78932410    0.80612210 L",  # Ser coordinates
            "H    0   -4.03060530   -7.09699790    0.36810310 L",  # Val coordinates
            "O    0   -3.99861870   -6.18252120    0.65846340 L"
        ],
        "his_gly3": [
            "O     0   10.29649250   -2.41901770   -0.2378918 L",  # His coordinates
            "H     0   10.36614620   -1.71366010   0.88536300 L",  
            "H     0    9.84058420   -2.7485774    -0.7157113 L"   # Gly3 coordinates
        ],
    }

    for combo in FragmentCombinations:
        OutputFile = str(counter) + "-New.com"
        with open(OutputFile, "w") as outputfile: 
            FragmentCharge = 0 
            LigandCharge = 0    
            FragmentMultiplicity = 1
            LigandMultiplicity = 1
            TotalCharge = FragmentCharge + LigandCharge
            TotalMultiplicity = max(FragmentMultiplicity, LigandMultiplicity)
            
            BaseHeader = [
                "%chk=" + str(counter) + "-New.chk\n",
                "%mem=" + Mem + "GB\n",
                "%nprocshared=" + Cores + "\n",
                "#" + " " + Functional +  " "+ BasisSet + " " + (CorrSolvent if CorrSolvent else "") + "\n",
                "\n",
                "MSc Project Code\n",
                "\n"
            ]

            TotalHeader = BaseHeader + [str(TotalCharge) + " " + str(TotalMultiplicity) + "\n"]
            LigandHeader = BaseHeader + [str(LigandCharge) + " " + str(LigandMultiplicity) + "\n"]
            FragmentHeader = BaseHeader + [str(FragmentCharge) + " " + str(FragmentMultiplicity) + "\n"]

            if N == 3:
                # Ligand + Frag1 + Frag2 + Frag3
                write_header(outputfile, TotalHeader, blank_ligand, [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                # Ligand + Frag1(Bq) + Frag2 + Frag3
                write_header(outputfile, LigandHeader, blank_ligand, [bq_fragment_list[combo[0] - 1]] + [fragment for i in combo[1:] for fragment in blank_fragment_list[i-1]])
                # Ligand + Frag1 + Frag2(Bq) + Frag3
                write_header(outputfile, LigandHeader, blank_ligand, [bq_fragment_list[combo[1] - 1]] + [fragment for i in combo[2:] for fragment in blank_fragment_list[i-1]])
                # Ligand + Frag1 + Frag2 + Frag3(Bq)
                write_header(outputfile, LigandHeader, blank_ligand, [fragment for i in combo[:2] for fragment in blank_fragment_list[i-1]] + [bq_fragment_list[combo[2] - 1]])
                # Ligand + Frag1(Bq) + Frag2(Bq) + Frag3
                write_header(outputfile, LigandHeader, blank_ligand, [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [blank_fragment_list[combo[2] - 1]])
                # Ligand + Frag1(Bq) + Frag2 + Frag3(Bq)
                write_header(outputfile, LigandHeader, blank_ligand, [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])
                # Ligand + Frag1 + Frag2(Bq) + Frag3(Bq)
                write_header(outputfile, LigandHeader, blank_ligand, [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])
                # Ligand + Frag1(Bq) + Frag2(Bq) + Frag3(Bq)
                write_header(outputfile, LigandHeader, blank_ligand, [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])
                # Ligand(Bq) + Frag1 + Frag2 + Frag3
                write_header(outputfile, FragmentHeader, bq_ligand, [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                # Ligand(Bq) + Frag1(Bq) + Frag2 + Frag3
                write_header(outputfile, FragmentHeader, bq_ligand, [bq_fragment_list[combo[0] - 1]] + [fragment for i in combo[1:] for fragment in blank_fragment_list[i-1]])
                # Ligand(Bq) + Frag1 + Frag2(Bq) + Frag3
                write_header(outputfile, FragmentHeader, bq_ligand, [bq_fragment_list[combo[1] - 1]] + [fragment for i in combo[2:] for fragment in blank_fragment_list[i-1]])
                # Ligand(Bq) + Frag1 + Frag2 + Frag3(Bq)
                write_header(outputfile, FragmentHeader, bq_ligand, [fragment for i in combo[:2] for fragment in blank_fragment_list[i-1]] + [bq_fragment_list[combo[2] - 1]])
                # Ligand(Bq) + Frag1(Bq) + Frag2(Bq) + Frag3
                write_header(outputfile, FragmentHeader, bq_ligand, [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [blank_fragment_list[combo[2] - 1]])
                # Ligand(Bq) + Frag1(Bq) + Frag2 + Frag3(Bq)
                write_header(outputfile, FragmentHeader, bq_ligand, [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])
                # Ligand(Bq) + Frag1 + Frag2(Bq) + Frag3(Bq)
                write_header(outputfile, FragmentHeader, bq_ligand, [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]] + [bq_fragment_list[combo[2] - 1]])

            elif N == 2:
                # Ligand + Frag1 + Frag2
                write_header(outputfile, TotalHeader, blank_ligand, [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                # Ligand + Frag1(Bq) + Frag2
                write_header(outputfile, LigandHeader, blank_ligand, [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]])
                # Ligand + Frag1 + Frag2(Bq)
                write_header(outputfile, LigandHeader, blank_ligand, [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]])
                # Ligand + Frag1(Bq) + Frag2(Bq)
                write_header(outputfile, LigandHeader, blank_ligand, [bq_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]])
                # Ligand(Bq) + Frag1 + Frag2
                write_header(outputfile, FragmentHeader, bq_ligand, [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                # Ligand(Bq) + Frag1(Bq) + Frag2
                write_header(outputfile, FragmentHeader, bq_ligand, [bq_fragment_list[combo[0] - 1]] + [blank_fragment_list[combo[1] - 1]])
                # Ligand(Bq) + Frag1 + Frag2(Bq)
                write_header(outputfile, FragmentHeader, bq_ligand, [blank_fragment_list[combo[0] - 1]] + [bq_fragment_list[combo[1] - 1]])

            elif N == 1:
                # Ligand + Frag1
                write_header(outputfile, TotalHeader, blank_ligand, [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                # Ligand(Bq) + Frag1
                write_header(outputfile, FragmentHeader, bq_ligand, [fragment for i in combo for fragment in blank_fragment_list[i-1]])
                # Ligand + Frag1(Bq)
                write_header(outputfile, LigandHeader, blank_ligand, [bq_fragment_list[i-1] for i in combo])

        # Now, check the generated file for specific amino acid pairs
        with open(OutputFile, "r") as infile:
            lines = infile.readlines()

        # Flags to check presence of pairs
        has_ala = any(coords_to_remove["ala_ser"][0] in line for line in lines)
        has_ser = any(coords_to_remove["ala_ser"][1] in line or coords_to_remove["ser_val"][0] in line for line in lines)
        has_val = any(coords_to_remove["ser_val"][1] in line for line in lines)
        has_his = any(coords_to_remove["his_gly3"][0] in line for line in lines)
        has_gly3 = any(coords_to_remove["his_gly3"][1] in line for line in lines)

        # If the pairs exist, remove only the specific coordinates
        if has_ala and has_ser:
            for coord in coords_to_remove["ala_ser"]:
                lines = [line for line in lines if coord not in line]
        if has_ser and has_val:
            for coord in coords_to_remove["ser_val"]:
                lines = [line for line in lines if coord not in line]
        if has_his and has_gly3:
            for coord in coords_to_remove["his_gly3"]:
                lines = [line for line in lines if coord not in line]

        # Write back the modified lines to the output file
        with open(OutputFile, "w") as outfile:
            outfile.writelines(lines)

        counter += 1

if __name__ == "__main__":
    user_inp = user_inputs()
    N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent, OtherInput = user_inp
    ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list = reading_file(FileName, 14)
    FragmentCombinations = generate_combinations(range(2, N+2), N)
    headers(FragmentCombinations, ligand, user_inp, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list)
