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
    return json_files

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

def write_to_csv(json_file, unique_keys):
    """Write extracted data to a CSV file in the same directory as the JSON file."""
    # Create the CSV filename based on the JSON filename
    csv_filename = os.path.splitext(json_file)[0] + '.csv'
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        header = ['Request'] + unique_keys
        writer.writerow(header)
        
        # Write each row of data
        info = extract_info(json_file)
        for req_key, req_data in info.items():
            row = [req_key] + [req_data.get(key, '') for key in unique_keys]
            writer.writerow(row)

    print(f"Data from {json_file} has been written to {csv_filename}")

if __name__ == "__main__":
    # Set the directory to search for JSON files
    root_dir = '.'
    
    # Find all JSON files in the directory and subdirectories
    json_files = find_json_files(root_dir)
    
    # Collect all unique keys from the 'info' sections
    unique_keys = collect_unique_keys(json_files)
    
    # Convert each JSON file to CSV in the same directory
    for json_file in json_files:
        write_to_csv(json_file, unique_keys)
