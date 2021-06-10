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
'''
This function opens a text file and reads the contents into an iterable dictionary with an indexed key word,
simulatanouesly removing paragraph markers and formatting to prevent errors with the expected use of the returned
word. A random number fuction then generates a key for the selection of a word from the dictinary, which is returned.

Input: none, however it is assumed the text file is in the same directory as the exeuting file
Returns: a string object of a word selected at random
'''
    
    d = {}
    
    file = open('word_list.txt')
    
    for index, word in enumerate(file):
        d.update({index : word.rstrip('\n)')})
    
    file.close()
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:28:13 2021

@author: wittsy
"""

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
    '''
    This function opens a text file and reads the contents into an iterable dictionary with an indexed key word,
    simulatanouesly removing paragraph markers and formatting to prevent errors with the expected use of the returned
    word. A random number fuction then generates a key for the selection of a word from the dictinary, which is returned.
    Input: none, however it is assumed the text file is in the same directory as the exeuting file
    Returns: a string object of a word selected at random
    '''

    d = {}
    
    file = open('word_list.txt')
    
    for index, word in enumerate(file):
        d.update({index : word.rstrip('\n)')})
    
    file.close()
    
    word_index = random.randint(0, (len(d)-1))    #generation of a random number between zero (inclusive) and the size of the ditionary (adjusted for zero index)
    
    return d[word_index] # returns a string object


def get_valid_user_input():
    
    '''
    This function handles the user interaction, requesting that a user inputs a guess for the word in play.
    This guess is checked to be a letter of the alphabet and if so is returned as a lower case version of the
    letter to ensure that the return is consistently lower case. if not the function loops until a
    valid guess is inputted by the user.
    Input : none
    Returns : a lower case string object of a letter representing the guess of the user 
    '''

    
    guess = input('Please enter your next guess: ') # User guess input
    alphabet = list(string.ascii_lowercase) # cast a list object containing all 26 letters of the alphabet as lower case letters

    while guess.lower() not in alphabet: #check that the guess is a letter
        print('Your guess is not a letter of the alphabet. Please try again.') #if not ask for a valid guess.
        guess = input('Please enter your next guess: ')
    return guess.lower()

def mask_word(word):
    '''
    This fuction receives a string obeject and returns a string of '*'s the length of the recieved word. Essentially creating a mask for the word in play
    Input : string object
    Returns : string object of '*'s the length of the received word.
    '''

    length = 0

    for letter in word:
        length += 1

    return ('*' * length)

def check_for_win(letter_list):
    '''
    This function checks for the win condition, inducing a win from a lack of "*"s in the received word, which is a list object.
    input : a list object of string objects 
    returns : a boolean True on detecting a win and False if a win condition is not detected. 
    '''
    if '*' in letter_list:
        return False
    else:
        return True

def display_remaining_lives(lives):
    '''
    Simple function to print the number of lives remaining for the user. Uses a global variable 'lives' which is an integer. 
    imput: integer
    returns : Nil
    '''

    print(f'You have {lives} lives remaining.\n')

def display_word(letter_list):
    '''    
    this function displays a string object that is a concatenation of the working letters, whether they are revealed or still '*'
    imput : list object of string objects
    returns : nil
    '''
    word = ''
    word = word.join(letter_list)
    print(word)
    
def replay():
    '''
    This function handles the 'play again' condition. The user input generates a boolean True should another game be required and a boolean False if not
    input : generated in function
    returns : boolean 
    '''

    replay_condition = input('Would you like to play again? (y/n) ')

    if replay_condition.lower() == 'y':
        return True
    else:
        return False

#Game Script

while True:

    game_word = generate_new_word() #generate a word to play the game with as a reference

    working_word = list(mask_word(game_word)) # generaate a 'working' word that is used in playing the game.

    lives = 7 #number of lives is started as the int value 7

    playing = True # sets the game in play

    while playing:
        
        display_word(working_word) #display the working word

        choice = get_valid_user_input() #get a user guess that is valid for the game


        if choice in list(game_word): 
        #index through the working word and if the letter is in the game word change the working word to show a correct guess, if not then leave it as a '*'
            for index, letter in enumerate(list(game_word)):
                if working_word[index] == '*':
                    if letter == choice:
                        working_word[index] = choice
                    else:
                        working_word[index] = '*'
        else:
            lives -= 1
            display_remaining_lives(lives)
            if lives == 0:                   #no lives left causes game end by making 'playing' False
                print('You Lose')
                playing = False

        if check_for_win(working_word):       #check for the win condition and end the game if a win is detected.
            print('Contratulations, you win')
            playing = False


    if not replay():     # check for wether the user wants to play again. break and end the routine if not. 
        break
