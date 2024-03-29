def modular_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def decrypt_affine_cipher(ciphertext, most_freq, second_most_freq):
    freq_diff = most_freq - ord('E')  
    second_freq_diff = second_most_freq - ord('T')  

    a = modular_inverse(freq_diff, 26)
    if a == -1:
        print("Cannot find modular inverse for decryption.")
        return None

    decrypted_b = (a * second_freq_diff) % 26

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(((a * (ord(char) - base - decrypted_b + 26)) % 26) + base)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def main():
    ciphertext = "BUABUABBABUBBUABABBABBABBBUBU"

    
    freq = [0] * 26
    for char in ciphertext:
        if char.isalpha():
            freq[ord(char.upper()) - ord('A')] += 1

    
    most_freq = freq.index(max(freq)) + ord('A')
    freq[most_freq - ord('A')] = 0  
    second_most_freq = freq.index(max(freq)) + ord('A')

    plaintext = decrypt_affine_cipher(ciphertext, most_freq, second_most_freq)
    if plaintext:
        print("Decrypted plaintext:", plaintext)

if __name__ == "__main__":
    main()
