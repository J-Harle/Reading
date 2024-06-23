coordinate_to_amino_acid = {
    "-6.1673150 -1.0012230 -5.5507890 L": "Gly",
    "-10.7245130 -2.3717130 -1.7466690 L": "Thr",
    "-8.5798880 -5.5231540 0.7363670 L": "Ala",
    "-1.5104980 -5.3861860 1.4109020 L": "Val",
    "-4.9314660 -6.4725550 0.1640280 L": "Ser",
    "-1.7311330 7.7003060 -1.2719070 L": "Phe",
    "-6.1747680 4.7063980 -2.2484910 L": "Val 2",
    "-9.9421730 2.8696930 2.2321750 L": "Trp",
    "4.5284160 -4.7614300 1.6830450 L": "Gly2",
    "5.0647790 0.5872610 6.4829920 L": "Ile",
    "8.4764910 2.2820350 -2.4158850 L": "Tyr",
    "4.9069360 4.7402680 3.1808670 L": "Cys",
    "11.1648970 -2.3408500 -2.3366500 L": "His",
    "9.9633070 -2.3290650 1.2717110 L": "Gly 3",    
}

def search_first_coordinates_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Searching first coordinates in file: {file_name}")
            for line in file:
                stripped_line = line.strip()
                print(f"Checking line: '{stripped_line}'")  # Debugging output
                if stripped_line in coordinate_to_amino_acid:
                    found_amino_acid = coordinate_to_amino_acid[stripped_line]
                    print(f"First set of coordinates found: {stripped_line}")
                    print(f"Corresponding amino acid: {found_amino_acid}")
                    return found_amino_acid
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error processing file '{file_name}': {str(e)}")
    
    return None

if __name__ == "__main__":
    file_name = "1-New.com"  # Specify the file to test with
    amino_acid = search_first_coordinates_in_file(file_name)
    if amino_acid:
        print(f"First set of coordinates correspond to amino acid: {amino_acid}")
    else:
        print("No matching amino acid found for the first set of coordinates.")
