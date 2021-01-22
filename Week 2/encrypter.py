file = open('example.txt', 'r')
lines = file.readlines()
key = 5
encrypted = open('encrypted.txt', 'w')

for line in lines:
    new_line = ''
    for character in line:
        if (character == '\n'):
            new_line += character
        elif (character == ' '):
            new_line += ' '
        elif (character.isupper()):
            char_index = ord(character) - ord('A')
            char_shifted = (char_index + key) % 26 + ord('A')
            new_char = chr(char_shifted)
            new_line += new_char
        elif (character.islower()):
            char_index = ord(character) - ord('a')
            char_shifted = (char_index + key) % 26 + ord('a')
            new_char = chr(char_shifted)
            new_line += new_char
        else:
            char_shifted = (int(character) + key) % 10
            new_char = str(char_shifted)
            new_line += new_char
    encrypted.writelines(new_line)