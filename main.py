import json

with open('./morse.json', mode='r') as file:
    MORSE_DICT = json.load(file)

while True:
    string = input("Please input a string. If you want to quit, type 'q': ").lower()

    if string != 'q':
        for char in string:
            if char in MORSE_DICT:
                string = string.replace(char, f"{MORSE_DICT[char]} ")
            else:
                continue
        print(string)
    else:
        print("Goodbye!")
        break
