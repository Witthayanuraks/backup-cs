import os
import re
import time

DEFAULT_FLAG_REGEX = r'flag\{[^}]+\}'
CHUNK_SIZE = 400000


print("Bismillah Berjalan .... ➛")

def get_regex_pattern():
    choice = input("Use default flag pattern (flag\\{[^}]+\\})? (y/n): ").strip().lower()
    if choice == 'n':
        custom_pattern = input("Custom rgx pattern: ").strip()
        try:
            return re.compile(custom_pattern, re.IGNORECASE)
        except Exception as e:
            print(f"Invalid regex pattern. Using default instead. Error: {e}")
            return re.compile(DEFAULT_FLAG_REGEX, re.IGNORECASE)
    return re.compile(DEFAULT_FLAG_REGEX, re.IGNORECASE)

def process_file_in_chunks(file_path, pattern, max_attempts=3, wait_time=2):
    print("\n ↴ ")
    print("📂 Processing {file_path}...")
    found = []
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                buffer = ""
                while True:
                    chunk = file.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    buffer += chunk
                    matches = pattern.findall(buffer)
                    if matches:
                        for match in matches:
                            print(f"Found flag in {file_path}: {match}")
                            found.append((file_path, match))
                    buffer = buffer[-100:]
            break
        except FileNotFoundError:
            attempts += 1
            print(f"File {file_path} tidak ditemukan. Attempt {attempts} dari {max_attempts}. Retrying dalam {wait_time} detik...")
            time.sleep(wait_time)
        except KeyboardInterrupt:
            print("\nProses file dihentikan oleh pengguna.")
            raise
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            break
    return found

def search_directory(directory, pattern):
    print(" ⤳ ⤳ ⤳ Nyari dulu bentar ....")
    found_flags = []
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                found_flags.extend(process_file_in_chunks(file_path, pattern))
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"Skipping file {file_path} karena error: {e}")
    return found_flags

def save_results_to_file(results):
    file_name = input("Enter output file name (e.g. results.txt): ").strip()
    try:
        with open(file_name, 'w', encoding='utf-8') as out_file:
            out_file.write("Flag Search Results\n")
            out_file.write("===================\n")
            out_file.write(f"Scan Date: {time.strftime('%Y-%m-%d')}\n")
            out_file.write(f"Total flags found: {len(results)}\n\n")
            out_file.write("File Path -> Flag\n")
            for file_path, flag in results:
                out_file.write(f"{file_path} -> {flag}\n")
        print(f"Results saved to {file_name}.")
    except Exception as e:
        print(f"Error saving results: {e}")

def main():
    pattern = get_regex_pattern()
    while True:
        directory = input("Enter Directory File 📂 : ").strip()
        if os.path.isdir(directory):
            break
        else:
            print(f"'{directory}' bukan directory yang valid.")
            retry = input("[⛭] Coba lagi? (y/n): ").strip().lower()
            if retry != 'y':
                return

    # Main scanning loop.
    while True:
        print(f"[Ξ] Validasi ....  {time.strftime('%Y-%m-%d')} ...")
        print("\n ↴ ")
        print(f"[⚙] Running everything ....")
        try:
            results = search_directory(directory, pattern)
        except KeyboardInterrupt:
            print("\nScanning has stoped. Aku Pergi...")
            return

        if results:
            print("\n ↴ ")
            print("🗂️ Summary of found flags:")
            for file_path, flag in results:
                print(f"{file_path} -> {flag}")
            print(f"sum flags funds: {len(results)}")
        else:
            print("null 😞...")

        save_choice = input("Do you want to save the results to a file? (y/n): ").strip().lower()
        if save_choice == 'y':
            save_results_to_file(results)

        # Tanya apakah pengguna ingin melakukan scan direktori lain.
        scan_again = input("Scan any directory? (y/n): ").strip().lower()
        if scan_again == 'y':
            directory = input("Enter new Directory File 📂 : ").strip()
            if not os.path.isdir(directory):
                print(f"'{directory}' bukan directory yang valid. Keluar.")
                break
        else:
            print("Exiting. !")
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting gracefully.")
