from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_aes_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_aes_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def encrypt_aes_cbc(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_aes_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
   
    plaintext = b'Hello, world!'
    key = get_random_bytes(16)  
    iv = get_random_bytes(16) 

   
    ciphertext_ecb = encrypt_aes_ecb(plaintext, key)
    print("ECB Mode - Ciphertext:", ciphertext_ecb.hex())

    
    decrypted_ecb = decrypt_aes_ecb(ciphertext_ecb, key)
    print("ECB Mode - Decrypted:", decrypted_ecb.decode())

    
    ciphertext_cbc = encrypt_aes_cbc(plaintext, key, iv)
    print("CBC Mode - Ciphertext:", ciphertext_cbc.hex())

   
    decrypted_cbc = decrypt_aes_cbc(ciphertext_cbc, key, iv)
    print("CBC Mode - Decrypted:", decrypted_cbc.decode())

if __name__ == "__main__":
    main()
