import os
import re
import asyncio
import aiofiles
import hashlib
from stegano import lsb
import exifread

# # 
# file_path = '../Doc'

# Regular expression for CTF flag pattern
FLAG_REGEX = r'flag\{[^}]+\}'
flag_pattern = re.compile(FLAG_REGEX, re.IGNORECASE)


async def custom_flag_pattern(filename, flag_pattern):
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            matches = flag_pattern.findall(content)
            for match in matches:
                print(f"[FLAG] Found in {filename}: {match}")
                yield match
    except Exception:
        pass

async def process_file_for_flags(file_path):
    found = []
    try:
        async with aiofiles.open(file_path, mode='r', encoding='utf-8', errors='ignore') as file:
            content = await file.read()
            matches = flag_pattern.findall(content)
            for match in matches:
                print(f"[FLAG] Found in {file_path}: {match}")
                found.append((file_path, match))
    except Exception:
        pass
    return found

async def process_file_for_hashes(file_path):
    """Compute file hashes (MD5, SHA-1, SHA-256)."""
    try:
        async with aiofiles.open(file_path, mode='rb') as file:
            content = await file.read()
            md5_hash = hashlib.md5(content).hexdigest()
            sha1_hash = hashlib.sha1(content).hexdigest()
            sha256_hash = hashlib.sha256(content).hexdigest()
            print(f"[HASH] {file_path} -> MD5: {md5_hash}, SHA-1: {sha1_hash}, SHA-256: {sha256_hash}")
    except Exception:
        pass

async def process_image_metadata(file_path):
    """Extract metadata from image files."""
    try:
        with open(file_path, 'rb') as img:
            tags = exifread.process_file(img)
            print(f"[METADATA] {file_path} ->")
            for tag, value in tags.items():
                print(f"    {tag}: {value}")
    except Exception:
        pass

async def process_steganography(file_path):
    """Check for hidden messages using LSB steganography."""
    try:
        secret_message = lsb.reveal(file_path)
        if secret_message:
            print(f"[STEGANOGRAPHY] Hidden message in {file_path}: {secret_message}")
    except Exception:
        pass

async def async_search(start_dir, mode):
    """Asynchronously search files based on the selected mode."""
    tasks = []
    for root, _, files in os.walk(start_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            if mode == '1':
                tasks.append(process_file_for_flags(file_path))
            elif mode == '2':
                tasks.append(process_file_for_hashes(file_path))
            elif mode == '3':
                if filename.lower().endswith(('jpg', 'jpeg', 'png')):
                    tasks.append(process_image_metadata(file_path))
            elif mode == '4':
                if filename.lower().endswith(('png', 'bmp')):
                    tasks.append(process_steganography(file_path))
    await asyncio.gather(*tasks)

def main():
    """Main function to execute the tool based on user selection."""
    print("\nChoose an option:")
    print("1. Search for flags in files")
    print("2. Compute hashes of files")
    print("3. Extract metadata from images")
    print("4. Check for hidden messages in images")
    print("5. -")
    
    mode = input("Enter (1-4): ").strip()
    if mode not in ('1', '2', '3', '4'):
        print("Aku Pergi ...")
        return
    
    directory = input("Enter the directory to scan: ").strip()
    if not os.path.isdir(directory):
        print(f"'{directory}' is not a valid directory.")
        return
    
    asyncio.run(async_search(directory, mode))

if __name__ == '__main__':
    main()
