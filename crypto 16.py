import re
from collections import Counter


english_letter_frequency = {
    'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02,
    'h': 6.09, 'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75,
    'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76,
    'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07
}

def calculate_letter_frequency(text):
 
    letter_count = Counter(re.sub(r'[^a-z]', '', text.lower()))
    total_letters = sum(letter_count.values())
  
    frequency = {letter: (count / total_letters) * 100 for letter, count in letter_count.items()}
    return frequency

def decrypt(ciphertext, key):
 
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            decrypted_text += key[char.lower()] if char.islower() else key[char.lower()].upper()
        else:
            decrypted_text += char
    return decrypted_text

def letter_frequency_attack(ciphertext, top_n=10):
    ciphertext_frequency = calculate_letter_frequency(ciphertext)
    
    sorted_cipher_letters = sorted(ciphertext_frequency, key=ciphertext_frequency.get, reverse=True)
    possible_plaintexts = []

    for i in range(top_n):
        
        key = {cipher_letter: english_letter for cipher_letter, english_letter in zip(sorted_cipher_letters, english_letter_frequency)}
        plaintext = decrypt(ciphertext, key)
        possible_plaintexts.append(plaintext)
       
        sorted_cipher_letters.append(sorted_cipher_letters.pop(0))

    return possible_plaintexts

def main():
    ciphertext = input("Enter the ciphertext: ")
    top_n = int(input("Enter the number of possible plaintexts to generate: "))
    possible_plaintexts = letter_frequency_attack(ciphertext, top_n)
    
    print(f"\nTop {top_n} possible plaintexts:")
    for i, plaintext in enumerate(possible_plaintexts, start=1):
        print(f"\nPlaintext {i}: {plaintext}")

if __name__ == "__main__":
    main()


