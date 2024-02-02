import csv
import itertools
from  itertools import combinations
from collections import defaultdict
#Aquireing the inputs to create the header:
k=int(input("How many amino acids are in the structure?: "))
N=int(input("How many amino acids would you like to include in the interaction?: "))
UnCorrFileName = str(input("Which file would you like to open? (Do not include .com): "))
FileName = UnCorrFileName + ".com"
##%chk=FileName.chk - This line will be added in the Header.
#%mem=memGB
#nprocshared=Cores
#Functional, Basis set, Solvent, Other input
Mem=str(int(input("How much memory would you like to use (In GB)?: ")))
Cores=str(int(input("How many cores would you like to use?: ")))
Functional=input("Which functional would you like to use?: ")
BasisSet=input("Which basis set would you like to use?: ")
Solvent=input("Which solvent would you like to use? If none, leave blank: ")
OtherInput=input("Would you like any other commands in the command line? If none, leave blank: ")

#--Searching the File for Ligand and Fragments:--
def ReadingFile():
    Ligand = []
    with open(FileName, 'r') as File:
        for line in File:
            if "(Fragment=1)" in line:
                Ligand.append(line)
    return Ligand
    F = defaultdict(list)
    FragmentList = F
    for i in range(3,k+1,1):
        with open(FileName, 'r')as File:
            Fragment = "Fragment="+str(i)
            for line in File:
                if Fragment in line:
                    F[i-1].append(line)
    return FragmentList
    
    #Creating the combinations:
    AllCombos += itertools.combinations(FragmentList,N)
    return AllCombos

#---------------------------------
#^^^Everything Above Here works^^^
#---------------------------------


def CreateFiles(ReadingFile):
    l = 2
    x = 1
    f = open (l,"w")
    with f as outputfile:
        w = csv.writer(outputfile, delimiter = " ")
        FragmentCharge = 0
        FragmentMultiplicity = 1
        LigandCharge = 0
        LigandMultiplicity = 1
        TotalCharge = FragmentCharge + LigandCharge
        if LigandMultiplicity > FragmentMultiplicity:
            TotalMultiplicity = LigandMultiplicity
        else:
            TotalMultiplicity = FragmentMultiplicity

    def BaseHeader():
        w.writerow(["%chk="+ l+ ".chk"])
        w.writerow(["%mem="+ Mem+ "GB"])
        w.writerow(["nprocshared="+ Cores])
        w.writerow(["#", Functional, " ", BasisSet, "SCRF=Solvent=", Solvent+ ")", " ", OtherInput])
        w.writerow([" "])
        w.writerow(["Title Card Required"])
        w.writerow([" "])
    
    def MainHeader():
        w.writerow([BaseHeader()])
        w.writerow([TotalCharge+ TotalMultiplicity])


    def LigandHeader():
        w.writerow([BaseHeader()])
        w.writerow([LigandCharge+ LigandMultiplicity])


    def FragmentHeader():
        w.writerow([BaseHeader()])
        w.writerow([FragmentCharge+ FragmentMultiplicity])
    
    while l < k+2:
        w.writerow([MainHeader()])
        w.writerow([Ligand])
        w.writerow([AllCombos[x]])
        w.writerow([" "])
        w.writerow(["--Link1--"])
                #Need to make Ligand Bq
                #Will need to change header charge
        w.writerow([FragmentHeader()])
        w.writerow([Ligand()])
        w.writerow([AllCombos[x]])
        w.writerow([" "])
        w.writerow(["--Link1--"])
                #Need to make ActualCombinations Bq
                #Can use string.replace(Fragment=X/-Bq)
                #Will need to change header charge
        w.writerow([LigandHeader()])
        w.writerow([Ligand()])
        w.writerow([AllCombos[x]])
        w.writerow([" "])
    l = l + 1
    x = x + 1 

print(CreateFiles(ReadingFile))
