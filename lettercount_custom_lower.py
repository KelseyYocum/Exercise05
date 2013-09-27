from sys import argv

script, filename = argv

def custom_lower_char(char):
    if ord(char) >= 65 and ord(char) <= 90:
        return chr(ord(char) + 32)
    return char

def custom_lower_string(string):
    new_string = ""
    for char in string:
        char = custom_lower_char(char)
        new_string += char
    return new_string

open_file = open(filename)
text = open_file.read()
open_file.close()

alphabet = [0] * 26

for char in text:
    letter = custom_lower_char(char)
    if ord(letter)>=97 and ord(letter) <=122:
        alphabet[ord(letter) - 97] += 1

for count in alphabet:
    print count


