import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

flag_pattern = re.compile(r'flag\{[^}]+\}', re.IGNORECASE)

def process_file(file_path):
    """
    Process a single file to search for flags.
    
    Args:
        file_path (str): The path of the file to search.
        
    Returns:
        list: A list of tuples (file_path, flag) for each flag found in the file.
    """
    found = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            matches = flag_pattern.findall(content)
            if matches:
                for match in matches:
                    print(f"Found flag in {file_path}: {match}")
                    found.append((file_path, match))
    except Exception:
        pass
    return found

def multi_threaded_search(start_dir, max_workers=8):
    """
    Search for flags in files under the given directory using multi-threading.
    
    Args:
        start_dir (str): The directory to search.
        max_workers (int): Maximum number of worker threads.
    
    Returns:
        list: A list of tuples (file_path, flag) for each flag found.
    """
    found_flags = []
    file_paths = []
    
    # Collect all file paths.
    for root, dirs, files in os.walk(start_dir):
        for filename in files:
            file_paths.append(os.path.join(root, filename))
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {executor.submit(process_file, fp): fp for fp in file_paths}
        for future in as_completed(future_to_file):
            found_flags.extend(future.result())
            
    return found_flags

if __name__ == '__main__':
    directory = input("Enter the directory to search for flags: ").strip()
    
    if not os.path.isdir(directory):
        print(f"'{directory}' is not a valid directory.")
    else:
        results = multi_threaded_search(directory)
        if results:
            print("\nSummary of found flags:")
            for file_path, flag in results:
                print(f"{file_path} -> {flag}")
        else:
            print("No flags were found.")
