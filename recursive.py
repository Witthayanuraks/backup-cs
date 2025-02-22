import os
import re

flag_pattern = re.compile(r'flag\{[^}]+\}', re.IGNORECASE)

def search_for_flags(start_dir):
    """
    Recursively search for flag patterns in all files under the given directory.
    
    Args:
        start_dir (str): The directory path to start searching from.
        
    Returns:
        list: A list of tuples (file_path, flag) for each flag found.
    """
    found_flags = []
    
    for root, dirs, files in os.walk(start_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    matches = flag_pattern.findall(content)
                    if matches:
                        for match in matches:
                            print(f"Found flag in {file_path}: {match}")
                            found_flags.append((file_path, match))
            except Exception:
                continue
    return found_flags

if __name__ == '__main__':
    directory = input("Enter the directory to search for flags: ").strip()
    
    if not os.path.isdir(directory):
        print(f"'{directory}' is not a valid directory.")
    else:
        results = search_for_flags(directory)
        if results:
            print("\nSummary of found flags:")
            for file_path, flag in results:
                print(f"{file_path} -> {flag}")
        else:
            print("No flags were found.")
