# Name:  Rabsun Shrestha
# Student Number:  10494870



import urllib.request # Used to send a request to the Wordnik API over the internet.
import json # Used to convert between JSON-formatted text and Python variables.
import string # Used to provide convenient access to a string variable containing all uppercase letters.
import random
import copy


from tkinter import *  # Used to create the GUI.
import tkinter.messagebox # Used to show pop-up information windows.

# This function generates and returns a list of 9 letters.  It has been completed for you.
# See Point 1 of the "Functions in word_find.py" section of the assignment brief.
def select_letters():
    # This tuple contains 26 numbers, representing the frequency of each letter of the alphabet in Scrabble.
    letter_weights = (9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1)

    # The letter_weights tuple is used in this call to the "random.choices()" function, along with
    # the pre-defined "string.ascii_uppercase" variable which contains the letters A to Z.
    chosen_letters = random.choices(string.ascii_uppercase, weights=letter_weights, k=9)

    # We've selected a list of 9 random letters using the specified letter frequencies, and now return it.
    return chosen_letters



# This function displays the 9 letters in a 3x3 grid.
# See Point 2 of the "Functions in word_find.py" section of the assignment brief.
def display_letters(letters):
    print(' '*15+letters[0],'|',letters[1],'|',letters[2],'\n'+' '*15+'-'*9,'\n'+' '*15+letters[3],'|',letters[4],'|',letters[5],'\n'+' '*15+'-'*9,'\n'+' '*15+letters[6],'|',letters[7],'|',letters[8],'\n')
    

# This function checks whether a word entered by the user contains appropriate letters.
# See Point 3 of the "Functions in word_find.py" section of the assignment brief.
def validate_word(word, letters):
    cletters=copy.deepcopy(letters)
    for i in word:
        if (i in cletters):
            cletters.remove(i)
        else:
            return False
            break
    return True
            
            
def word_check(word):
    API_key =  'rjjy9serim1v1mefkl72qt7evgp3jtnbraddx1ufgc7mgzu2d'
    try:
        # concatenate the variables into the URL and send the request, then store the response as 'response'
        response = json.load(urllib.request.urlopen('http://api.wordnik.com/v4/word.json/' + word.lower() + '/scrabbleScore?api_key=' + API_key))
            # print the Scrabble score of the word
        word_value = response['value']
        return word_value
            
    except urllib.error.HTTPError:
            # if the word is not recognised, print this message
        return 0





score=0
letters=[]
used_words=[]
print('Welcome to Word Find!\nCome up with as many words as possible from the letters below\n')
while(True):
# prompt the user to select easy mode or hard mode.
    mode=str(input('Do you wish to play [e]asy or [h]ard mode? '))
    if mode=='e':
        print('\nEasy mode selected !!!')
        hard_mode=False
        break
    elif mode=='h':
        print('\nHard mmode selected !!!')
        hard_mode=True
        break
    else:
        print('\nInvalid input, please select mode\n')

regame=True
while(regame==True):
    letters=select_letters()
    # Enter gameplay loop (Requirement 3).
    while(True):
        print('Your Score:',str(score),'and','your letters are: \n')
        display_letters(letters)
        word=input('Enter a word, [S]uffle a letters, [L]ist words, [E]game: ').upper()
        if(word=='E'):
            break
        elif(word=='S'):
            random.shuffle(letters)
        elif(word=='L'):
            print('\nPreviously entered words:')
            used_words.sort()
            if len(used_words)<1:
                print('Your list is empty')
            else:
                for wrd in used_words:
                    print(wrd)
       # check word length
        elif(len(word)<3):
            print('\n-----Word count is less than 3-----\n')
            if(hard_mode==True):
                print('Game Over')
                break
        # check word already used or not
        elif(word in used_words):
            print('\n-----Word already exist-----\n')
            if(hard_mode==True):
                print('Game Over')
                break
        # check word is contruct with given letters or not
        elif(validate_word(word,letters)==False):
            print('\n-----Enter valid letters-----\n')
            if(hard_mode==True):
                print('Game Over')
                break
        else:
            if(word_check(word)==0):
                print('The word "' + word + '" is not recognised.')
                if(hard_mode==True):
                    print('Game Over')
                    break
            else:
                print('The word "' + word + '" is worth ' + str(word_check(word)) + ' points.')
                score=score+word_check(word)
                used_words.append(word)

            
    # Print final score and record log of game if it is above 50.
    if score>=50:
        print('Congratulations!!')
        mydic={'letters':letters,'words':used_words,'score':score}
        with open('logs.txt','r') as f:
            try:
                logs = json.load(f)
            except:
                logs=[]
        with open('logs.txt','w') as json_file:
            logs.append(mydic)
            json.dump(logs,json_file)
            json_file.close()
    print('Your final score is',str(score))        
    print('Thank you for playing!')
    # ask for re game
    re=input('\n'+'-'*5+'Do you want to restart the game ?'+'-'*5+'\nEnter "y" to play and anykey to exit: ').upper()
    if re=='Y':
        regame=True
    else:
        regame=False
    
    
      
