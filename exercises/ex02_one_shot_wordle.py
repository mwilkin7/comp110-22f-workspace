"""EX02 - One-Shot Wordle."""

__author__: str = "730397316"

output: str = ""
secret_word: str = "python"
secret_number: int = len(secret_word)
match_tracker: int = 0
word_guess: str = input(f"What is your {secret_number} letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

if word_guess == secret_word:
    while secret_number != match_tracker:
        if word_guess[match_tracker] == secret_word[match_tracker]:
            output += GREEN_BOX
        match_tracker = match_tracker + 1
    print(output)
    print("Woo! You got it!")

if word_guess != secret_word: 
    while len(word_guess) != secret_number:
        word_guess = input(f"That was not {secret_number} letters. Try again: ")
    else:
        while secret_number != match_tracker:
            if word_guess[match_tracker] == secret_word[match_tracker]:
                output += GREEN_BOX
            else:
                incorrect_position_tracker: bool = False
                alternate_indices_tracker: int = 0
                while alternate_indices_tracker != secret_number:
                    if word_guess[match_tracker] == secret_word[alternate_indices_tracker]:
                        incorrect_position_tracker = True
                    alternate_indices_tracker = alternate_indices_tracker + 1
                if incorrect_position_tracker is True:
                    output += YELLOW_BOX
                if incorrect_position_tracker is False:
                    output += WHITE_BOX
            match_tracker = match_tracker + 1
        
        print(output)
        print("Not quite. Play again soon!")