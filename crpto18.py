expansion_table = [32, 1, 2, 3, 4, 5, 4, 5,
                   6, 7, 8, 9, 8, 9, 10, 11,
                   12, 13, 12, 13, 14, 15, 16, 17,
                   16, 17, 18, 19, 20, 21, 20, 21,
                   22, 23, 24, 25, 24, 25, 26, 27,
                   28, 29, 28, 29, 30, 31, 32, 1]


compression_permutation = [14, 17, 11, 24, 1, 5, 3, 28,
                           15, 6, 21, 10, 23, 19, 12, 4,
                           26, 8, 16, 7, 27, 20, 13, 2,
                           41, 52, 31, 37, 47, 55, 30, 40,
                           51, 45, 33, 48, 44, 49, 39, 56,
                           34, 53, 46, 42, 50, 36, 29, 32]

def permute(initial_key, permutation_table):
    return ''.join(initial_key[i - 1] for i in permutation_table)

def generate_subkeys(initial_key):
    key_permuted = permute(initial_key, compression_permutation)
    c0 = key_permuted[:28]
    d0 = key_permuted[28:]

    subkeys = []
    for i in range(16):
        c_shifted = c0[i+1:] + c0[:i+1]
        d_shifted = d0[i+1:] + d0[:i+1]
        cd_concatenated = c_shifted + d_shifted
        subkey = permute(cd_concatenated, compression_permutation)
        subkeys.append(subkey)

    return subkeys

def initial_permutation(input_text):
    return permute(input_text, initial_permutation)

def expansion(input_text):
    return permute(input_text, expansion_table)


initial_key = "0001001100110100010101110111100110011011101111001101111111110001"
subkeys = generate_subkeys(initial_key)
print("Subkeys:")
for i, subkey in enumerate(subkeys):
    print(f"K{i + 1}: {subkey}")


