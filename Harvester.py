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
                content = file.read()
                # Debugging: Print a small part of the content to check if it's being read correctly
                print(f"Reading {filename}, content preview: {content[:100]}...")

                # Find all occurrences of SCF Done followed by a value with A.U
                matches = re.findall(r"SCF Done:\s*([\d\.\-E+]+)\s*A\.U", content)
                if matches:
                    SCF_values.extend(matches)

            if SCF_values:
                output_file.write(f"SCF values in {filename}:\n")
                for value in SCF_values:
                    output_file.write(f"{value}\n")
            else:
                output_file.write(f"No SCF values with A.U found in {filename}\n")
        
        except Exception as e:
            output_file.write(f"An error occurred while processing {filename}: {e}\n")
            # Debugging: Print the error message
            print(f"An error occurred while processing {filename}: {e}\n")
