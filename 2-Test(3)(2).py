import csv
import itertools
from collections import defaultdict
import os
import traceback

def calculate_combinations(N, k):
    """Calculate the number of combinations."""
    if k == 0 or k == N:
        return 1
    k -= min(k, N - k)
    result = 1
    for i in range(k):
        result *= N - i
        result //= i + 1
    return result

def read_file(filename, k):
    """Read the file and extract ligand and fragments."""
    ligand = []
    fragment_list = defaultdict(list)
    with open(filename, 'r') as file:
        for line in file:
            if "(Fragment=1)" in line:
                ligand.append(line)
    for i in range(3, k + 1, 1):
        with open(filename, 'r') as file:
            fragment = "Fragment=" + str(i)
            for line in file:
                if fragment in line:
                    fragment_list[i - 1].append(line)
    return ligand, fragment_list

def create_files(ligand, fragment_list, N, output_directory, mem, cores, functional, basis_set, solvent, other_input):
    """Create input files for different combinations of fragments."""
    nCK = calculate_combinations(N, len(fragment_list))
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    print("Creating input files...")
    try:
        for l, combo in zip(range(2, nCK + 2), itertools.combinations(fragment_list.values(), N)):
            file_path = os.path.join(output_directory, f"{l}.com")
            print(f"File path: {file_path}")

            # Open the file for writing
            with open(file_path, "w") as outputfile:
                # Write the base header
                outputfile.write("%chk=" + str(l) + ".chk\n")
                outputfile.write("%mem=" + mem + "GB\n")
                outputfile.write("nprocshared=" + cores + "\n")
                outputfile.write("#" + functional + " " + basis_set + " SCRF=Solvent=" + solvent + ") " + other_input + "\n")
                outputfile.write("\n")
                outputfile.write("TitleCardRequired\n")
                outputfile.write("\n")

                total_charge = 0
                total_multiplicity = 1
                outputfile.write(str(total_charge + total_multiplicity) + "\n")

                for fragment in combo:
                    fragment_charge = 0
                    fragment_multiplicity = 1
                    ligand_charge = 0
                    ligand_multiplicity = 1

                    outputfile.write(str(ligand_charge + ligand_multiplicity) + "\n")
                    outputfile.writelines(ligand)
                    outputfile.writelines(fragment)
                    outputfile.write("\n\n--Link1--\n\n")
                    outputfile.write(str(fragment_charge + fragment_multiplicity) + "\n")
                    outputfile.writelines(ligand)
                    outputfile.writelines(fragment)
                    outputfile.write("\n\n--Link1--\n\n")
                    outputfile.write(str(ligand_charge + ligand_multiplicity) + "\n")
                    outputfile.writelines(ligand)
                    outputfile.writelines(fragment)
                    outputfile.write("\n\n")

            print(f"File created successfully: {file_path}")

        print(f"All files created successfully in directory: {output_directory}")

    except Exception as e:
        print(f"Error occurred while creating files: {e}")
        traceback.print_exc()

def main():
    try:
        k = int(input("How many amino acids are in the structure?: "))
        N = int(input("How many amino acids would you like to include in the interaction?: "))
        uncorr_file_name = input("Which file would you like to open? (Do not include .com): ")
        file_name = uncorr_file_name + ".com"
        mem = str(int(input("How much memory would you like to use (In GB)?: ")))
        cores = str(int(input("How many cores would you like to use?: ")))
        functional = input("Which functional would you like to use?: ")
        basis_set = input("Which basis set would you like to use?: ")
        solvent = input("Which solvent would you like to use? If none, leave blank: ")
        other_input = input("Would you like any other commands in the command line? If none, leave blank: ")

        ligand, fragment_list = read_file(file_name, k)
        output_directory = "output_files"

        create_files(ligand, fragment_list, N, output_directory, mem, cores, functional, basis_set, solvent, other_input)

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
