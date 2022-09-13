"""EX01 - Chardle - A cute step toward Wordle."""

__author__: str = "730397316"
word_guess: str = input("Enter a 5-character word: ")
if len(word_guess) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter_guess: str = input("Enter a single character: ")
if len(letter_guess) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + letter_guess + " in " + word_guess)

index_0: str = word_guess[0]
index_1: str = word_guess[1]
index_2: str = word_guess[2]
index_3: str = word_guess[3]
index_4: str = word_guess[4]

match_number: int = 0

if letter_guess == index_0:
    match_number = match_number + 1
    print(letter_guess + " found at index 0")

if letter_guess == index_1:
    match_number = match_number + 1
    print(letter_guess + " found at index 1")

if letter_guess == index_2:
    match_number = match_number + 1
    print(letter_guess + " found at index 2")

if letter_guess == index_3:
    match_number = match_number + 1
    print(letter_guess + " found at index 3")

if letter_guess == index_4:
    match_number = match_number + 1
    print(letter_guess + " found at index 4")

if match_number == 0:
    print("No instances of " + letter_guess + " found in " + word_guess)

if match_number == 1:
    print("1 instance of " + letter_guess + " found in " + word_guess)

if match_number == 2:
    print("2 instances of " + letter_guess + " found in " + word_guess)

if match_number == 3:
    print("3 instances of " + letter_guess + " found in " + word_guess)

if match_number == 4:
    print("4 instances of " + letter_guess + " found in " + word_guess)

if match_number == 5:
    print("5 instances of " + letter_guess + " found in " + word_guess)