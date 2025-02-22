import base64

def base32_encode(input_string):
    try:
        base32_encoded = base64.b32encode(input_string.encode()).decode()
        print(f"Encoded Base32: {base32_encoded}")
    except Exception as e:
        print(f"Error: {e}")
        ans = input("Masukkan string yang valid: ")
        base32_encode(ans) 

if __name__ == "__main__":
    input_string = input("Masukin = ") 
    base32_encode(input_string)
