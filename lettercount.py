from sys import argv

script, filename = argv

open_file = open(filename)
text = open_file.read()
open_file.close()

alphabet = [0] * 26

for char in text:
    letter = char.lower()
    if ord(letter)>=97 and ord(letter) <=122:
        alphabet[ord(letter) - 97] += 1

for count in alphabet:
    print count