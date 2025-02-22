def caesarchip(text):
    for shift in range(26):
        result = ''.join(
            chr((ord(c) - 65 + shift) % 26 + 65) if c.isupper() else
            chr((ord(c) - 97 + shift) % 26 + 97) if c.islower() else c
            for c in text
        )
        print(f"[/]  {shift}: {result}")

# Contoh penggunaan
text = "JAM{code}"
caesarcipheralshi(text);