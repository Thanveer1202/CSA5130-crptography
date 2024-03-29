def modular_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def validate_a(a):
    inverse = modular_inverse(a, 26)
    return inverse != -1

def encrypt(plaintext, a, b):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(((a * (ord(char) - base) + b) % 26) + base)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, a, b):
    decrypted_text = ''
    inverse = modular_inverse(a, 26)
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(((inverse * ((ord(char) - base) - b + 26)) % 26) + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    if not validate_a(a):
        print("Invalid value of 'a'. Please choose another value.")
        return

    plaintext = "Affine Caesar Cipher"
    print("\nPlaintext:", plaintext)

    
    ciphertext = encrypt(plaintext, a, b)
    print("Encrypting...")
    print("Ciphertext:", ciphertext)

 
    decrypted_text = decrypt(ciphertext, a, b)
    print("\nDecrypting...")
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
