"""EX03 - Structured Wordle."""

__author__: str = "730397316"


def contains_char (term: str, single_character: str) -> bool:
    """This function will determine whether the 2nd string (a single character) is found in the 1st string"""
    assert len(single_character) == 1
    match_check: int = 0
    term_length: int = len(term)
    char_index_tracker: int = 0

    while term_length != char_index_tracker:
        if term[char_index_tracker] == single_character:
            match_check = match_check + 1
        char_index_tracker = char_index_tracker + 1

    if match_check == 0:
        return False
    if match_check > 0:
        return True


def emojified (secret_word: str, guess: str) -> str:
    """Given 2 equal length strings (guess and secret_word), this function will return a string of emojis whose color will indicate the matching of indexes"""
    assert len(secret_word) == len(guess)
    guess_index_tracker: int =  0
    output: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while len(secret_word) != guess_index_tracker:
        if secret_word[guess_index_tracker] == guess[guess_index_tracker]:
            output += GREEN_BOX
        else:
            if contains_char(secret_word, guess[guess_index_tracker]):
                output += YELLOW_BOX
            else:
                output += WHITE_BOX
        guess_index_tracker = guess_index_tracker + 1
    return output


def input_guess (expected_length_integer: int) -> str:
    guess = input(f"Enter a {expected_length_integer} character word: ")
    while len(guess) != expected_length_integer:
        guess = input(f"That wasn't {expected_length_integer} chars. Try again: ")
    if len(guess) == expected_length_integer:
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    max_turns: int = 6
    expected_length_integer: int = 5
    secret_word: str = "codes"
    while turn_number <= max_turns:
        print(f"=== Turn { turn_number}/{max_turns } ===")
        guess: str = input_guess(expected_length_integer)
        if guess == secret_word:
            print(emojified(secret_word, guess))
            print(f"You won in{ turn_number }turns")
        if guess != secret_word:
            print(emojified(secret_word, guess))
        turn_number = turn_number + 1
    print(f"X/{max_turns} - Sorry, try again tomorrow!")