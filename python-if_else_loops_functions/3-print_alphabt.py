#!/usr/bin/python3
result = ''
for ascii_code in range(97, 123):
    letter = chr(ascii_code)
    if letter not in ('q', 'e'):
        result += letter
print("{}".format(result), end="")
