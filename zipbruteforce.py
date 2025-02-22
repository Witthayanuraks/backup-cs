import os
import base64
import os.path

WORDLIST_PATH = "wordlist.txt" 
# penggunaan wordlist 
ZIP = "arsip.zip"
OUTPUT = "extracted"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Nyari pw nya
def openZIP():
  with open(WORDLIST_PATH, "r") as wordlist:
    for password in wordlist:
      password = password.strip()
      print(f"[?] Lihat list kata: {password}")
      try:
        with zipfile.ZipFile(ZIP) as rarfiles:
          zipfiles.extractall(path=OUTPUT_DIR, pwd=password)
          print(f"[+] Password ditemukan: '{password}'")
          findingfile()
          return
      except rarfile.RarWrongPassword:
        print(f"[-] Password salah: '{password}'")
      except Exception as e:
        print(f"[!] Error: {e}")
  print("[!] Tidak ada password yang cocok di wordlist")
