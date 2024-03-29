def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def break_affine_cipher(frequent_letter, second_frequent_letter, frequent_count, second_frequent_count):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Calculate the key 'a' using the known frequencies
    a = (alphabet.index(frequent_letter) - alphabet.index(second_frequent_letter)) * mod_inverse(frequent_count - second_frequent_count, 26) % 26
    
    # Calculate the key 'b' using the known frequencies and the calculated 'a'
    b = (alphabet.index(frequent_letter) - (a * frequent_count)) % 26
    
    return a, b

def decrypt_affine_cipher(ciphertext, a, b):
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Decrypt each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():
            char_index = (mod_inverse(a, 26) * (alphabet.index(char) - b)) % 26
            plaintext += alphabet[char_index]
        else:
            plaintext += char
    
    return plaintext

def main():
    ciphertext = "BUVBVBUVUBUVUBVVVVVVBVVVBUVUBVBUVBUVVVVVBUVVVVVVVBVUBVVVBUVVBVU"
    frequent_letter = "B"
    second_frequent_letter = "U"
    frequent_count = 14
    second_frequent_count = 11
    
    a, b = break_affine_cipher(frequent_letter, second_frequent_letter, frequent_count, second_frequent_count)
    print("Calculated key 'a':", a)
    print("Calculated key 'b':", b)
    
    decrypted_message = decrypt_affine_cipher(ciphertext, a, b)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()



