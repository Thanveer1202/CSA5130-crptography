def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isalpha():  
            
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  

    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, shift):
    decrypted_message = ""

    for char in encrypted_message:
        if char.isalpha():  
            
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char

    return decrypted_message

def main():
    message = input("Enter a message: ")
    
    
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if shift < 1 or shift > 25:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 25.")

    encrypted_message = caesar_cipher_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()

