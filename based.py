## TOOLS UNTUK MENGEKSEKUSI 
# base32 de / en
# base45 de / en
# base58 de / en
# base62 de / en
# base64 de / en
# base85 de / en
# base92 de / en
# base95 de / en
# Setiap kode dari base64 adalah code uniq yang dimana saat penggunaanya 
# kita harus menggunakan padding 
# `padding n = 1 ` untuk memberikan jarak 
# antara ` 1 character dan value ` dan eksekusinya menggunakan bytes / secara utf-8
import base64

# === Alphabet untuk eksekusi base58 pake blockchain
BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def encode_base58(b: bytes) -> str:
    num = int.from_bytes(b, byteorder="big")
    encode = ""
    while num > 0:
        num, rem = divmod(num, 58)
        encode = BASE58_ALPHABET[rem] + encode
    n_pad = 0
    for byte in b:
        if byte == 0:
            n_pad += 1
        else:
            break
    return BASE58_ALPHABET[0] * n_pad + encode

def decode_base58(s: str) -> bytes:
    num = 0
    for char in s:
        num = num * 58 + BASE58_ALPHABET.index(char)
    b = num.to_bytes((num.bit_length() + 7) // 8, byteorder="big")
    n_pad = 0
    for char in s:
        if char == BASE58_ALPHABET[0]:
            n_pad += 1
        else:
            break
    return b'\x00' * n_pad + b
# === untuk eksekusi base62 
BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode_base62(b: bytes) -> str:
    num = int.from_bytes(b, byteorder="big")
    if num == 0:
        return BASE62_ALPHABET[0]
    encode = ""
    while num > 0:
        num, rem = divmod(num, 62)
        encode = BASE62_ALPHABET[rem] + encode
    return encode

def decode_base62(s: str) -> bytes:
    num = 0
    for char in s:
        num = num * 62 + BASE62_ALPHABET.index(char)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder="big")

# Aksek modul exeternal
try:
    import base45
except ImportError:
    base45 = None

try:
    import base92
except ImportError:
    base92 = None

def main():
    print("1. Encode")
    print("2. Decode")
    op = input(" = ").strip()

    if op not in ['1', '2']:
        print("Gakda")
        return
    print("1. Base32")
    print("2. Base45")
    print("3. Base58")
    print("4. Base62")
    print("5. Base64")
    print("6. Base85")
    print("7. Base92")
    tipe = input(" = ").strip()

    if op == '1':
        data = input("\n Input string yang mawu diencode: ")
        b_data = data.encode('utf-8')
        try:
            if tipe == '1':
                hasil = base64.b32encode(b_data).decode('utf-8')
            elif tipe == '2':
                if base45 is None:
                    print("Coba cek MODULnya , kalo gakda coba Install dulu pip install base45")
                    return
                hasil = base45.b45encode(b_data).decode('utf-8')
            elif tipe == '3':
                hasil = encode_base58(b_data)
            elif tipe == '4':
                hasil = encode_base62(b_data)
            elif tipe == '5':
                hasil = base64.b64encode(b_data).decode('utf-8')
            elif tipe == '6':
                hasil = base64.b85encode(b_data).decode('utf-8')
            elif tipe == '7':
                if base92 is None:
                    print("Coba cek MODULnya , kalo gakda coba Install dulu pip install base92")
                    return
                hasil = base92.encode(b_data)
            else:
                print("GAkda.")
                return
            print("\nHasil encode:", hasil)
        except Exception as e:
            print("eRROR:", e)

    elif op == '2':  
        data = input("\nInput string yang mawu didecode: ")
        try:
            if tipe == '1':
                b_hasil = base64.b32decode(data)
            elif tipe == '2':
                if base45 is None:
                    print("Coba cek MODULnya , kalo gakda coba Install pip install base45")
                    return
                b_hasil = base45.b45decode(data)
            elif tipe == '3':
                b_hasil = decode_base58(data)
            elif tipe == '4':
                b_hasil = decode_base62(data)
            elif tipe == '5':
                b_hasil = base64.b64decode(data)
            elif tipe == '6':
                b_hasil = base64.b85decode(data)
            elif tipe == '7':
                if base92 is None:
                    print("Coba cek MODULnya , kalo gakda coba Install pip install base92")
                    return
                b_hasil = base92.decode(data)
            else:
                print("Gakda.")
                return
        except Exception as e:
            print("eRROR:", e)
            return
        try:
            hasil = b_hasil.decode('utf-8')
        except UnicodeDecodeError:
            hasil = b_hasil
        print("\nOtputnya decode:", hasil)

if __name__ == '__main__':
    main()
