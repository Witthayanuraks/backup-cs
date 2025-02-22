#Selesai 
import base64

def encode(data):
    try:
        enkode = base64.b64encode(data.encode()).decode()
        return enkode
    except Exception as e:
        return f"Error / Ga beres {e}"

if __name__ == "__main__":
    # Example usage
    input_data = "Hello world!"
    print("Encoded:", encode(input_data))
