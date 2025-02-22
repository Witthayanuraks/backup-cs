import sys
import hashlib
from argon2 import PasswordHasher
from cryptography.fernet import Fernet

# ----------------------- Fungsi Hashing -----------------------

def generate_hash_md5(password):
    print("Tunggu Bentar ...")
    return hashlib.md5(password.encode()).hexdigest()

def generate_hash_sha1(password):
    print("Tunggu Bentar ...")
    return hashlib.sha1(password.encode()).hexdigest()

def generate_hash_sha224(password):
    print("Tunggu Bentar ...")
    return hashlib.sha224(password.encode()).hexdigest()

def generate_hash_sha256(password):
    print("Tunggu Bentar ...")
    return hashlib.sha256(password.encode()).hexdigest()

def generate_hash_sha384(password):
    print("Tunggu Bentar ...")
    return hashlib.sha384(password.encode()).hexdigest()

def generate_hash_sha512(password):
    print("Tunggu Bentar ...")
    return hashlib.sha512(password.encode()).hexdigest()

# Konfigurasi Argon2 menggunakan PasswordHasher (argon2-cffi)
ph = PasswordHasher(
    time_cost=2,              # Jumlah iterasi (sesuaikan dengan kebutuhan)
    memory_cost=1024 * 128,   # Memory cost dalam kibibytes
    parallelism=2,
    hash_len=32,
)

def generate_hash_argon2(password):
    print("Tunggu Bentar ...")
    try:
        return ph.hash(password)
    except Exception as e:
        print(f"[E] Gagal membuat hash Argon2: {e}")
        sys.exit(1)

# ----------------------- Fungsi Enkripsi & Dekripsi -----------------------

def encrypt_text(text, key):
    """
    Mengenkripsi teks menggunakan kunci simetris (Fernet).
    """
    try:
        f = Fernet(key)
        encrypted = f.encrypt(text.encode())
        return encrypted.decode()
    except Exception as e:
        print(f"[E] Enkripsi gagal: {e}")
        sys.exit(1)

def decrypt_text(token, key):
    """
    Mendekripsi teks terenkripsi menggunakan kunci simetris (Fernet).
    """
    try:
        f = Fernet(key)
        decrypted = f.decrypt(token.encode())
        return decrypted.decode()
    except Exception as e:
        print(f"[E] Dekripsi gagal: {e}")
        sys.exit(1)

# ----------------------- Fungsi Utilitas -----------------------

def exit_program():
    print("[D] Program selesai")
    sys.exit(0)

def verify_lowercase(password):
    return any(char.islower() for char in password)

def verify_uppercase(password):
    return any(char.isupper() for char in password)

def validate_password(password):
    if not password:
        print("[E] Password tidak boleh kosong!")
        sys.exit(1)
    if not verify_lowercase(password):
        print("[E] Password harus mengandung setidaknya satu huruf kecil!")
        sys.exit(1)
    if not verify_uppercase(password):
        print("[E] Password harus mengandung setidaknya satu huruf besar!")
        sys.exit(1)
    print("[P] Password sudah valid")

# ----------------------- Main Program -----------------------

def main():
    print("Pilih operasi:")
    print("1. Hashing (satu arah)")
    print("2. Enkripsi (dua arah)")
    print("3. Dekripsi (dua arah)")
    operasi = input("[i] Masukkan pilihan (1/2/3): ").strip()

    if operasi == "1":
        # --- Proses Hashing ---
        password = input("[i] Masukkan password: ")
        validate_password(password)
        print("\nPilih metode hash:")
        print(" - argon2")
        print(" - md5")
        print(" - sha1")
        print(" - sha224")
        print(" - sha256")
        print(" - sha384")
        print(" - sha512")
        hash_type = input("[i] Masukkan jenis hash: ").lower()
        
        hash_options = {
            'argon2': generate_hash_argon2,
            'md5': generate_hash_md5,
            'sha1': generate_hash_sha1,
            'sha224': generate_hash_sha224,
            'sha256': generate_hash_sha256,
            'sha384': generate_hash_sha384,
            'sha512': generate_hash_sha512,
        }
        
        if hash_type in hash_options:
            hashed_password = hash_options[hash_type](password)
            print(f"\n[i] Jenis hash yang dipilih: {hash_type}")
            print(f"[i] Password: {password}")
            print(f"[P] Hashed Password: {hashed_password}")
        else:
            print(f"[E] Metode hash '{hash_type}' tidak ditemukan.")
    
    elif operasi == "2":
        # --- Proses Enkripsi ---
        plaintext = input("[i] Masukkan teks yang ingin dienkripsi: ")
        print("\n[i] Untuk enkripsi, kunci (key) harus berupa 32-byte Base64-encoded string.")
        key_input = input("[i] Masukkan key (kosong untuk generate key baru): ").strip()
        if not key_input:
            key = Fernet.generate_key()
            print(f"[i] Generated key: {key.decode()}")
        else:
            key = key_input.encode()
        
        encrypted_text = encrypt_text(plaintext, key)
        print(f"\n[P] Teks terenkripsi: {encrypted_text}")
    
    elif operasi == "3":
        # --- Proses Dekripsi ---
        token = input("[i] Masukkan teks terenkripsi: ")
        key_input = input("[i] Masukkan key untuk dekripsi: ").strip()
        if not key_input:
            print("[E] Key harus disediakan untuk dekripsi!")
            sys.exit(1)
        key = key_input.encode()
        
        decrypted_text = decrypt_text(token, key)
        print(f"\n[P] Teks terdekripsi: {decrypted_text}")
    
    else:
        print("[E] Pilihan tidak dikenali!")
    
    exit_program()

if __name__ == '__main__':
    main()
