import pikepdf
import logging
from os import unittest
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# config.logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# init path nya
file_kata_sandi = ""
file_pdf = ""

if not os.path.exists(file_kata_sandi):
    logging.error(f".f pw : '{file_kata_sandi}' tidak ditemukan.")
    exit(1)
if not os.path.exists(file_pdf):
    logging.error(f".f pdf :'{file_pdf}' tidak ditemukan.")
    exit(1)

# cek list apa yang sandi bilang
with open(file_kata_sandi, "r", encoding="utf-8", errors="ignore") as f:
    daftar_kata_sandi = [baris.strip() for baris in f]
logging.info(f"Berhasil memuat {len(daftar_kata_sandi)} kata sandi dari '{file_kata_sandi}'.")

def coba_kata_sandi(kata_sandi):
    try:
        with pikepdf.open(file_pdf, password=kata_sandi) as pdf:
            return kata_sandi  
    except pikepdf._qpdf.PasswordError:
        return None

# Proses multithreading untuk mencoba kata sandi
kata_sandi_tertemukan = None
with ThreadPoolExecutor(max_workers=10) as executor:  
    futures = {executor.submit(coba_kata_sandi, kata): kata for kata in daftar_kata_sandi}
    for future in tqdm(as_completed(futures), desc="Membuka PDF", total=len(daftar_kata_sandi)):
        hasil = future.result()
        if hasil:  
            kata_sandi_tertemukan = hasil
            break

# Menampilkan hasil
if kata_sandi_tertemukan:
    logging.info(f"[... +] Ada: {kata_sandi_tertemukan}")
else:
    logging.warning("[... -] Gak:9")
