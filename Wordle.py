import random
import sys
from turtle import color
from Words_list import valid_words5

CHOSEN_WORD = random.choice(valid_words5)
GUESS_COUNT = 6

class Color:
    prefix = '\033'
    base ="\033[0m"
    grey = "\033]09m"
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    persistent_color = [red,green]

class GuessWord:
    counter = 1
    wordles = []
    alphabet = {
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
    }
    def __init__(self, w_str:str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ""

    def jump_turn(self):
        GuessWord.counter +=1

    def is_valid(self):
        return self.w_str in valid_words5
    
    def apply_greens(self):
        for i, _ in enumerate(self.w_chars):
            actual_char = CHOSEN_WORD[i]
            guessed_char = self.w_chars[i]
            if actual_char == guessed_char:
                colored_char = f"{Color.green}{actual_char}{Color.base}"
                self.w_chars[i] = colored_char
                self.edit_alphabet(actual_char, colored_char)

    def apply_yellows(self):
        for i, _ in enumerate(self.w_chars):
            guessed_char = self.w_chars[i]
            if guessed_char in CHOSEN_WORD:
                colored_char = f"{Color.yellow}{guessed_char}{Color.base}"
                self.w_chars[i] = colored_char
                self.edit_alphabet(guessed_char, colored_char)
            #applied red word, implying character not in the chosen word
            else:
                colored_char = f"{Color.red}{guessed_char}{Color.base}"
                self.edit_alphabet(guessed_char, colored_char)
    
    def edit_alphabet(self, guess_char, colored_char):
        if guess_char not in GuessWord.alphabet.keys():
            return
        
        older_value = GuessWord.alphabet.get(guess_char,"")
        modify_color = True
        for c in Color.persistent_color:
            if c in older_value:
                modify_color = False

        if modify_color:
            GuessWord.alphabet[guess_char] = colored_char

    def apply_guesses(self):
        self.apply_greens()
        self.apply_yellows()
        self.post_guess_w_str = "".join(self.w_chars)
        GuessWord.wordles.append(self.post_guess_w_str)
        print(self.post_guess_w_str)
    
    def check_perfect_guess(self):
        if self.w_str == CHOSEN_WORD:
            print(f"Congratulations! You beat Wordle in {GuessWord.counter} guesses")
            for element in GuessWord.wordles:
                print(element)
            sys.exit(1)

    def check_game_loss(self):
        if GuessWord.counter == GUESS_COUNT + 1:
            print(f'You lost the game. The word was {CHOSEN_WORD}')
            sys.exit(1)