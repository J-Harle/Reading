import csv
import itertools
from collections import defaultdict
import math 
import traceback
import os

k = int(input("How many amino acids are in the structure?: "))
N = int(input("How many amino acids would you like to include in the interaction?: "))
UnCorrFileName = str(input("Which file would you like to open? (Do not include .com): "))
FileName = UnCorrFileName + ".com"
Mem = str(int(input("How much memory would you like to use (In GB)?: ")))
Cores = str(int(input("How many cores would you like to use?: ")))
Functional = input("Which functional would you like to use?: ")
BasisSet = input("Which basis set would you like to use?: ")
Solvent = input("Which solvent would you like to use? If none, leave blank: ")
OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")

def ReadingFile():
    Ligand = []
    with open(FileName, 'r') as File:
        for line in File:
            if "(Fragment=1)" in line:
                Ligand.append(line)
    FragmentList = defaultdict(list)
    for i in range(3, k + 1, 1):
        with open(FileName, 'r') as File:
            Fragment = "Fragment=" + str(i)
            for line in File:
                if Fragment in line:
                    FragmentList[i - 1].append(line)
    return Ligand, FragmentList

Ligand, FragmentList = ReadingFile()

def calculate_combinations(N, k):
    if k == 0 or k == N:
        return 1
    k -= min(k, N - k)
    result = 1
    for i in range(k):
        result *= N - i
        result //= i + 1
    return result



def CreateFiles(Ligand, FragmentList):
    nCK = calculate_combinations(N, k)
    output_directory = "output_files"  # Directory to store output files

    # Ensure the output directory exists or create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    print("Calling CreateFiles function...")

    try:
        for l, combo in zip(range(2, nCK + 2), itertools.combinations(FragmentList.values(), N)):
            file_path = os.path.join(output_directory, f"{l}.com")
            print(f"File path: {file_path}")

            # Open the file for writing
            with open(file_path, "w") as outputfile:
                # Write the base header
                outputfile.write("%chk=" + str(l) + ".chk\n")
                outputfile.write("%mem=" + Mem + "GB\n")
                outputfile.write("nprocshared=" + Cores + "\n")
                outputfile.write("#" + Functional + " " + BasisSet + " SCRF=Solvent=" + Solvent + ") " + OtherInput + "\n")
                outputfile.write("\n")
                outputfile.write("TitleCardRequired\n")
                outputfile.write("\n")

                TotalCharge = 0  # Change if different
                TotalMultiplicity = 1  # Change if different
                outputfile.write(str(TotalCharge + TotalMultiplicity) + "\n")

                for fragment in combo:
                    FragmentCharge = 0        #| Change if different 
                    FragmentMultiplicity = 1    #| Change if different
                    LigandCharge = 0        #| Change if different
                    LigandMultiplicity = 1     #| Change if different

                    outputfile.write(str(LigandCharge + LigandMultiplicity) + "\n")
                    outputfile.writelines(Ligand)
                    outputfile.writelines(fragment)
                    outputfile.write("\n")
                    outputfile.write("\n")
                    outputfile.write("--Link1--\n")
                    outputfile.write("\n")
                    outputfile.write(str(FragmentCharge + FragmentMultiplicity) + "\n")
                    outputfile.writelines(Ligand)
                    outputfile.writelines(fragment)
                    outputfile.write("\n")
                    outputfile.write("\n")
                    outputfile.write("--Link1--\n")
                    outputfile.write("\n")
                    outputfile.write(str(LigandCharge + LigandMultiplicity) + "\n")
                    outputfile.writelines(Ligand)
                    outputfile.writelines(fragment)
                    outputfile.write("\n")
                    outputfile.write("\n")

            print(f"File created successfully: {file_path}")

        print(f"All files created successfully in directory: {output_directory}")

    except Exception as e:
        print(f"Error occurred while creating files: {e}")
        traceback.print_exc()

print("Calling CreateFiles function...")
CreateFiles(Ligand, FragmentList)
