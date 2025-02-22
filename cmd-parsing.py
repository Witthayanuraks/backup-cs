import os
import re
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="CTF Flag Finder: Search for flag patterns in files within a directory."
    )
    parser.add_argument(
        "directory",
        help="The directory to search for flags."
    )
    parser.add_argument(
        "-e", "--extension",
        help="Optional file extension filter (e.g., '.txt'). Only files with this extension will be searched.",
        default=None
    )
    parser.add_argument(
        "-p", "--pattern",
        help="Optional custom regex pattern for the flag. Default is 'flag\\{[^}]+\\}'.",
        default=r'flag\{[^}]+\}'
    )
    return parser.parse_args()

def search_for_flags(start_dir, flag_regex, extension_filter=None):
    """
    Recursively search for flag patterns in all files under the given directory.
    
    Args:
        start_dir (str): Directory path.
        flag_regex (str): The regular expression string to search for.
        extension_filter (str): Optional file extension filter.
        
    Returns:
        list: A list of tuples (file_path, flag) for each flag found.
    """
    flag_pattern = re.compile(flag_regex, re.IGNORECASE)
    found_flags = []
    
    for root, dirs, files in os.walk(start_dir):
        for filename in files:
            if extension_filter and not filename.endswith(extension_filter):
                continue
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
    args = parse_arguments()
    
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory.")
        exit(1)
    
    results = search_for_flags(args.directory, args.pattern, args.extension)
    if results:
        print("\nSummary of found flags:")
        for file_path, flag in results:
            print(f"{file_path} -> {flag}")
    else:
        print("No flags were found.")
