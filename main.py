MORSE_DICT = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

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
