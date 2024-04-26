import random
import sympy

def generate_prime(bits):
    """Generates a prime number of 'bits' bits"""
    min_value = 1 << (bits - 1)
    max_value = (1 << bits) - 1
    return sympy.randprime(min_value, max_value)

def gcd(a, b):
    """Calculates the GCD of two numbers using sympy's gcd function"""
    return sympy.gcd(a, b)

def modinv(a, m):
    """Calculates the modular inverse using sympy's inverse function"""
    return int(sympy.mod_inverse(a, m))

def generate_rsa_key_pair(bits):
    """Generates an RSA key pair"""
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    d = modinv(e, phi_n)
    return (e, n), (d, n)

def encrypt(message, public_key):
    """Encrypts a message with a public key"""
    e, n = public_key
    if isinstance(message, str):
        message = string_to_int(message)
        message_type = 0  # 0 for string
    elif isinstance(message, int):
        message_type = 1  # 1 for int

    encrypted_message = pow(message, e, n)
    return (encrypted_message, message_type)

def decrypt(encrypted_message, private_key):
    """Decrypts a message with a private key"""
    encrypted_num, message_type = encrypted_message
    d, n = private_key
    decrypted_int = pow(encrypted_num, d, n)

    if message_type == 0:  # It was a string
        try:
            return int_to_string(decrypted_int)
        except ValueError:
            return "String decoding error"
    else:  # It was an integer
        return decrypted_int

def string_to_int(s):
    """Converts a string to a large integer"""
    return int.from_bytes(s.encode('utf-8'), 'big')

def int_to_string(i):
    """Converts a large integer back to a string"""
    length = (i.bit_length() + 7) // 8
    bytes_array = i.to_bytes(length, 'big')
    return bytes_array.decode('utf-8', 'ignore')

def save_keys(public_key, private_key):
    with open('public_key.txt', 'w') as f:
        f.write(f"{public_key[0]},{public_key[1]}")  # e,n
    with open('private_key.txt', 'w') as f:
        f.write(f"{private_key[0]},{private_key[1]}")  # d,n

# Example usage
bits = 4096
public_key, private_key = generate_rsa_key_pair(bits)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

# Encrypt an integer
message = ""
encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

# Decrypt
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)

save_keys(public_key, private_key)

