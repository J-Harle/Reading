import os
import re
import xlsxwriter

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
    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()

    # Write header
    worksheet.write(0, 0, 'SCF Done Values')

    # Write data
    for row_num, value in enumerate(data, 1):
        worksheet.write(row_num, 0, value)
    
    workbook.close()

if __name__ == "__main__":
    log_directory = "/path/to/your/log/files"  # Update this to your directory
    output_file = "scf_done_values.xlsx"
    
    scf_done_values = extract_scf_done_values(log_directory)
    save_to_excel(scf_done_values, output_file)
    print(f"Extracted {len(scf_done_values)} values and saved to {output_file}.")
