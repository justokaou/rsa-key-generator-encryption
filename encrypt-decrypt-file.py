import argparse
import os

# Fonction pour charger les clés RSA
def load_key(file_path):
    with open(file_path, 'r') as file:
        key_components = file.read().split(',')
        return (int(key_components[0]), int(key_components[1]))

# Fonction pour lire le fichier par blocs
def read_file_in_blocks(filename, block_size):
    with open(filename, 'rb') as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            yield block

# Fonction pour chiffrer le fichier
def encrypt_file(input_filename, output_filename, public_key):
    e, n = public_key
    block_size = n.bit_length() // 8 - 1
    with open(output_filename, 'wb') as output_file:
        for chunk in read_file_in_blocks(input_filename, block_size):
            # Ajouter du padding si nécessaire
            if len(chunk) < block_size:
                chunk += b'\x00' * (block_size - len(chunk))
            encrypted_num = pow(int.from_bytes(chunk, 'big'), e, n)
            encrypted_chunk = encrypted_num.to_bytes((n.bit_length() + 7) // 8, 'big')
            output_file.write(encrypted_chunk)

# Fonction pour déchiffrer le fichier
def decrypt_file(input_filename, output_filename, private_key):
    d, n = private_key
    block_size = (n.bit_length() + 7) // 8
    decrypted_data = []
    with open(output_filename, 'wb') as output_file:
        for chunk in read_file_in_blocks(input_filename, block_size):
            decrypted_num = pow(int.from_bytes(chunk, 'big'), d, n)
            decrypted_chunk = decrypted_num.to_bytes(block_size, 'big').rstrip(b'\x00')
            decrypted_data.append(decrypted_chunk)
        
        # Joindre tous les morceaux déchiffrés
        decrypted_data = b''.join(decrypted_data)
        output_file.write(decrypted_data)

parser = argparse.ArgumentParser(description="Script de chiffrement et déchiffrement utilisant RSA")
parser.add_argument('-k', '--keys', required=True, help="Chemin vers le répertoire contenant les fichiers de clés RSA (public_key et private_key)")
parser.add_argument('-m', '--mode', required=True, choices=['encrypt', 'decrypt'], help="Mode : 'encrypt' pour chiffrer le fichier, 'decrypt' pour déchiffrer le fichier")
parser.add_argument('-i', '--input', required=True, help="Chemin vers le fichier d'entrée à chiffrer ou déchiffrer, y compris le nom du fichier")
parser.add_argument('-o', '--output', required=True, help="Chemin vers le fichier de sortie pour enregistrer les données chiffrées ou déchiffrées, y compris le nom du fichier")
args = parser.parse_args()

key_path = args.keys
mode = args.mode
input_file = args.input
output_file = args.output

public_key_path = os.path.join(key_path, 'public_key')
private_key_path = os.path.join(key_path, 'private_key')

public_key = load_key(public_key_path)
private_key = load_key(private_key_path)

if mode == 'encrypt':
    encrypt_file(input_file, output_file, public_key)
    print("Fichier chiffré et sauvegardé avec succès.")

elif mode == 'decrypt':
    decrypt_file(input_file, output_file, private_key)
    print("Fichier déchiffré et sauvegardé avec succès.")
