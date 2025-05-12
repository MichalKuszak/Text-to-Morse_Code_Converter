import json

with open('./morse.json', mode='r') as file:
    MORSE_DICT = json.load(file)

# Endless loop for user inputs
while True:
    string = input("Please input a string. If you want to quit, type 'q': ").lower()

# Main program functionality
    if string != 'q':    # Typing 'q' (case-insensitive) quits the program
        for char in string:
            if char in MORSE_DICT:
                string = string.replace(char, f"{MORSE_DICT[char]} ")
            else:
                print(f"Character {char} not translated into Morse Code!")
                continue
        print(string)
    else:
        print("Goodbye!")
        break
