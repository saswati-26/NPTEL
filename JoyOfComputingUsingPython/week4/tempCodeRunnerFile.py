import random

def select_movie():
    movies = ["avatar", "titanic", "inception", "interstellar", "jurassic park", "forrest gump", "the godfather", "the dark knight", "the shawshank redemption", "pulp fiction"]
    return random.choice(movies)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def guess_movie(player):
    movie = select_movie()
    guessed_letters = set()
    attempts = 6
    
    print(f"\nPlayer {player}, get ready to guess the movie!")
    
    while attempts > 0:
        print("\n" + display_word(movie, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in movie:
            print("Correct!")
            guessed_letters.add(guess)
        else:
            print("Incorrect!")
            attempts -= 1
            print(f"Attempts left: {attempts}")
        
        if "_" not in display_word(movie, guessed_letters):
            print(f"\nCongratulations Player {player}! You guessed the movie '{movie}'!")
            return
        
    print(f"\nSorry, Player {player}, you ran out of attempts. The movie was '{movie}'.")
    return

def main():
    print("Welcome to the Movie Guessing Game!")
    print("Each player will take turns guessing letters to reveal the movie name.")
    print("You have 6 attempts to guess the movie. Good luck!\n")
    
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of Player 2: ")
    
    guess_movie(player1)
    guess_movie(player2)

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
