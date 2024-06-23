# Dictionary mapping specific coordinates to their corresponding amino acids and labels
coordinate_to_amino_acid = {
    "-5.83097600   -0.87369600   -6.96591900 L": "Ala1",
    "-6.16731500   -1.00122300   -5.55078900 L": "Ala2",
    "-1.77912300    6.17102700   -1.47821900 L": "Cys2",
    # Add more coordinates and corresponding amino acids here
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
