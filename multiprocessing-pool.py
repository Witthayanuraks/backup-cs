import os
import re
from multiprocessing import Pool, cpu_count

FLAG_REGEX = r'flag\{[^}]+\}'
flag_pattern = re.compile(FLAG_REGEX, re.IGNORECASE)

def search_for_flags(start_dir):
    """
    Recursively search for flag patterns in all files under the given directory.
    Returns a list of tuples (file_path, flag).
    """
    found = []
    for root, dirs, files in os.walk(start_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            found.extend(process_file(file_path))
    return found

def process_file(file_path):
    """
    Process a single file to search for flag patterns.
    Returns a list of tuples (file_path, flag).
    """
    found = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            matches = flag_pattern.findall(content)
            for match in matches:
                print(f"Found flag in {file_path}: {match}")
                found.append((file_path, match))
    except Exception:
        pass
    return found

def collect_file_paths(start_dir):
    """
    Recursively collect all file paths under the given directory.
    """
    file_paths = []
    for root, _, files in os.walk(start_dir):
        for filename in files:
            file_paths.append(os.path.join(root, filename))
    return file_paths

def main():
    directory = input("Enter the directory to search for flags: ").strip()
    if not os.path.isdir(directory):
        print(f"'{directory}' is not a valid directory.")
        return

    file_paths = collect_file_paths(directory)
    found_flags = []

    # Use as many processes as the number of CPU cores available.
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_file, file_paths)
        for res in results:
            found_flags.extend(res)

    if found_flags:
        print("\nSummary of found flags:")
        for file_path, flag in found_flags:
            print(f"{file_path} -> {flag}")
    else:
        print("No flags were found.")

if __name__ == '__main__':
    main()
