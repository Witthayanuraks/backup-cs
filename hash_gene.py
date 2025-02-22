import sys
import hashlib
from argon2 import PasswordHasher

# ----------------------- Hash Functions -----------------------

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

# Configure Argon2 via PasswordHasher (requires argon2-cffi)
ph = PasswordHasher(
    time_cost=2,              # Number of iterations (adjust as needed)
    memory_cost=1024 * 128,   # Memory cost in kibibytes
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

# ----------------------- Utility Functions -----------------------

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
    # User Inputs
    password = input("[i] Masukkan password: ")
    validate_password(password)
    
    hash_type = input("[i] Pilih metode hash: ").lower()
    
    # Hash-processing options
    options = {
        'argon2': generate_hash_argon2,
        'md5': generate_hash_md5,
        'sha1': generate_hash_sha1,
        'sha224': generate_hash_sha224,
        'sha256': generate_hash_sha256,
        'sha384': generate_hash_sha384,
        'sha512': generate_hash_sha512,
        'zero': exit_program,
        '0': exit_program,
        'zero/0': exit_program,
    }
    
    if hash_type in options:
        hashed_password = options[hash_type](password)
        print(f"[i] Jenis hash yang dipilih: {hash_type}")
        print(f"[i] Password: {password}")
        print(f"[P] Hashed Password: {hashed_password}")
    else:
        print(f"[E] Metode hash '{hash_type}' tidak ditemukan.")
    
    exit_program()

if __name__ == '__main__':
    main()
