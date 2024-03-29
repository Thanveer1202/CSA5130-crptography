import random

def generate_cipher_key():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabet)
    return {chr(97 + i): alphabet[i] for i in range(26)}

def monoalphabetic_substitution_encrypt(message, cipher_key):
    return ''.join(cipher_key.get(char.lower(), char) if char.isalpha() else char for char in message)

def monoalphabetic_substitution_decrypt(encrypted_message, cipher_key):
    decryption_key = {value: key for key, value in cipher_key.items()}
    return ''.join(decryption_key.get(char.lower(), char) if char.isalpha() else char for char in encrypted_message)

def main():
    message = input("Enter a message: ")
    cipher_key = generate_cipher_key()
    encrypted_message = monoalphabetic_substitution_encrypt(message, cipher_key)
    print("Encrypted message:", encrypted_message)
    decrypted_message = monoalphabetic_substitution_decrypt(encrypted_message, cipher_key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
