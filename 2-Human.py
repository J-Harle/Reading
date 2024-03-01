import csv
import itertools
from collections import defaultdict

#Aquiring the inputs to create the header:
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

#Calculating nCK
def calculate_combination(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    numerator = 1
    denominator = 1
    for i in range(1, min(k, n - k) + 1):
        numerator *= n - i + 1
        denominator *= i
    return numerator // denominator

def reading_file():
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

# Function to create output files
def create_files(ligand, fragment_list):
	nCK = calculate_combination(len(fragment_list), N)
	for l in range(2, nCK + 2):
		combo = list(itertools.combinations(fragment_list, N))[l - 2]
		with open(str(l) + "-New.com", "a") as outputfile:
			w = csv.writer(outputfile, delimiter=" ")
		
		FragmentCharge = 0
		LigandCharge = 0
		TotalCharge = FragmentCharge + LigandCharge
		FragmentMultiplicity = 1
		LigandMultiplicity = 1
		if FragmentMultiplicity >= LigandMultiplicity:
			TotalMultiplicity = FragmentMultiplicity
		else:
			TotalMultiplicity = LigandMultiplicity		

		BaseHeader = [
			["%chk=" +str(l)+"-New" + ".chk"],
			["%mem=" + Mem + "GB"],
			["%nprocshared=" + Cores],
			["#", Functional + " ", BasisSet + "SCRF=(Solvent="+ Solvent + ")"+ " "+ OtherInput],
			[" "],
			["ProCoder"],
			[" "]
		]
		
		LigandHeader = [
			[BaseHeader],
			[LigandCharge + LigandMultiplicity]
		]
	
		FragmentHeader = [
			[BaseHeader],
			[FragmentCharge + FragmentMultiplicity]
		]
		
		TotalHeader = [
			[BaseHeader],
			[TotalCharge + TotalMultiplicity]
		]

	w.writerow(TotalHeader)
	w.writerow(ligand)
	w.writerow(x)
	w.writerow[(" ")]
	w.writerow[("--Link1--")]
	w.writerow[(" ")]
	w.writerow[(FragmentHeader)]
	w.writerow[(ligand)]
	w.writerow[(x)]
	w.writerow[(" ")]
	w.writerow[("--Link1--")]
	w.writerow[(LigandHeader)]
	w.writerow[(ligand)]
	w.writerow[(x)]
	w.writerow[(" ")]
	
	


ligand, fragment_list = reading_file()
create_files(ligand, fragment_list)
