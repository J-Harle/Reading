#Coordinates of the alpha carbons of each amino acid (Change according to active site)
alpha_c_coord = {
    "C     0   -6.16731500   -1.00122300   -5.55078900 L": "Gly",
    "C     0  -10.72451300   -2.37171300   -1.74666900 L": "Thr",
    "C                 -8.57988800   -5.52315400    0.73636700": "Ala",
    "C    0   -1.51049800   -5.38618600    1.41090200 L": "Val",
    "C    0   -4.93146600   -6.47255500    0.16402800 L": "Ser",
    "C     0   -1.73113300    7.70030600   -1.27190700 L": "Phe",
    "C     0   -6.17476800    4.70639800   -2.24849100 L": "Val2",
    "C     0   -9.94217300    2.86969300    2.23217500 L": "Trp",
    "C    0    4.52841600   -4.76143000    1.68304500 L": "Gly2",
    "C    0    5.06477900    0.58726100    6.48299200 L": "Ile",
    "C    0    8.47649100    2.28203500   -2.41588500 L": "Tyr",
    "C    0    4.90693600    4.74026800    3.18086700 L": "Cys",
    "C     0   11.16489700   -2.34085000   -2.33665000 L": "His",
    "C     0    9.96330700   -2.32906500    1.27171100 L": "Gly3",
}
# Number of files to process, change accordingly
num_files = 364  

# Open a text file to write the results
with open("amino_acids_in_files.txt", "w") as output_file:
    for counter in range(1, num_files + 1):
        filename = f"{counter}-New.com"
        AA_in_file = []

        with open(filename, 'r') as file:
            content = file.read()
            for coord, AA in alpha_c_coord.items():
                if coord in content:
                    if AA not in AA_in_file:
                        AA_in_file.append(AA)
                    if len(AA_in_file) == 3:
                        break

        output_file.write(f"Amino acids in {filename}: {'-'.join(AA_in_file)}\n")
