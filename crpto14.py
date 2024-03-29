import string

ALPHABET_SIZE = 26


def char_to_num(c):
    if c.isalpha():
        return ord(c.lower()) - ord('a')
    return -1


def num_to_char(num):
    return chr(num + ord('a'))


def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = key[key_index % len(key)]
            encrypted_char = (char_to_num(char) + shift) % ALPHABET_SIZE
            ciphertext += num_to_char(encrypted_char)
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def main():
    plaintext = "meetmeattheusualplaceattenratherthaneightoclock"
    key = [3, 19, 5]  

    ciphertext = vigenere_encrypt(plaintext, key)

    print("Plaintext:", plaintext)
    print("Key:", key)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
