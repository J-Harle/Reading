import csv
import itertools
from collections import defaultdict
import math 
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

def CalculateCombinations(N, k):
	if k == 0 or k == N:
		return 1
	k - min(k, N - k)
	result = 1
	for i in range(k):
		result *= N - i
		result //= i + 1
	return result

def def CreateFiles(Ligand, FragmentList):
    nCK = calculate_combinations(N, k)
    output_directory = "output_files"  # Directory to store output files

    # Ensure the output directory exists or create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        # Iterate through combinations and create files
        for l, combo in zip(range(2, nCK + 2), itertools.combinations(FragmentList.values(), N)):
            file_path = os.path.join(output_directory, f"{l}.csv")

            # Open the file for writing
            with open(file_path, "w") as outputfile:
                w = csv.writer(outputfile, delimiter=" ")
                # Write to the file...

                print(f"File created successfully: {file_path}")

    except Exception as e:
        print(f"Error occurred while creating files: {e}")
            BaseHeader = [
                ["%chk=" + str(l) + ".chk"],
                ["%mem=" + Mem + "GB"],
                ["nprocshared=" + Cores],
                ["#", Functional, " ", BasisSet, "SCRF=Solvent=", Solvent + ")", " ", OtherInput],
                [" "],
                ["Title" + "Card" + "Required"],
                [" "]
            ]
            w.writerows(BaseHeader)
		#can make some logic to change only 4 inputs rather than 6? (worth it?)
            TotalCharge = 0  # Change if different
            TotalMultiplicity = 1  # Change if different

            MainHeader = [
                BaseHeader,
                [TotalCharge + TotalMultiplicity]
            ]
            w.writerows(MainHeader)

            for fragment in combo:
                FragmentCharge = 0  		#| Change if different 
                FragmentMultiplicity = 1	#| Change if different
                LigandCharge = 0  		#| Change if different
                LigandMultiplicity = 1 		#| Change if different

                LigandHeader = [
                    BaseHeader,
                    [LigandCharge + LigandMultiplicity]
                ]
                w.writerows(LigandHeader)
                w.writerow(Ligand)
                w.writerow(fragment)
                w.writerow([" "])
                w.writerow(["--Link1--"])
                FragmentHeader = [
                    BaseHeader,
                    [FragmentCharge + FragmentMultiplicity]
                ]
                w.writerows(FragmentHeader)
                w.writerow(Ligand)
                w.writerow(fragment)
                w.writerow([" "])
                w.writerow(["--Link1--"])
                ActualCombinationHeader = [
                    BaseHeader,
                    [LigandCharge + LigandMultiplicity]
                ]
                w.writerows(ActualCombinationHeader)
                w.writerow(Ligand)
                w.writerow(fragment)
                w.writerow([" "])

CreateFiles(Ligand, FragmentList)
