#Importing the Morse code Letters
from letter_morse import ENGLISH_TO_MORSE

#Looping through the letters
MC_TO_ENGLISH = {}
for key, value in ENGLISH_TO_MORSE.items():
    MC_TO_ENGLISH[value] = key
#Function for converting Eng to Morse
def english_to_mc(message):
    morse = []
    for char in message:
        if char in ENGLISH_TO_MORSE:
            morse.append(ENGLISH_TO_MORSE[char])
    return"".join(morse)
#function for converting Morse to Eng
def mc_to_english(message):
    message = message.split(" ")
    english = []
    for code in message:
        if code in MC_TO_ENGLISH:
            english.append(MC_TO_ENGLISH[code])
    return " ".join(english)

#The Input
def main():
    while True:
        response = input("Convert Morse to English(1) or English to Morse(2)?").upper()
        if response == "1" or response =="2":
            break


    if response == "1":
        print("Enter Morse code (with a space after each code): ")
        morse = input("> ")
        english = mc_to_english(morse)
        print("### English version ###")
        print(english)

    elif response == "2":
        print("Enter english text: ")
        english = input("> ").upper()
        morse = english_to_mc(english)
        print("###Morse code Version###")
        print(morse)

if __name__== "__main__":
    main()
