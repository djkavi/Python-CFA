#!/usr/bin/env python

import random

def main():
    """Start a music guessing game."""
    print("Guess the music!")

    music = [
        "baa baa black sheep",
        "baby shark",
        "daddy finger",
        "johny johny yes papa",
        "oh mack donal",
        "twinkel twinkel",
        "rain rain go away"
        ] 

    x = random.choice(music)
    
    guess = None

    while x != guess:

        guess = str(input("What the baby song am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()