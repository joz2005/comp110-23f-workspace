__author__ = "730655251"

secret_word = "python"
user = str(input(f"What is your {len(secret_word)}-letter guess?"))

while len(user) != len(secret_word):
    user = str(input(f"That was not {len(secret_word)} letters! Try again:"))

index = 0
box_string = ""

while index < len(user):

    letter_found = False
    alt_index = 0

    if user[index] == secret_word[index]:
        box_string += "\U0001F7E9"

    else:
        while not letter_found and alt_index < len(secret_word):
            if user[index] == secret_word[alt_index]:
                letter_found = True
            alt_index += 1
        if letter_found:
            box_string += "\U0001F7E8"
        else:
            box_string += "\U00002B1C"
            
    index += 1

print(box_string)

if user.lower() == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")