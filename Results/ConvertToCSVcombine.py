import os
import json
import csv

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

def find_json_files(root_dir):
    """Recursively find all JSON files in a directory."""
    json_files = []
    for dirpath, _, filenames in walklevel(root_dir):
        for filename in filenames:
            if filename.endswith('.json'):
                json_files.append(os.path.join(dirpath, filename))
    return sorted(json_files)

def extract_info(json_file):
    """Extract 'info' data from a JSON file."""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get('info', {})

def collect_unique_keys(json_files):
    """Collect all unique keys from the 'info' sections."""
    unique_keys = set()
    for json_file in json_files:
        info = extract_info(json_file)
        for req_key, req_data in info.items():
            unique_keys.update(req_data.keys())
    unique_keys.discard('str')  # Remove the 'str' key
    return sorted(unique_keys)

def write_to_csv(json_files, unique_keys, output_csv):
    """Write extracted data to a CSV file."""
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the first header row
        header = []
        for unique_key in unique_keys:
            header.append('Request')
            header.append(unique_key)
            for i in range(1, len(json_files)):
                header.append('')
        print(header)
        writer.writerow(header)

        # Write the second header row
        header = []
        for unique_key in unique_keys:
            header.append('')
            for file_path in json_files:
                file_name = os.path.basename(file_path).split(".")[0]
                file_name = file_name.replace("_GPT_3_5_TURBO", "")
                header.append(file_name)

        print(header)
        writer.writerow(header)

        # load the data from disk
        data = []
        # Write each row of data
        column_base_index = 1
        columns_total = len(json_files) * len(unique_keys)
        for json_file in json_files:
            info = extract_info(json_file)

            row_index = 0
            for req_key, req_data in info.items():
                column_index = column_base_index

                if len(data) <= row_index:
                    data.append(([req_key] + [''] * (len(json_files))) * (len(unique_keys)))

                for key in unique_keys:
                    item = req_data.get(key, '')
                    
                    data[row_index][column_index] = item
                    column_index += len(json_files) + 1
                row_index += 1
            column_base_index += 1

        # replace dots with commas in floats
        for row in data:
            for i in range(len(row)):
                row[i] = str(row[i]).replace(".", ",")

        # Write each row of data
        for row in data:
            print(row)
            writer.writerow(row)

    print(f"Data has been written to {output_csv}")

if __name__ == "__main__":
    # Set the directory to search for JSON files
    root_dir = '.'
    
    # Output CSV file name
    one_shot_csv = 'one_shot.csv'
    iterative_csv = 'iterative.csv'
    
    # Find all JSON files in the directory and subdirectories
    json_files = find_json_files(root_dir)
    one_shot = []
    iterative = []
    for json_file in json_files:
        if "one_shot" in os.path.basename(json_file):
            one_shot.append(json_file)
        else:
            iterative.append(json_file)
    
    # Collect all unique keys from the 'info' sections
    unique_keys = collect_unique_keys(json_files)
    
    # Convert each JSON file to CSV in the same directory
    write_to_csv(one_shot, unique_keys, one_shot_csv)
    write_to_csv(iterative, unique_keys, iterative_csv)
