import string

def generate_cipher_sequence(keyword):
 
    cipher_sequence = list(keyword.upper())

  
    keyword = keyword.lower()

   
    for letter in string.ascii_lowercase:
        if letter not in keyword:
            cipher_sequence.append(letter.upper())

    return ''.join(cipher_sequence)

def encrypt(plaintext, cipher_sequence):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            index = ord(char.lower()) - ord('a')
            if 0 <= index < 26:
                encrypted_char = cipher_sequence[index]
                if char.isupper():
                    ciphertext.append(encrypted_char)
                else:
                    ciphertext.append(encrypted_char.lower())
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def main():
    keyword = "CIPHER"
    cipher_sequence = generate_cipher_sequence(keyword)

    plaintext = input("Enter the plaintext: ")
    encrypted_text = encrypt(plaintext, cipher_sequence)

    print("Cipher sequence generated from keyword:", cipher_sequence)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
