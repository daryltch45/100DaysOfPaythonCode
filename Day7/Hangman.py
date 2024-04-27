import Hangman_art
import Hangman_words
import random

print(Hangman_art.logo)

word = random.choice(Hangman_words.word_list)
stage = -1
displayed_word = '_'*len(word)

def guess(char, word, displayed_word, stage):

    intermediate_word = displayed_word
    for i in range(len(word)):
        if word[i] == char:
            intermediate_word = intermediate_word[:i] + char + intermediate_word[i + 1:]

    if intermediate_word == displayed_word:
        if char in word:
            print('You already guessed that letter')
        else:
            print(f'You guessed {char}, that\'s not in the word. You lose a life.')
        stage -= 1
        print(Hangman_art.stages[stage])
    else:
        print(intermediate_word)
        print(Hangman_art.stages[stage])

    return intermediate_word, stage



print(word)
while stage > -len(word):
    char = input('Guess a letter: ')
    displayed_word, stage = guess(char, word, displayed_word, stage)
    if displayed_word == word:
        print('You win!')
        break

