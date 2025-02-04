import random
import os

with open("words.txt", "r") as wordlist:
    words = [i.strip("\n") for i in wordlist.readlines()]

chosen_word = random.choice(words)
censored = ["_" for _ in chosen_word]
tries = 6
used_letters = set()

hangman_stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def uncensor(letter, censor, word):
    for i in range(len(word)):
        if word[i] == letter:
            censor[i] = letter
    return censor

def main():
    global censored, tries, used_letters
    print("Welcome to Hangman!")
    while tries > 0:
        os.system("clear" if os.name == "posix" else "cls")
        print(hangman_stages[6 - tries])
        print("Used letters:", " ".join(sorted(used_letters)))
        print(" ".join(censored))
        letter = input("Guess a letter: ").lower()
        if letter in used_letters:
            continue
        used_letters.add(letter)
        if letter in chosen_word:
            censored = uncensor(letter, censored, chosen_word)
        else:
            tries -= 1
        if "_" not in censored:
            os.system("clear" if os.name == "posix" else "cls")
            print("You win!")
            print("The word was:", chosen_word)
            break
    if tries == 0:
        os.system("clear" if os.name == "posix" else "cls")
        print(hangman_stages[6])
        print("You lose! The word was:", chosen_word)

if __name__ == "__main__":
    main()