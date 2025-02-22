import socket

host = "ctf.antix.or.id"
port = 60901

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    data = s.recv(1024)
    if not data:
        break
    print(data.decode(), end="")  # Menampilkan output dari server
    
    user_input = input()  # Meminta input dari user
    s.sendall(user_input.encode() + b"\n")  # Mengirim input ke server



# Tutup koneksi ke server
s.close()
