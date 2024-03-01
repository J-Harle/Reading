import csv
import itertools
from collections import defaultdict

def reading_file(FileName, k):
    ligand = []
    fragment_list = defaultdict(list)

    with open(FileName, 'r') as file:
        for line in file:
            if "(Fragment=1)" in line:
                ligand.append(line)
            for i in range(3, k + 1):
                fragment = "Fragment=" + str(i)
                if fragment in line:
                    fragment_list[i - 1].append(line)

    return ligand, fragment_list

def generate_combinations(fragment_list, N):
    combinations = list(itertools.combinations(fragment_list.values(), N))
    return combinations

def create_files(ligand, fragment_list, N):
    combinations = generate_combinations(fragment_list, N)
    for l, combo in enumerate(combinations, start=2):
        with open(str(l) + "-New.com", "a") as outputfile:
            w = csv.writer(outputfile, delimiter=" ")

            FragmentCharge = 0
            LigandCharge = 0
            TotalCharge = FragmentCharge + LigandCharge
            FragmentMultiplicity = 1
            LigandMultiplicity = 1
            TotalMultiplicity = max(FragmentMultiplicity, LigandMultiplicity)

            BaseHeader = [
                "%chk=" + str(l) + "-New" + ".chk",
                "%mem=" + Mem + "GB",
                "%nprocshared=" + Cores,
                "#" + Functional + " " + BasisSet + "SCRF=(Solvent=" + Solvent + ")" + " " + OtherInput,
                "",
                "Eeby Deeby",
                ""
            ]

            LigandHeader = BaseHeader + [f"{LigandCharge} {LigandMultiplicity}"]

            FragmentHeader = BaseHeader + [f"{FragmentCharge} {FragmentMultiplicity}"]

            TotalHeader = BaseHeader + [f"{TotalCharge} {TotalMultiplicity}"]

            w.writerow(TotalHeader)
            w.writerow(ligand)
            w.writerow(combo)
            w.writerow([" "])
            w.writerow(["--Link1--"])
            w.writerow([" "])
            w.writerow(FragmentHeader)
            w.writerow(ligand)
            w.writerow(combo)
            w.writerow([" "])
            w.writerow(["--Link1--"])
            w.writerow(LigandHeader)
            w.writerow(ligand)
            w.writerow(combo)
            w.writerow([" "])

k = int(input("How many amino acids are in the structure?: "))
N = int(input("How many amino acids would you like to include in the interaction?: "))
UnCorrFileName = input("Which file would you like to open? (Do not include .com): ")
FileName = UnCorrFileName + ".com"
Mem = str(int(input("How much memory would you like to use (In GB)?: ")))
Cores = str(int(input("How many cores would you like to use?: ")))
Functional = input("Which functional would you like to use?: ")
BasisSet = input("Which basis set would you like to use?: ")
Solvent = input("Which solvent would you like to use? If none, leave blank: ")
OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")

ligand, fragment_list = reading_file(FileName, k)
create_files(ligand, fragment_list, N)