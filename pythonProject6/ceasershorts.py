alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
continue_coder = True
while continue_coder:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26


    def ceaser(plain_text, shifter, work):
        message = ""
        if work == "decode":
            shifter *= -1
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shifter
                new_letter = alphabet[new_position]
            else:
                new_letter = letter

            message += new_letter

        print(f"The encrypted word is {message}.")

    ceaser(text,shift,direction)
    restart = input("Would you like to start again?\n type yes or no\n").lower()
    if restart == "no":
        continue_coder = False
        print("nothing else?")
