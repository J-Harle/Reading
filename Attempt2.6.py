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
    CorrSolvent = "SCRF=(Solvent=" + Solvent + ")"
    Solvent2 = None
    if Solvent == "None" or "none" or "":
        CorrSolvent = Solvent2
    OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")
    return k, N, FileName, Mem, Cores, Functional, BasisSet, Solvent

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

def Headers(FragmentCombinations, ligand, UserInputs):
    counter = 1  
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
                "%chk=" + str(counter) + "-New" + ".chk" + "\n",
                "%mem=" + Mem + "GB" + "\n",
                "%nprocshared=" + Cores + "\n",
                "#" + " " + Functional +  " "+ BasisSet + " " + CorrSolvent + "\n",
                "\n",
                "MSc Project Code" + "\n",
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
            outputfile.writelines("\n")
        
       counter += 1

user_inputs = UserInputs()
k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
ligand, fragment_list = ReadingFile(FileName, k)
FragmentCombinations = GenerateCombinations(fragment_list.values(), N)
Headers(FragmentCombinations, ligand, user_inputs)
