# Functions to load RSA keys
def load_key(file_path):
    with open(file_path, 'r') as file:
        key_components = file.read().split(',')
        return (int(key_components[0]), int(key_components[1]))

# Function to read the file in blocks
def read_file_in_blocks(filename, block_size):
    with open(filename, 'rb') as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            yield block

# Function to encrypt the file
def encrypt_file(filename, public_key):
    e, n = public_key
    encrypted_data = []
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(n.bit_length() // 8 - 1)  # read blocks slightly smaller than the key size
            if not chunk:
                break
            encrypted_num = pow(int.from_bytes(chunk, 'big'), e, n)
            encrypted_data.append(encrypted_num.to_bytes((n.bit_length() + 7) // 8, 'big'))
    return encrypted_data

# Function to decrypt the file
def decrypt_file(encrypted_data, private_key):
    d, n = private_key
    decrypted_data = []
    for data in encrypted_data:
        decrypted_num = pow(int.from_bytes(data, 'big'), d, n)
        decrypted_data.append(decrypted_num.to_bytes((n.bit_length() + 7) // 8, 'big'))
    return b''.join(decrypted_data)

public_key = load_key('public_key.txt')
private_key = load_key('private_key.txt')

# Path to the file to be encrypted/decrypted
file_path = "test.txt"

encrypted_data = encrypt_file(file_path, public_key)
with open('encrypted_test.txt', 'wb') as file:
    file.writelines(encrypted_data)

decrypted_data = decrypt_file(encrypted_data, private_key)
with open('decrypted_test.txt', 'wb') as file:
    file.write(decrypted_data)
