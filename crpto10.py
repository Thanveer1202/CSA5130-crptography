def prepare_plain_text(input_text):
    input_text = input_text.upper().replace("J", "I")  
    input_text = ''.join(filter(str.isalpha, input_text))
    input_text += 'X' * (len(input_text) % 2)
    return input_text


def find_position(key_table, ch):
    for row in range(5):
        for col in range(5):
            if key_table[row][col] == ch:
                return row, col


def encrypt(key_table, input_text):
    encrypted_text = ""
    i = 0
    while i < len(input_text):
        a = input_text[i]
        b = input_text[i + 1]
        row1, col1 = find_position(key_table, a)
        row2, col2 = find_position(key_table, b)

        if row1 == row2:  # Same row
            encrypted_text += key_table[row1][(col1 + 1) % 5] + key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += key_table[(row1 + 1) % 5][col1] + key_table[(row2 + 1) % 5][col2]
        else:
            encrypted_text += key_table[row1][col2] + key_table[row2][col1]
        i += 2
    return encrypted_text

def main():
    key_table = [
        ['M', 'F', 'H', 'I', 'K'],
        ['U', 'N', 'O', 'P', 'Q'],
        ['Z', 'V', 'W', 'X', 'Y'],
        ['E', 'L', 'A', 'R', 'G'],
        ['D', 'S', 'T', 'B', 'C']
    ]

    message = "Must see you over Cadogan West. Coming at once."
    prepared_text = prepare_plain_text(message)

    encrypted_message = encrypt(key_table, prepared_text)
    print("Encrypted message:", encrypted_message)

if __name__ == "__main__":
    main()
