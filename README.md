
# Python RSA generator and encryption

This project is a project with two script. The first one generates an RSA key pair, and the second allows for encrypting and decrypting a file.


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![](https://img.shields.io/badge/Python-red)]()
[![](https://img.shields.io/badge/Sympy-green)]()


## Run Locally

Clone the project

```bash
  git clone https://github.com/dyfault-eth/rsa-key-generator-encryption.git
```

Go to the project directory

```bash
  cd rsa-key-generator-encryption
```

Install dependencies

```bash
  pip install -r requirements.txt
```


## Usage/Examples

Help

```bash
    python generate-rsa-key.py -h
```

```bash
    python encrypt-file.py -h
```

Start key generation

```bash
  python generate-rsa-key.py --bits 4096 --ouput ./rsa_keys
```

Encrypt file

```bash
  python encrypt-file.py --mode encrypt --keys ./rsa_keys --input ./input_files/decrypted_files/test.txt --output ./output_files/encrypted_files/test.txt
```

Decrypt file

```bash
  python encrypt-file.py --mode decrypt --keys ./rsa_keys --input ./input_files/encrypted_files/test.txt --output ./output_files/decrypted_files/test.txt
```


## Authors

- [@dyfault-eth](https://www.github.com/dyfault-eth)

