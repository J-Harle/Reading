import itertools
from collections import defaultdict

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
    
    if Solvent.lower() == "none" or Solvent == "":
        CorrSolvent = None
    else:
        CorrSolvent = "SCRF=(Solvent=" + Solvent + ")"
    
    OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")
    
    return k, N, FileName, Mem, Cores, Functional, BasisSet, Solvent, CorrSolvent

def ReadingFile(FileName, k):
    ligand = []
    fragment_list = defaultdict(list)

    with open(FileName, 'r') as file:
        for line in file:
            if "(Fragment=1)" in line:
                ligand.append(line)
            for i in range(3, k+3, 1): #k+3 as first fragment is ligand and there is no fragment 2
                fragment = "Fragment=" + str(i)
                if fragment in line:
                    fragment_list[i - 1].append(line)
    return ligand, fragment_list

def GenerateCombinations(Fragments, K):
    FragmentCombinations = itertools.combinations(Fragments, K)
    return FragmentCombinations

def Headers(fragment_combinations, ligand, k, N, file_name, mem, cores, functional, basis_set, solvent, corr_solvent):
    counter = 1
    for combo in fragment_combinations:
        output_file = str(counter) + "-New.com"
        with open(output_file, "w") as outputfile:
            fragment_charge = 0
            ligand_charge = 0
            fragment_multiplicity = 1
            ligand_multiplicity = 1
            total_charge = fragment_charge + ligand_charge
            total_multiplicity = max(fragment_multiplicity, ligand_multiplicity)

            base_header = [
                "%chk=" + str(counter) + "-New" + ".chk" + "\n",
                "%mem=" + mem + "GB" + "\n",
                "%nprocshared=" + cores + "\n",
                "#" + " " + functional + " " + basis_set + (" " + corr_solvent if corr_solvent else "") + "\n",
                "\n",
                "MSc Project Code" + "\n",
                "\n"
            ]

            total_header = base_header + [str(total_charge) + " " + str(total_multiplicity) + "\n"]
            ligand_header = base_header + [str(ligand_charge) + " " + str(ligand_multiplicity) + "\n"]
            fragment_header = base_header + [str(fragment_charge) + " " + str(fragment_multiplicity) + "\n"]

            if N == 1:
                outputfile.writelines(total_header)
                outputfile.writelines(ligand)
                for fragment in combo:
                    outputfile.writelines(fragment)
                outputfile.write("\n--Link1--\n")
                # Modify fragment 1 to -Bq
                outputfile.writelines(fragment_header)
                outputfile.writelines(ligand)
                for fragment in combo:
                    outputfile.writelines(fragment)
                outputfile.write("\n--Link1--\n")
                for i in range(2, k+1):
                    # Modify fragment i to -Bq
                    outputfile.writelines(fragment_header)
                    outputfile.writelines(ligand)
                    for fragment in combo:
                        outputfile.writelines(fragment)
                    outputfile.write("\n--Link1--\n")
            else:
                # Handle other cases here
                pass

            counter += 1

k, N, FileName, Mem, Cores, Functional, BasisSet, Solvent, CorrSolvent = UserInputs()
ligand, fragment_list = ReadingFile(FileName, k)
FragmentCombinations = GenerateCombinations(fragment_list.values(), N)
Headers(FragmentCombinations, ligand, k, N, FileName, Mem, Cores, Functional, BasisSet, Solvent, CorrSolvent)
