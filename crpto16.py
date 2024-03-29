import string
import math
from collections import Counter

ALPHABET_SIZE = 26


letter_frequency = {
    'a': 0.0817, 'b': 0.0149, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270,
    'f': 0.0223, 'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015,
    'k': 0.0077, 'l': 0.0403, 'm': 0.0241, 'n': 0.0675, 'o': 0.0751,
    'p': 0.0193, 'q': 0.0009, 'r': 0.0599, 's': 0.0633, 't': 0.0906,
    'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015, 'y': 0.0197,
    'z': 0.0007
}


def count_frequency(ciphertext):
    ciphertext = ciphertext.lower()
    return Counter(c for c in ciphertext if c.isalpha())


def chi_squared(observed, expected):
    return sum(((observed[char] - expected[char] * 100) ** 2) / (expected[char] * 100) for char in string.ascii_lowercase)


def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a') - key) % ALPHABET_SIZE) + ord('a'))
            decrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            decrypted_text += char
    return decrypted_text


def sort_chi_squared(chi_squared_values):
    return sorted(range(len(chi_squared_values)), key=lambda i: chi_squared_values[i])

def main():
    ciphertext = "Lclle wjmn ju pwj efgvif xyvvu ju pfl fyhklk cl pomkl ul wj"

    frequency = count_frequency(ciphertext)
    total = sum(frequency.values())

    chi_squared_values = []
    for key in range(ALPHABET_SIZE):
        expected_frequency = {char: letter_frequency[char] * total for char in string.ascii_lowercase}
        plaintext = decrypt(ciphertext, key)
        observed_frequency = count_frequency(plaintext)
        chi_squared_values.append(chi_squared(observed_frequency, expected_frequency))

    sorted_indices = sort_chi_squared(chi_squared_values)

    print("Top 10 Possible Plaintexts:")
    for i in range(10):
        key = sorted_indices[i]
        plaintext = decrypt(ciphertext, key)
        print(f"{i + 1}. Key: {key}, Plaintext: {plaintext}")

if __name__ == "__main__":
    main()
