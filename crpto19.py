from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def encrypt_3des_cbc(plaintext, key):
    iv = get_random_bytes(8)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)
    return iv + ciphertext  

def main():
    plaintext = b'Hello, world!'
    key = b'1234567890abcdef12345678'

    ciphertext = encrypt_3des_cbc(plaintext, key)
    print("Ciphertext:", ciphertext.hex())

if __name__ == "__main__":
    main()
