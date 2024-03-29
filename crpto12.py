import numpy as np

ALPHABET_SIZE = 26

def char_to_num(c):
    if c.isalpha():
        return ord(c.lower()) - ord('a')
    return -1  


def num_to_char(num):
    return chr(num + ord('a'))


def encrypt(message, key):
    encrypted = []
    for i in range(0, len(message), 2):
        a = char_to_num(message[i])
        b = char_to_num(message[i + 1])

        ciphertext = np.dot(key, np.array([a, b])) % ALPHABET_SIZE
        encrypted.extend(ciphertext)

 
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1 


def decrypt(ciphertext, key):
    determinant = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    inverse = mod_inverse(determinant % ALPHABET_SIZE, ALPHABET_SIZE)
    if inverse == -1:
        print("Inverse does not exist for the given key.")
        return

    inverse_key = np.array([[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]])
    inverse_key = (inverse_key * inverse) % ALPHABET_SIZE

    decrypted = []
    for i in range(0, len(ciphertext), 2):
        a, b = np.dot(inverse_key, np.array([ciphertext[i], ciphertext[i + 1]])) % ALPHABET_SIZE
        decrypted.append(a)
        decrypted.append(b)

    return ''.join(num_to_char(num) for num in decrypted)

def main():
    key = np.array([[9, 4], [5, 7]])
    message = "meetmeattheusualplaceattenratherthaneightoclock"

    print("Original Message:", message)
    encrypted_message = encrypt(message, key)
    print("Encrypted Message:", encrypted_message)

    ciphertext = [2, 11, 13, 20, 0, 19, 7, 4, 13, 4, 0, 18, 7, 14, 8, 4, 11, 19, 8, 19, 0, 13, 18, 8, 19, 4, 6, 4, 17, 3, 6, 19, 8, 18, 7, 13, 4, 6, 7, 13, 4, 11, 6, 7, 4, 2]
    decrypted_message = decrypt(ciphertext, key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
