from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad5
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 8

def print_hex(prefix, data):
    print(f"{prefix}: {' '.join([hex(byte)[2:].zfill(2).upper() for byte in data])}")

def encrypt_decrypt_ecb(plaintext, key, mode):
    cipher = DES.new(key, DES.MODE_ECB)
    if mode == 'encrypt':
        ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))
    elif mode == 'decrypt':
        ciphertext = unpad(cipher.decrypt(plaintext), BLOCK_SIZE)
    return ciphertext

def encrypt_decrypt_cbc(plaintext, key, iv, mode):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    if mode == 'encrypt':
        ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))
    elif mode == 'decrypt':
        ciphertext = unpad(cipher.decrypt(plaintext), BLOCK_SIZE)
    return ciphertext

def encrypt_decrypt_cfb(plaintext, key, iv, mode):
    cipher = DES.new(key, DES.MODE_CFB, iv)
    if mode == 'encrypt':
        ciphertext = cipher.encrypt(plaintext)
    elif mode == 'decrypt':
        ciphertext = cipher.decrypt(plaintext)
    return ciphertext

def main():
    plaintext = b'Hello, world!' 
    key = get_random_bytes(BLOCK_SIZE)
    iv = get_random_bytes(BLOCK_SIZE)

    print("Plaintext:", plaintext.decode())

    print("\nECB Mode Encryption:")
    ciphertext_ecb = encrypt_decrypt_ecb(plaintext, key, 'encrypt')
    print_hex("Ciphertext", ciphertext_ecb)

    print("\nECB Mode Decryption:")
    decrypted_ecb = encrypt_decrypt_ecb(ciphertext_ecb, key, 'decrypt')
    print("Decrypted:", decrypted_ecb.decode())

    print("\nCBC Mode Encryption:")
    ciphertext_cbc = encrypt_decrypt_cbc(plaintext, key, iv, 'encrypt')
    print_hex("Ciphertext", ciphertext_cbc)

    print("\nCBC Mode Decryption:")
    decrypted_cbc = encrypt_decrypt_cbc(ciphertext_cbc, key, iv, 'decrypt')
    print("Decrypted:", decrypted_cbc.decode())

    print("\nCFB Mode Encryption:")
    ciphertext_cfb = encrypt_decrypt_cfb(plaintext, key, iv, 'encrypt')
    print_hex("Ciphertext", ciphertext_cfb)

    print("\nCFB Mode Decryption:")
    decrypted_cfb = encrypt_decrypt_cfb(ciphertext_cfb, key, iv, 'decrypt')
    print("Decrypted:", decrypted_cfb.decode())

if __name__ == "__main__":
    main()
