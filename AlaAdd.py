  from collections import defaultdict
import itertools

def UserInputs():
    k = int(input("How many amino acids are in the structure?: "))
    N = int(input("How many amino acids would you like to include in the interaction?: "))
    UnCorrFileName = input("Which file would you like to open? (Do not include .com): ")
    FileName = f"{UnCorrFileName}.com"
    Mem = str(int(input("How much memory would you like to use (In GB)?: ")))
    Cores = str(int(input("How many cores would you like to use?: ")))
    Functional = input("Which functional would you like to use?: ")
    BasisSet = input("Which basis set would you like to use?: ")
    if BasisSet.strip() == "":
        BasisSet = "" #Allows for PM6 to be used
    Solvent = input("Which solvent would you like to use? If none, leave blank: ")
    CorrSolvent = f"SCRF=(Solvent={Solvent})" if Solvent.lower() != "none" else ""
    OtherInput = input("Would you like any other commands in the command line? If none, leave blank: ")
    if OtherInput.strip() == "":
        OtherInput = ""
    return k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent

def ReadingFile(FileName, k):
    ligand = []
    fragment_list = defaultdict(list)

    with open(FileName, 'r') as file:
        for line in file:
            if "(Fragment=1)" in line:
                ligand.append(line)
            for i in range(3, k+3, 1): # k+3 as first fragment is ligand and there is no fragment 2
                fragment = f"Fragment={i}"
                if fragment in line:
                    fragment_list[i - 1].append(line)

    # Create copies of ligand and fragment lists then line.replace
    bq_ligand = ligand.copy()
    blank_ligand = ligand.copy()
    bq_fragment_list = fragment_list.copy()
    blank_fragment_list = fragment_list.copy()
    
    for i in range(1, k+3):
        bq_ligand = [line.replace(f"(Fragment={i})", "-Bq") for line in bq_ligand]
        blank_ligand = [line.replace(f"(Fragment={i})", " ") for line in blank_ligand]
        bq_fragment_list[i - 1] = [line.replace(f"(Fragment={i})", "-Bq") for line in bq_fragment_list[i - 1]]
        blank_fragment_list[i - 1] = [line.replace(f"(Fragment={i})", " ") for line in blank_fragment_list[i - 1]]

    return ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list

def GenerateCombinations(Fragments, K):
    FragmentCombinations = itertools.combinations(Fragments, K)
    return FragmentCombinations

def Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list):
    k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
    counter = 1  
    for combo in FragmentCombinations:
        OutputFile = f"{counter}-New.com"  
        with open(OutputFile, "w") as outputfile: 
            FragmentCharge = 0 
            LigandCharge = 1    
            FragmentMultiplicity = 1
            LigandMultiplicity = 1
            TotalCharge = FragmentCharge + LigandCharge
            TotalMultiplicity = max(FragmentMultiplicity, LigandMultiplicity)
            
            BaseHeader = [
                f"%chk={counter}-New.chk\n",
                f"%mem={Mem}GB\n",
                f"%nprocshared={Cores}\n",
                f"#{Functional} {BasisSet} {CorrSolvent}\n",
                "\n",
                "Josh Harle - MSc Project Code\n",
                "\n"
            ]

            TotalHeader = BaseHeader + [f"{TotalCharge} {TotalMultiplicity}\n"]

            LigandHeader = BaseHeader + [f"{LigandCharge} {LigandMultiplicity}\n"]
            
            FragmentHeader = BaseHeader + [f"{FragmentCharge} {FragmentMultiplicity}\n"]


            Ala = [ 
              N                 -7.29235700   -5.91669600    0.15769400
              C                 -8.57988800   -5.52315400    0.73636700
              C                 -9.14530500   -6.54482100    1.74166000
              O                 -9.92591300   -6.18422000    2.64679400
              C                 -9.60419000   -5.38980300   -0.39704200
              H                 -7.24168100   -6.05566000   -0.84305700
              H                 -8.47780100   -4.58596700    1.28927800
              H                 -9.72462300   -6.34711200   -0.91200600
              H                 -9.26383800   -4.63630900   -1.10858900
              H                -10.57273300   -5.08847200    0.00654500
              O                 -8.76586600   -7.91880900    1.62915300
              H                 -9.21672300   -8.43827600    2.32769400
              H                 -6.55416120   -6.05342196    0.67196336
           ]

          bq_Ala = [
              N-Bq                 -7.29235700   -5.91669600    0.15769400
              C-Bq                 -8.57988800   -5.52315400    0.73636700
              C-Bq                 -9.14530500   -6.54482100    1.74166000
              O-Bq                 -9.92591300   -6.18422000    2.64679400
              C-Bq                 -9.60419000   -5.38980300   -0.39704200
              H-Bq                 -7.24168100   -6.05566000   -0.84305700
              H-Bq                 -8.47780100   -4.58596700    1.28927800
              H-Bq                 -9.72462300   -6.34711200   -0.91200600
              H-Bq                 -9.26383800   -4.63630900   -1.10858900
              H-Bq                -10.57273300   -5.08847200    0.00654500
              O-Bq                 -8.76586600   -7.91880900    1.62915300
              H-Bq                 -9.21672300   -8.43827600    2.32769400
              H-Bq                 -6.55416120   -6.05342196    0.67196336
           ]
            
            w = outputfile.writelines
            
            # Ligand + Frag1 + Frag2 + Frag3
            w(TotalHeader)
            w(blank_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(Ala)
            w("\n--Link1--\n")
            
            # Ligand + Frag1(Bq) + Frag2 + Frag3
            w(LigandHeader)
            w(blank_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(Ala)
            w("\n--Link1--\n")
            
            # Ligand + Frag1 + Frag2(Bq) + Frag3
            w(LigandHeader)
            w(blank_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(Ala)
            w("\n--Link1--\n")
            
            # Ligand + Frag1 + Frag2 + Frag3(Bq)
            w(LigandHeader)
            w(blank_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(bq_Ala)
            w("\n--Link1--\n")
            
            # Ligand + Frag1(Bq) + Frag2(Bq) + Frag3
            w(LigandHeader)
            w(blank_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(Ala)
            w("\n--Link1--\n")
            
            # Ligand + Frag1(Bq) + Frag2 + Frag3(Bq)
            w(LigandHeader)
            w(blank_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(bq_Ala)
            w("\n--Link1--\n")
            
            # Ligand + Frag1 + Frag2(Bq) + Frag3(Bq)
            w(LigandHeader)
            w(blank_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(bq_Ala)
            w("\n--Link1--\n")
            
            # Ligand + Frag1(Bq) + Frag2(Bq) + Frag3(Bq)
            w(LigandHeader)
            w(blank_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(bq_Ala)
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1 + Frag2 + Frag3
            w(FragmentHeader)
            w(bq_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(Ala)
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1(Bq) + Frag2 + Frag3
            w(FragmentHeader)
            w(bq_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(Ala)
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1 + Frag2(Bq) + Frag3
            w(FragmentHeader)
            w(bq_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(Ala)
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1 + Frag2 + Frag3(Bq)
            w(FragmentHeader)
            w(bq_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(bq_Ala)
            w("\n--Link1--\n")

            # Ligand(Bq) + Frag1(Bq) + Frag2(Bq) + Frag3
            w(FragmentHeader)
            w(bq_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(Ala)
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1(Bq) + Frag2 + Frag3(Bq)
            w(FragmentHeader)
            w(bq_ligand)
            w(bq_fragment_list[combo[0] - 1])
            w(blank_fragment_list[combo[1] - 1])
            w(bq_Ala)
            w("\n--Link1--\n")
            
            # Ligand(Bq) + Frag1 + Frag2(Bq) + Frag3(Bq)
            w(FragmentHeader)
            w(bq_ligand)
            w(blank_fragment_list[combo[0] - 1])
            w(bq_fragment_list[combo[1] - 1])
            w(bq_Ala)
            w("\n")
          
        counter += 1

user_inputs = UserInputs()
k, N, FileName, Mem, Cores, Functional, BasisSet, CorrSolvent = user_inputs
ligand, bq_ligand, blank_ligand, fragment_list, bq_fragment_list, blank_fragment_list = ReadingFile(FileName, k)
FragmentCombinations = GenerateCombinations(fragment_list.keys(), N)
Headers(FragmentCombinations, ligand, user_inputs, bq_ligand, blank_ligand, bq_fragment_list, blank_fragment_list)
