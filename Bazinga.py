import re
import os

# Open a text file to write the results
with open("SCF_values_in_files.txt", "w") as output_file:
    for filename in os.listdir(directory):
        if filename.endswith(".log"):
            filepath = os.path.join(directory, filename)
            SCF_values = []

            try:
                with open(filepath, 'r') as file:
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
