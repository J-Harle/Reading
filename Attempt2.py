import itertools
from collections import defaultdict

#user inputs
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
  OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")
  return k, N, FileName, Mem, Cores, Functional, BasisSet, Solvent

def ReadingFile(FileName, k):
    ligand = []
    FragmentList = defaultdict(list)

    with open(FileName, 'r') as file:
        for line in file:
            if "(Fragment=1)" in line:
                ligand.append(line)
            for i in range(3, k + 1):
                fragment = "Fragment=" + str(i)
                if fragment in line:
                    fragment_list[i - 1].append(line)

    return ligand, FragmentList
def GenerateCombinations():
  Fragments = list(FragmentList())
  FragmentCombinations = itertools.combinations(Fragments, K)
  return FragmentCombinations

def Headers(GenerateCombinations):
  FragmentCombinations = GenerateCombinations(Fragments, N)
  for FileName in FragmentCombinations:
    with open(str(FileName) + "-New.com", "a") as outputfile:
  
    FragmentCharge = 0
    LigandCharge = 0
    TotalCharge = FragmentCharge + LigandCharge
    FragmentMultiplicity = 1
    LigandMultiplicity = 1
    TotalMultiplicity = max(FragmentMultiplicity, LigandMultiplicity)

    BaseHeader = [
    "%chk=" + str(FileNumber)+ "-New" + "\n"
    "%mem=" + Mem + "GB" + "\n"
    "%nprocshared=" + Cores + "\n"
    "#" + Functional + BasisSet + "SCRF=(Solvent=" + Solvent + ")" + "\n"
    "\n"
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    "\n"
    ]

  TotalHeader = BaseHeader + [
  str(TotalCharge) + " " + str(TotalMultiplicity) + "\n"
  ]

  LigandHeader = BaseHeader + [
  str(LigandCharge) + " " + str(LigandMultiplicity) + "\n"
  ] 

  FragmentHeader = BaseHeader + [
  str(FragmentHeader) + " " + str(FragmentMultiplicity) + "\n"
  ]

  outputfile.writelines(TotalHeader)
  outputfile.writelines(ligand)
  for fragment in combo:
    outputfile.writelines(fragment)
   # outputfile.write('\n')  # Ensure each fragment is on a new line
  outputfile.write("\n--Link1--\n")
  outputfile.writelines(FragmentHeader)
  outputfile.writelines(ligand)
  for fragment in combo:
    outputfile.writelines(fragment)
    #outputfile.write('\n')  # Ensure each fragment is on a new line
  outputfile.write("\n--Link1--\n")
  outputfile.writelines(LigandHeader)
  outputfile.writelines(ligand)
  for fragment in combo:
    outputfile.writelines(fragment)
    #outputfile.write('\n')  # Ensure each fragment is on a new line

ligand, FragmentList = ReadingFile(FileName, K)
create_files(ligand,fragment_list, UserInputs)
