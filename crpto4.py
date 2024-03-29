def generate_cipher_alphabets(key):
    cipher_alphabets = []
    for char in key:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        shifted_alphabet = alphabet[alphabet.index(char):] + alphabet[:alphabet.index(char)]
        cipher_alphabets.append(shifted_alphabet)
    return cipher_alphabets

def polyalphabetic_encrypt(message, key):
    cipher_alphabets = generate_cipher_alphabets(key)
    encrypted_message = ""
    key_index = 0
    for char in message:
        if char.isalpha():
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            shift = ord(cipher_alphabets[key_index][alphabet.index(char.lower())]) - ord(alphabet[0])
            encrypted_char = chr((ord(char) - ord(alphabet[0]) + shift) % 26 + ord(alphabet[0]))
            encrypted_message += encrypted_char.upper() if char.isupper() else encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_message += char
    return encrypted_message

def main():
    message = input("Enter the plaintext message: ")
    key = input("Enter the key: ")

    encrypted_message = polyalphabetic_encrypt(message, key)
    print("Encrypted message:", encrypted_message)

if __name__ == "__main__":
    main()
