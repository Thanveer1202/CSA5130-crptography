def generate_playfair_matrix(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    remaining_letters = ''.join(letter for letter in "abcdefghiklmnopqrstuvwxyz" if letter not in keyword)
    matrix = [keyword + remaining_letters[i:i+5] for i in range(0, len(remaining_letters), 5)]
    return matrix

def find_position(matrix, letter):
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)
    return None, None

def playfair_encrypt(message, keyword):
    message = message.replace(" ", "").upper()
    matrix = generate_playfair_matrix(keyword)
    encrypted_message = ""

    for i in range(0, len(message), 2):
        letter1, letter2 = message[i], message[i + 1] if i + 1 < len(message) else 'X'
        (row1, col1), (row2, col2) = find_position(matrix, letter1), find_position(matrix, letter2)

        if None in (row1, col1, row2, col2):
            encrypted_message += letter1 + letter2
        elif row1 == row2:
            encrypted_message += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_message += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_message += matrix[row1][col2] + matrix[row2][col1]

    return encrypted_message

def main():
    message = input("Enter the plaintext message: ")
    keyword = input("Enter the keyword: ")
    print("Encrypted message:", playfair_encrypt(message, keyword))

if __name__ == "__main__":
    main()
