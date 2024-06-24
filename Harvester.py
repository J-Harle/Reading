import re
import os

# Number of files to process, change accordingly
num_files = 364  

# Open a text file to write the results
with open("SCF_values_in_files.txt", "w") as output_file:
    for counter in range(1, num_files + 1):
        filename = f"{counter}-New.log"
        SCF_values = []

        if not os.path.isfile(filename):
            output_file.write(f"{filename} does not exist.\n")
            continue

        try:
            with open(filename, 'r') as file:
                for line in file:
                    # Look for lines containing "SCF Done" followed by a value with "A.U."
                    match = re.search(r"SCF Done:\s*E\(RBMK\) =\s*([-\d\.]+)\s+A\.U\.", line)
                    if match:
                        SCF_values.append(match.group(1))

            if SCF_values:
                output_file.write(f"SCF values in {filename}:\n")
                for value in SCF_values:
                    output_file.write(f"{value}\n")
            else:
                output_file.write(f"No SCF values with A.U. found in {filename}\n")
        
        except Exception as e:
            output_file.write(f"An error occurred while processing {filename}: {e}\n")
