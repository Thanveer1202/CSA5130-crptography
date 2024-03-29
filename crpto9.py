def find_position(key_table, ch):
    if ch == 'J':
        ch = 'I'
    for row in range(5):
        for col in range(5):
            if key_table[row][col] == ch:
                return row, col

def decrypt(key_table, message):
    decrypted_message = ""
    i = 0
    while i < len(message):
        a = message[i]
        b = message[i + 1]
        row1, col1 = find_position(key_table, a)
        row2, col2 = find_position(key_table, b)

        if row1 == row2:  # Same row
            decrypted_message += key_table[row1][(col1 - 1) % 5] + key_table[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_message += key_table[(row1 - 1) % 5][col1] + key_table[(row2 - 1) % 5][col2]
        else:
            decrypted_message += key_table[row1][col2] + key_table[row2][col1]
        i += 2
    return decrypted_message

def main():
    key_table = [
        ['K', 'X', 'J', 'E', 'Y'],
        ['U', 'R', 'E', 'B', 'Z'],
        ['W', 'H', 'Y', 'T', 'U'],
        ['H', 'E', 'Y', 'F', 'S'],
        ['K', 'R', 'E', 'H', 'E']
    ]

    message = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ"

    decrypted_message = decrypt(key_table, message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
