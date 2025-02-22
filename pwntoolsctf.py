# how to use this feature in code
# --------------------------------
# hased this into everything need it 
# 
# 
# 
# 
#  

# ----------------------------------------------------------------
from pwn import *
import sys
import hashlib
import pynput
# ----------------------------------------------------------------
def hash_to_hex(hash_str):
    print("hash to hex... formating ")
    return ''.join(format(ord(c), '02x') for c in hash_str)
    try:
        return hashlib.sha256(hash_str.encode()).hexdigest()
    except UnicodeDecodeError:
        return 'Error: Non-Latin characters found in password'
    except Exception as e:
        return 'Error: {}'.format(e)

def brute_force_crack(wanted_hash):
    print("Brute force cracking... ")
    try:
        with open(password_list_file, "r", encoding='latin-1') as password_file:
            for password in password_file:
                password = password.strip('\n')
                password_hash = hashlib.sha256(password.encode()).hexdigest()
                if password_hash == wanted_hash:
                    print("Found password: {}".format(password))
                    sys.exit(0)
                attempts += 1
    except FileNotFoundError:
        print("Password list file not found")
        sys.exit(1)

if len(sys.argv) != 3:
    print("Invalid arguments")
    print("Usage: python3 %s <hash> <password_list>" % sys.argv[0])
    sys.exit(1)

wanted_hash = sys.argv[1]
password_list_file = sys.argv[2]
attempts = 0

with log.progress("Attempting to crack: {}! ".format(wanted_hash)) as p:
    try:
        with open(password_list_file, "r", encoding='latin-1') as password_file:
            for password in password_file:
                password = password.strip('\n')
                password_hash = hashlib.sha256(password.encode()).hexdigest()
                if password_hash == wanted_hash:
                    p.success("Found password: {}".format(password))
                    sys.exit(0)
                attempts += 1
        p.failure("Password not found after {} attempts".format(attempts))
    except FileNotFoundError:
                p.failure("Password list file not found")
                sys.exit(1)
        
with log.proces("Attempting to back: {}! ".format(wanted_hash)) as p:
    with open(password, "r", encoding='latin-1') as password:
        for password in passwordlist :
            password = password.strip()
            p.info("Trying password: {}".format(password))
            try:
                p.sendline(password)
                if p.recvline().decode().strip() == wanted_hash:
                    p.info("Found password: {}".format(password))
                    sys.exit(0)
                attempts += 1
            except EOFError:
                break 
def any_execution(self):
    p = pwnlib.tubes.process.process(self.partition(string))
    p.interactive()
    self.close()
    self.p = p
    def close(self):
        if hasattr(self, 'p'):
            self.p.close()

def sendline(self, string):
    self.p.sendline(string)
    return self.p.sendline

def recvline(self):
    print ("recvline: {}".format(self))
    if hasattr(self, 'p'):
        return self.p.recvline().decode().strip()




if name == 'main':
    main()