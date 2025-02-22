import os
import base64
import os.path

WORDLIST_PATH = "wordlist.txt" 
# penggunaan wordlist 
RAR_PATH = "arsip.rar"
OUTPUT_DIR = "extracted"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Nyari pw nya
def openrar():
  with open(WORDLIST_PATH, "r") as wordlist:
    for password in wordlist:
      password = password.strip()
      print(f"[?] Lihat list kata: {password}")
      try:
        with rarfile.RarFile(RAR_PATH) as rarfiles:
          rarfiles.extractall(path=OUTPUT_DIR, pwd=password)
          print(f"[+] Password ditemukan: '{password}'")
          findingfile()
          return
      except rarfile.RarWrongPassword:
        print(f"[-] Password salah: '{password}'")
      except Exception as e:
        print(f"[!] Error: {e}")
  print("[!] Tidak ada password yang cocok di wordlist")


























# Decode isinya pake looping
def decodedfilelist(inputdecode):
  try:
    decoded_content = base64.b64decode(inputdecode).decode("utf-8")
    print(f"[+] Decoded berhasil, ulangi decode...")
    decodedfilelist(decoded_content)
  except Exception as e:
    print("[-] Maksimal, decode sudah error!")
    print(f"[!] Hasil yang ditemukan {inputdecode}")
    return

# Cari file abis di eksekusi
def findingfile():
  for root, _, files in os.walk(OUTPUT_DIR):
    for file in files:
      if file.endswith(".txt"):
        file_path = os.path.join(root, file)
        with open(file_path, "r") as f:
          content = f.read()
          decodedfilelist(content)

if __name__ == "__main__":
  openrar()