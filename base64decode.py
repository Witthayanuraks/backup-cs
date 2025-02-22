# Selesai
import base64

def decode_string(input_string):
    try:
        decoded_bytes = base64.b64decode(input_string)
        return decoded_bytes.decode()
    except Exception as e:
        return f"[!] Gakda / Cek lagi {e}"

def encodeteks(input_string):
    return base64.b64encode(input_string.encode()).decode()

if __name__ == "__main__":
    input_str = "Hello" # isinya 
    print("[!] Keluar nih", decode_string(input_str))    
