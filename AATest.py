coordinate_to_amino_acid = {
    "C     0   -6.16731500   -1.00122300   -5.55078900 L": "Gly",
    "C     0   -10.72451300   -2.37171300   -1.74666900 L": "Thr",
    "C     0   -8.57988800   -5.52315400    0.73636700 L": "Ala",
    "C     0   -1.51049800   -5.38618600    1.41090200 L": "Val",
    "C     0   -4.93146600   -6.47255500    0.16402800 L": "Ser",
    "C     0   -1.73113300    7.70030600   -1.27190700 L": "Phe",
    "C     0   -6.17476800    4.70639800   -2.24849100 L": "Val 2",
    "C     0   -9.94217300    2.86969300    2.23217500 L": "Trp",
    "C     0   4.52841600   -4.76143000    1.68304500 L": "Gly2",
    "C     0   5.06477900    0.58726100    6.48299200 L": "Ile",
    "C     0   8.47649100    2.28203500   -2.41588500 L": "Tyr",
    "C     0   4.90693600    4.74026800    3.18086700 L": "Cys",
    "C     0   11.16489700   -2.34085000   -2.33665000 L": "His",
    "C     0   9.96330700   -2.32906500    1.27171100 L": "Gly 3",    
}

def search_coordinates_in_file(file_name):
    found_amino_acids = []
    try:
        with open(file_name, 'r') as file:
            print(f"Searching coordinates in file: {file_name}")
            for line in file:
                stripped_line = line.strip()
                found = False
                for key in coordinate_to_amino_acid:
                    if stripped_line.startswith(key):
                        found_amino_acid = coordinate_to_amino_acid[key]
                        print(f"Coordinates found: {stripped_line}")
                        print(f"Corresponding amino acid: {found_amino_acid}")
                        found_amino_acids.append(found_amino_acid)
                        found = True
                        break  # Break out of inner loop once a match is found
                if found:
                    # If you want to find all occurrences, do not break here
                    pass
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error processing file '{file_name}': {str(e)}")
    
    return found_amino_acids

if __name__ == "__main__":
    file_name = "1-New.com"
    amino_acids = search_coordinates_in_file(file_name)
    if amino_acids:
        print(f"Found amino acids corresponding to the coordinates: {amino_acids}")
    else:
        print("No matching amino acids found for the coordinates.")
