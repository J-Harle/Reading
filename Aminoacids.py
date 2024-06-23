# Coordinates of Alpha-Carbons for each of the amino acids
coordinate_to_amino_acid = {
    "-6.1673150    -1.0012230   -5.5507890 L": "Gly",
    "-10.7245130   -2.3717130   -1.7466690 L": "Thr",
    "-8.5798880    -5.5231540   0.7363670 L": "Ala",
    "-1.5104980    -5.3861860   1.4109020 L": "Val",
    "-4.9314660    -6.4725550   0.1640280 L": "Ser",
    "-1.7311330     7.7003060   -1.2719070L": "Phe",
    "-6.1747680 4.7063980 -2.2484910 L": "Val 2",
    "-9.9421730 2.8696930 2.2321750 L": "Trp",
    "4.5284160 -4.7614300 1.6830450 L": "Gly2",
    "5.0647790  0.5872610 6.4829920 L": "Ile",
    "8.4764910 2.2820350 -2.4158850 L": "Tyr",
    "4.9069360 4.7402680 3.1808670 L": "Cys",
    "11.1648970 -2.3408500 -2.3366500 L": "His",
    "9.9633070 -2.3290650 1.2717110 L": "Gly 3",    
}

# Function to search for specific coordinates in a file
def search_coordinates_in_file(file_name):
    found_amino_acids = set()
    try:
        with open(file_name, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line in coordinate_to_amino_acid:
                    found_amino_acids.add(coordinate_to_amino_acid[stripped_line])
    except FileNotFoundError:
        pass  # Skip the file if it doesn't exist
    return found_amino_acids

# Function to search for coordinates in multiple files
def search_coordinates_in_files(max_file_number):
    all_found_amino_acids = {}
    for file_number in range(1, max_file_number + 1):
        file_name = str(file_number)
        found_amino_acids = search_coordinates_in_file(file_name)
        all_found_amino_acids[file_name] = found_amino_acids
    return all_found_amino_acids

# Example usage
if __name__ == "__main__":
    max_file_number = 100  # Set the maximum number of files to check
    results = search_coordinates_in_files(max_file_number)
    
    for file_name, amino_acids in results.items():
        if amino_acids:
            amino_acids_list = ' '.join(amino_acids)
            print(f"{file_name}: [{amino_acids_list}]")
