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
    #CorrSolvent = SCRF=(Solvent=" + Solvent + ")"
    #Solvent2 = None
    #if Solvent = None or none or blank=true:
        #CorrSolvent=Solvent2
    OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")
    return k, N, FileName, Mem, Cores, Functional, BasisSet, Solvent
#Solvent2 = (none)
#if Solvent=None or none:
	#Solvent = Solvent2

def ReadingFile(FileName, k):
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

def GenerateCombinations(Fragments, K):
    FragmentCombinations = []
    for combo in itertools.combinations(Fragments, K):
        for permutation in itertools.permutations(combo):
            FragmentCombinations.append(permutation)
    return FragmentCombinations

def Headers(FragmentCombinations, ligand, user_inputs):
    k, N, FileName, Mem, Cores, Functional, BasisSet, Solvent = user_inputs
    counter = 1  # Initialize counter for output file names
    
    for combo in FragmentCombinations:
        output_file_name = str(counter) + "-New.com"  # Unique output file name for each combination
        
        with open(output_file_name, "w") as outputfile:  # Use 'w' mode to create new file
            FragmentCharge = 0  # Assuming these values are fixed for now
            LigandCharge = 0    # You may adjust them as per your requirements
            FragmentMultiplicity = 1
            LigandMultiplicity = 1
            TotalCharge = FragmentCharge + LigandCharge
            TotalMultiplicity = max(FragmentMultiplicity, LigandMultiplicity)
            
            BaseHeader = [
                "%chk=" + str(counter) + "-New" + ".chk" + "\n",
                "%mem=" + Mem + "GB" + "\n",
                "%nprocshared=" + Cores + "\n",
                "#" + " " + Functional +  " "+ BasisSet + " " + "SCRF=(Solvent=" + Solvent + ")" + "\n",
                "\n",
                "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n",
		"\n"
            ]

            TotalHeader = BaseHeader + [str(TotalCharge) + " " + str(TotalMultiplicity) + "\n"]

            LigandHeader = BaseHeader + [str(LigandCharge) + " " + str(LigandMultiplicity) + "\n"]
            
            FragmentHeader = BaseHeader + [str(FragmentCharge) + " " + str(FragmentMultiplicity) + "\n"]

            outputfile.writelines(TotalHeader)
            outputfile.writelines(ligand)
            for fragment in combo:
                outputfile.writelines(fragment)
            outputfile.write("\n--Link1--\n")
            outputfile.writelines(FragmentHeader)
            outputfile.writelines(ligand)
            for fragment in combo:
                outputfile.writelines(fragment)
            outputfile.write("\n--Link1--\n")
            outputfile.writelines(LigandHeader)
            outputfile.writelines(ligand)
            for fragment in combo:
                outputfile.writelines(fragment)
        
        counter += 1

user_inputs = UserInputs()
k, N, FileName, Mem, Cores, Functional, BasisSet, Solvent = user_inputs
ligand, fragment_list = ReadingFile(FileName, k)
FragmentCombinations = GenerateCombinations(fragment_list.values(), N)
Headers(FragmentCombinations, ligand, user_inputs)
