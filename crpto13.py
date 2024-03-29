import numpy as np

ALPHABET_SIZE = 26


def char_to_num(c):
    if c.isalpha():
        return ord(c.lower()) - ord('a')
    return -1


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # Inverse does not exist


def solve_key(plaintext, ciphertext):
    p1, p2, p3, p4 = plaintext
    c1, c2, c3, c4 = ciphertext

    det = determinant([[p1, p2], [p3, p4]]) % ALPHABET_SIZE
    det_inv = mod_inverse(det, ALPHABET_SIZE)
    if det_inv is None:
        print("Inverse does not exist for the given plaintext-ciphertext pairs.")
        return None

    key = np.array([
        [(det_inv * (p4 * c1 - p2 * c2)) % ALPHABET_SIZE, (det_inv * (-p1 * c2 + p2 * c1)) % ALPHABET_SIZE],
        [(det_inv * (-p3 * c1 + p1 * c3)) % ALPHABET_SIZE, (det_inv * (p3 * c2 - p1 * c4)) % ALPHABET_SIZE]
    ], dtype=int)

    return key

def main():
    plaintext = [1, 0, 3, 2]
    ciphertext = [4, 5, 3, 6] 

    key = solve_key(plaintext, ciphertext)
    if key is not None:
        print("Derived Key Matrix:")
        print(key)

if __name__ == "__main__":
    main()

