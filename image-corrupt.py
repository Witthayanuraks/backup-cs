import re, os, sys 
import argparse

print(f"Bismillah Jalan ......")
def extract_flag(file_path, custom_regex=None, return_all=False):
    """
    Membuka file dalam mode biner dan mencari pola flag dalam file menggunakan regex.
    
    Parameter:
      - file_path: Lokasi file yang akan diperiksa.
      - custom_regex: (Optional) Pola regex kustom untuk mencari flag.
                      Jika None, maka digunakan pola default: FLAG\{.*?\}.
      - return_all: (Optional) Jika True, fungsi akan mengembalikan list semua flag yang ditemukan.
                    Jika False, hanya flag pertama yang ditemukan yang dikembalikan.
    
    Mengembalikan:
      - Sebuah string flag jika return_all False, atau list flag jika return_all True.
      - None jika tidak ada flag yang ditemukan atau terjadi error.
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan!")
        return None
    except Exception as e:
        print("Terjadi error saat membuka file:", e)
        return None
    if custom_regex is None:
        regex_pattern = rb'FLAG\{.*?\}, Flag{.*?\}, CTF{.*?\}'
    else:
        if isinstance(custom_regex, str):
            try:
                regex_pattern = custom_regex.encode('utf-8')
            except Exception as e:
                print("Terjadi error saat encoding custom regex:", e)
                return None
        elif isinstance(custom_regex, bytes):
            regex_pattern = custom_regex
        else:
            print("Custom regex harus berupa string atau bytes.")
            return None

    try:
        pattern = re.compile(regex_pattern)
    except re.error as e:
        print("Terjadi error saat mengompilasi regex:", e)
        return None

    if return_all:
        matches = pattern.findall(data)
        flags = []
        for match in matches:
            if isinstance(match, bytes):
                try:
                    flag = match.decode('utf-8')
                except UnicodeDecodeError:
                    flag = match.decode('latin-1')
            else:
                flag = match
            flags.append(flag)
        return flags if flags else None
    else:
        match = pattern.search(data)
        if match:
            result = match.group()
            if isinstance(result, bytes):
                try:
                    flag = result.decode('utf-8')
                except UnicodeDecodeError:
                    flag = result.decode('latin-1')
            else:
                flag = result
            return flag
        else:
            return None
def get_regex_pattern():
    choice = input("Use default flag pattern (flag\\{[^}]+\\}) [?] (y/n): ").strip().lower()
    if choice == 'n':
        custom_pattern = input("Custom rgx pattern : ").strip()
        try:
            return re.compile(custom_pattern, re.IGNORECASE)
        except Exception as e:
            print(f"Invalid regex pattern. Using default instead. Error: {e}")
            return re.compile(DEFAULT_FLAG_REGEX, re.IGNORECASE)
    return re.compile(DEFAULT_FLAG_REGEX, re.IGNORECASE)

def main():
    pattern = get_regex_pattern()
    while True:
        directory = input("Enter Directory File 📂 : ").strip()
        if os.path.isdir(directory):
            break
        else:
            print(f"'{directory}' bukan directory yang valid.")
            retry = input("\n [⛭] Coba lagi? (y/n): ").strip().lower()
            if retry != 'y':
                return
    parser = argparse.ArgumentParser(
        description="Ekstrak flag dari file gambar/GIF atau dari semua file dalam direktori menggunakan custom regex."
    )
    parser.add_argument("path", help="Path ke file atau direktori yang akan diperiksa.")
    parser.add_argument(
        "--regex",
        help="Custom regex untuk mencari flag (misal: 'FLAG\\{.*?\\}')",
        default=None
    )
    parser.add_argument(
        "--all",
        help="Jika disediakan, ekstrak semua flag yang ditemukan.",
        action="store_true"
    )

    args = parser.parse_args()

    # Jika path yang diberikan adalah direktori, proses semua file di dalamnya.
    if os.path.isdir(args.path):
        print(f"Memproses direktori: {args.path}")
        # Dapatkan daftar file dalam direktori (tanpa rekursif).
        files = os.listdir(args.path)
        if not files:
            print("Direktori kosong!")
            return
        for filename in files:
            file_path = os.path.join(args.path, filename)
            # Pastikan hanya memproses file (bukan subdirektori) + subdirektori
            if os.path.isfile(file_path):
                print(f"\nMemproses file: {file_path}")
                result = extract_flag(file_path, custom_regex=args.regex, return_all=args.all)
                if result:
                    if isinstance(result, list):
                        print("Flag ditemukan:")
                        for flag in result:
                            print(flag)
                    else:
                        print("Flag ditemukan:", result)
                else:
                    print("Flag tidak ditemukan!")
    elif os.path.isfile(args.path):
        # Jika path merupakan file, proses file tersebut.
        result = extract_flag(args.path, custom_regex=args.regex, return_all=args.all)
        if result:
            if isinstance(result, list):
                print("Flag ditemukan:")
                for flag in result:
                    print(flag)
            else:
                print("Flag ditemukan:", result)
        else:
            print("Flag gakda")
    else:
        print(f"Path '{args.path}' tidak valid. Pastikan path tersebut merupakan file atau direktori.")

if __name__ == '__main__':
    main()
