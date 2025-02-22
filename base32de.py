import base64

def base32_decode(input_string):
    try:
        decoded_bytes = base64.b32decode(input_string)
        return decoded_bytes.decode()
    except Exception as e:
        print(f"log: {e}")
        ans = input("Input: ")
        return base32_decode(ans)

if __name__ == "__main__":
    input_string = input("[i] Input string : ")
    result = base32_decode(input_string)
    print("[R] Hasil:", result)
