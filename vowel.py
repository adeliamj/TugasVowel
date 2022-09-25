#vowel declaration
VOWLES = ("a", "i", "u", "e", "o")

#user input
message = input("Enter your message: ").lower().strip()

new_message = ""

#if there is a vowel in the input, it will be removed
for letter in message:
     if letter not in VOWLES:
        new_message += letter

print (new_message)
