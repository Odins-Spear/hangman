#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:02:07 2021

@author: wittsy

Program to play hangman meeting the specification for the JHUB coding scheme.

Program must

1. Run in python3
2. Only stop for a guess or on the win/loss
3. must ask for the guess with "Please enter your next guess: "
4. The word must be 'starred' out exactly and the stars revealed on corect guesses
5. The program must say either "Congratulations you win" or "you lose"
6. The game must use a word from the "word_list.txt" file picked at random
7. Word list is saved in the same directory
8. User has 7 guesses

"""
import random
import string


def generate_new_word():

    d = {}
    
    file = open('word_list.txt')
    
    for index, word in enumerate(file):
        d.update({index : word.rstrip('\n)')})
    
    file.close()
    
    word_index = random.randint(0, (len(d)-1))
    
    return d[word_index]


def get_valid_user_input():

    guess = input('Please enter your next guess: ')
    alphabet = list(string.ascii_lowercase)

    while guess.lower() not in alphabet:
        print('Your guess is not a letter of the alphabet. Please try again.')
        guess = input('Please enter your next guess: ')
    return guess.lower()

def mask_word(word):

    length = 0

    for letter in word:
        length += 1

    return ('*' * length)

def check_for_win(letter_list):

    if '*' in letter_list:
        return False
    else:
        return True

def display_remaining_lives(lives):

    print(f'You have {lives} lives remaining.\n')

def display_word(letter_list):
    word = ''
    word = word.join(letter_list)
    print(word)
    
def replay():

    replay_condition = input('Would you like to play again? (y/n) ')

    if replay_condition.lower() == 'y':
        return True
    else:
        return False


while True:

    game_word = generate_new_word()

    working_word = list(mask_word(game_word))

    lives = 7

    playing = True

    while playing:
        
        display_word(working_word)

        choice = get_valid_user_input()

        if choice in list(game_word):

            for index, letter in enumerate(list(game_word)):
                if working_word[index] == '*':
                    if letter == choice:
                        working_word[index] = choice
                    else:
                        working_word[index] = '*'
        else:
            lives -= 1
            display_remaining_lives(lives)
            if lives == 0:
                print('You Lose')
                playing = False

        if check_for_win(working_word):
            print('Contratulations, you win')
            playing = False


    if not replay():
        break
