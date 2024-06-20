import os
import re
import pandas as pd

def extract_scf_done_values(log_directory):
    scf_done_values = []
    scf_done_pattern = re.compile(r'SCF Done:\s+E\(\w+\)\s+=\s+(-?\d+\.\d+)')
    
    # Traverse the log directory
    for root, _, files in os.walk(log_directory):
        for file in files:
            if file.endswith('.log'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    for line in f:
                        match = scf_done_pattern.search(line)
                        if match:
                            scf_done_values.append(float(match.group(1)))
                            break  # Only take the first match in each file

    return scf_done_values

def save_to_excel(data, output_file):
    df = pd.DataFrame(data, columns=['SCF Done Values'])
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    log_directory = "/path/to/your/log/files"  # Update this to your directory
    output_file = "scf_done_values.xlsx"
    
    scf_done_values = extract_scf_done_values(log_directory)
    save_to_excel(scf_done_values, output_file)
    print(f"Extracted {len(scf_done_values)} values and saved to {output_file}.")
