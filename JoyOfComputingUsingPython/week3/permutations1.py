'''
A jumbled word guessing game where in there are 2 players and computer gives the jumbled word and the players guess the word according to their turn and score is updated accordingly
'''

import random 

def choose():
    words = ['rainbow' , 'computer', 'science', 'programming', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled_word = "".join(random.sample(word, len(word)))
    return jumbled_word

def thank(p1n, p2n, p1,p2):
    print(f"{p1n}, your score is : {p1}")
    print(f"{p2n}, your score is : {p2}")
    print("Thank you for playing. \n Have a nice day ahead!!")

def play():
    p1_name = input("Player1, Please enter your name: ")
    p2_name = input("Player2, Please enter your name: ")
    p1_score = 0
    p2_score = 0
    turn = 0
    while (1):
        #computer's task
        picked_word = choose()
        qn = jumble(picked_word)
        print(qn)

        #player1's task
        if (turn % 2 == 0):
            print(p1_name, " ,It's your turn")
            ans = input("What's in your mind? ")
            if (ans == picked_word):
                p1_score = p1_score + 1
                print("Your current score is: ", p1_score)
            else:
                print("Better luck next time!! The word is: ",picked_word)
            c = int(input("Enter 1 to continue and 0 to quit : "))
            if (c == 0):
                thank(p1_name, p2_name, p1_score, p2_score)
                break

        #player2's task
        else:
            print(p2_name, " ,It's your turn")
            ans = input("What's in your mind? ")
            if (ans == picked_word):
                p2_score = p2_score + 1
                print("Your current score is: ", p2_score)
            else:
                print("Better luck next time!! The word is: ",picked_word)
            c = int(input("Enter 1 to continue and 0 to quit : "))
            if (c == 0):
                thank(p1_name, p2_name, p1_score, p2_score)
                break   
        turn = turn + 1  
play()