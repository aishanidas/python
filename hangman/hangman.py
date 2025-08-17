# -------------------------------------------
# Hangman game
# Created by: Aishani Das
# -------------------------------------------

import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee'''

someWords = someWords.split(' ')
word = random.choice(someWords)

letterGuessed = ''
correct = 0
flag = 0
wrong = 0

stages = ["",
          "________        ",
          "|        |      ",
          "|        0      ",
          "|       /|\\    ",
          "|       / \\    ",
          ]


def draw_hangman(wrong_tries):
        print("\n".join(stages[0:wrong_tries]))

if __name__ == '__main__':
        chances = len(stages)-1

        board = ["__"] * len(word)
        print ("Guess the word!")
        for i in word:
                print('_', end=' ')
        print("\n")
  
        while (chances != 0) and flag == 0:
                print("\n")
                guess = str(input('Enter a letter to guess: '))
                if guess == word:
                        flag == 1
                        print('Congratulations, You won!')
                        break
                        break
        
                if not guess.isalpha():
                        print('Enter only a LETTER')
                        continue
                elif guess in letterGuessed:
                        print('You have already guessed that letter')
                        continue
        
                if guess in word:
                        k = word.count(guess)
                        for _ in range(k):
                                letterGuessed += guess
        
                if guess not in word:
                        chances -= 1
                        wrong += 1
                        print((" ".join(board)))
                        e = wrong+1
                        draw_hangman(e)

                for char in word:
                        if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                                print(char, end=' ')
                                correct += 1
                        elif (Counter(letterGuessed) == Counter(word)):
                                print("The word is: ", end=' ')
                                print(word)
                                flag = 1
                                print('Congratulations, You won!')
                                break 
                                break
                
                        else:
                                print('_', end=' ')

                if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                        print()
                        print('You lost! Try again..')
                        print('The word was {}'.format(word))


