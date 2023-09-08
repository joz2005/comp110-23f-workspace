"""EX01 - Chardle - A cute step twoard Wordle."""

__author__ = "730655251"

user, count = str(input("Enter a 5-character word: ")), 0
if len(user) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter = str(input("Enter a single character: "))
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print(f"Searching for {letter} in {user}")

if user[0] == letter:
    print(f"{letter} found at index 0")
    count += 1
if user[1] == letter:
    print(f"{letter} found at index 1")
    count += 1
if user[2] == letter:
    print(f"{letter} found at index 2")
    count += 1
if user[3] == letter:
    print(f"{letter} found at index 3")
    count += 1
if user[4] == letter:
    print(f"{letter} found at index 4")
    count += 1
if count > 1:
    print(f"{count} instances of {letter} found in {user}")
elif count == 1:
    print(f"1 instance of {letter} found in {user}")
else:
    print(f"No insances of {letter} found in {user}")


