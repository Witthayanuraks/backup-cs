# import module as newname
# import os

data = [122, 123, 124, 125, 126, 127]
key = 13

def xor(encrypted_data, key):
    try:
        decrypted_data = [x ^ key for x in encrypted_data]
        return decrypted_data
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    result = xor(data, key)
    if result:
        print("[R] Output:", result)
