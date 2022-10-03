import Wordle
import Wordle6
import os

os.system("cls") if os.name == "nt" else os.system("clear")

print("WELCOME TO WORDLE!")
print("Choose game mode:\n1 for 5-letter words\n2 for 6-letter word")

def gamestart():
    game_mode = int(input())
    if game_mode == 1:
        print("Press h each turn to see the alphabet remaining!")
        if __name__ == '__main__':
            with open("cheat.txt","w") as f:
                f.write(Wordle.CHOSEN_WORD)
            while True:
                guess = Wordle.GuessWord(
                    w_str = input(f"[{Wordle.GuessWord.counter}]>")
                )
                if guess.w_str == "h":
                    list_values = list(Wordle.GuessWord.alphabet.values())
                    for element in list_values:
                        print(element, end=" " if list_values[-1] != element else "\n" )
                    continue
                if guess.is_valid():
                    guess.apply_guesses()
                    guess.check_perfect_guess()
                    guess.jump_turn()
                    guess.check_game_loss()
    elif game_mode == 2:
        print("Press h each turn to see the alphabet remaining!")
        if __name__ == '__main__':
            with open("cheat.txt","w") as f:
                f.write(Wordle6.CHOSEN_WORD)
            while True:
                guess = Wordle6.GuessWord(
                    w_str = input(f"[{Wordle6.GuessWord.counter}]>")
                )
                if guess.w_str == "h":
                    list_values = list(Wordle6.GuessWord.alphabet.values())
                    for element in list_values:
                        print(element, end=" " if list_values[-1] != element else "\n" )
                    continue
                if guess.is_valid():
                    guess.apply_guesses()
                    guess.check_perfect_guess()
                    guess.jump_turn()
                    guess.check_game_loss()
    else:
        print("Please input a valid number!")
        gamestart()
gamestart()