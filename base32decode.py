import base64

def base32_decode(input_string):
        decoded_bytes = base64.b32decode(input_string)
        return decoded_bytes.decode()
    except Exception as e:
        print(f"Gakda / Salah: {e}")
        ans = input("Masukin string Base32 yang benar: ")
        return base64.b32encode(ans.encode()).decode()

if __name__ == "__main__":
    input_string = input("Masukkan string Base32: ")
    result = base32_decode(input_string)
    print("Hasil:", result)
