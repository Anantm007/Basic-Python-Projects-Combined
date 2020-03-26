# The original word list from where the random word is selected

word_list=["python", "javascript", "php", "django", "html", "linux", "ubuntu", "hacker", "coding", "flask"]

# Utility to update the guessword if a correct guess is made

def update(word,guessword,ch):
    
    for i in range(len(word)):
        
        if ch==word[i]:
            guessword[i]=ch
            
    
    
    return guessword      

    

# Utility to print the current status of guessword

def printword(guessword):
    
    for i in range(len(guessword)):
        print(guessword[i],end=' ')
    

# Utility to check if the player has won or not

def wincheck(guessword,word):
    
    i=0
    for i in range(len(word)):
        
        if guessword[i]!=word[i]:
            return False
        
        else:
            i+=1
            
    return True

# Function to add new words to the existing list
import getpass

def update_list():
       

    pswd = getpass.getpass("Enter the Password  -   ")     # Prints asterisk on the screen


    # If password matches
    if pswd=="abcd1234":     # By default password (We are not going to change it)
        print("\nYOU HAVE THE ACCESS!!")
    
        while True:
            word=input("Enter the word to be added to the list    -   ")
            word_list.append(word)
        
            print("\nDo you want to enter more words   (y/n)  ?   ")
            ch=input()
        
            if ch=='n' or ch=='N':
                break


    # If password does not match
    else:
        print("\nACCESS DENIED!!!")
    

# The game!!

def play(name):
    
    
    word=random.choice(word_list)    # Original word
    print("\n\nRandom word selected, we are beginning the game now")


    guesses=0        # To keep a track on number of guesses
    guessword=[]     


    # Initiating the guessword
    for _ in range(len(word)):
        guessword+="_"



    # Loop to keep a check on number of guesses
    while guesses<=10:


        printword(guessword)
        print(f"\n{name}, you have {10-guesses} chances left")

        ch=input()



        # Loop to check for correct input
        while len(ch)!=1:

            print("\nWrong Input!!")
            ch=input()



        # If the entered character is found in the hidden word        
        if ch in word:
            print("\nCONGRATS, YOU GUESSED IT RIGHT\n\n")
            guessword=update(word,guessword,ch)    # Updating the guessword


        # If the entered character is not found in the hidden word    
        else:
            print("\n\nSORRY, YOUR GUESS WAS WRONG")
            guesses+=1


        # If all the letters have been correctly guessed
        if wincheck(guessword,word) == True:
            print(guessword)
            print("\n\nBINGO, YOU WON THE GAME!!")        
            break


        # If all the chances are over
        elif guesses == 10:
            print("\n\nSORRY, ALL YOUR CHANCES ARE OVER!!! ")
            print(f"\n\nTHE HIDDEN WORD WAS   -   {word}")
            break


# Main game

import random

def game():
    
    print("WELCOME TO THE HANGMAN GAME\n\n")
    name=input("Please Enter your Name    -     ")
    
    while True:
         
    
        print("\n\nPRESS 1 IF YOU WANT TO ENTER MORE WORDS TO THE WORD LIST")
        print("\nPRESS 2 IF YOU WANT TO PLAY HANGMAN")
        n=int(input())
    
        # If user wants to alter the word list
        if n==1:
            update_list()
        
        
        # IF user wants to play the game
        elif n==2:
            play(name)
        
        else:
            print("\nWRONG CHOICE!!!")
        
    
        print("\nDO YOU WANT TO PLAY AGAIN (y/n)   ?  ")
        ch=input()
    
        if ch=='n' or ch=='N':
            break

        

game()