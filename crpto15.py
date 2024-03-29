import string
from collections import Counter

ALPHABET_SIZE = 26


def count_frequency(ciphertext):
    ciphertext = ciphertext.lower()
    return Counter(c for c in ciphertext if c.isalpha())

def decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a') - shift) % ALPHABET_SIZE) + ord('a'))
            decrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def sort_frequency(frequency):
    return [idx for idx, _ in sorted(enumerate(frequency), key=lambda x: x[1], reverse=True)]

def main():
    ciphertext = "Lclle wjmn ju pwj efgvif xyvvu ju pfl fyhklk cl pomkl ul wj"

    frequency = count_frequency(ciphertext)
    sorted_indices = sort_frequency(frequency.values())

    print("Top 10 Possible Plaintexts:")
    for i in range(10):
        shift = (sorted_indices[i] - (ord('e') - ord('a')) + ALPHABET_SIZE) % ALPHABET_SIZE
        plaintext = decrypt(ciphertext, shift)
        print(f"{i + 1}. {plaintext}")

if __name__ == "__main__":
    main()
