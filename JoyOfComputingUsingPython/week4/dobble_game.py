import string
import random

def generate_cards():
    alphabets_list = list(string.ascii_letters)
    card1 = [0] * 5
    card2 = [0] * 5
    commom_alphabet = random.choice(alphabets_list)
    alphabets_list.remove(commom_alphabet)
    pos1 = random.randint(0, 4)
    pos2 = random.randint(0, 4)
    while pos2 == pos1:
        pos2 = random.randint(0, 4)
    card1[pos1] = commom_alphabet
    card2[pos2] = commom_alphabet
    
    for pos in range(5):
        if pos != pos1:
            card1[pos] = random.choice(alphabets_list)
            alphabets_list.remove(card1[pos])
        if pos != pos2:
            card2[pos] = random.choice(alphabets_list)
            alphabets_list.remove(card2[pos])
    
    print(card1, "\n", card2)

    ch = input("Identify the similar alphabets in both the lists: ")
    dobble_game(ch, commom_alphabet)

def dobble_game(ch, commom_alphabet):
    if ch == commom_alphabet:
        print("Hurray! You got it")
    else:
        print("Sorry! Better luck next time")

generate_cards()