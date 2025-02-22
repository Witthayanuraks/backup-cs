# xor eksekusi 

import import os

data = [122 , 123 , 124 , 125 , 126 , 127]
key = 13

def xor_decrypt(encrypted_data, key):
        try:
    decrypted_data = [x ^ key for x in encrypted_data]
    return decrypted_data
    print(xor_decrypt(encrypted_data, key));
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    xor_decrypt(data, key)