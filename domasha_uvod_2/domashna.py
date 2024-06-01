import random

with open("domashna_uvod.txt") as file:
    word_list = file.readlines()

random_list = random.sample(word_list, 100)

random_list = [word.strip() for word in random_list]

def get_word():
    word = random.choice(random_list)
    return word.lower()

def my_play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Already guessed", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Already guessed word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("You win! The word was", word)
    else:
        print("You ran out of tries. The word was", word, "Maybe next time!")

def display_hangman(tries):
    stages = ["""
                    _______
                    |/    |
                    |    (_)
                    |    \|/
                    |     |
                    |    / \\
                    |
                    |___
                """,
                """
                    _______
                    |/    |
                    |    (_)
                    |    \|/
                    |     |
                    |    / 
                    |
                    |___
                """,
                """
                    _______
                    |/    |
                    |    (_)
                    |    \|/
                    |     |
                    |    
                    |
                    |___
                """,
                """
                    _______
                    |/    |
                    |    (_)
                    |    \|
                    |     |
                    |    
                    |
                    |___
                """,
                """
                    _______
                    |/    |
                    |    (_)
                    |     |
                    |     |
                    |    
                    |
                    |___
                """,
                """
                    _______
                    |/    |
                    |    (_)
                    |    
                    |     
                    |    
                    |
                    |___
                """,
                """
                    _______
                    |/    |
                    |    
                    |    
                    |     
                    |    
                    |
                    |___
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    my_play(word)
    while input("Play again? (Y/N) ").lower() == "y":
        word = get_word()
        my_play(word)

if __name__ == "__main__":
    main()

# Стела Маркова 8в :)