import base64
def encode(data):
    try:
        enkode = base64.b64encode(data.encode()).decode()
        return enkode
    except Exception as e:
        return f"Error / Ga beres {e}"
# STRING KE ASCII
if __name__ == "__main__":
    input_data = "" # inputannya / isinya
    print("Output [enc] = ", encode(input_data))