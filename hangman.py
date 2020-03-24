import math;
import helper;
import subprocess as sp

# Clearing the terminal
sp.call('cls',shell=True)

word = helper.getRandomWord();
# print (word);

helper.__init__()

# Return a single random word
#word = 'tie';



word_length = len(word);
allowed_mistakes = math.floor(len(word)/2);


print (f'\nLenght of the word is {word_length}')
print (f'\nAllowed mistakes are: {allowed_mistakes}')
print (f'\nGo!\n\n')


'''
For Displaying the word
'''
guessed_word = '';

print('State: ', end=' ')

for i in word:
    print('_',end=' ')
    guessed_word += '_'

#print ('Guessed Word:',guessed_word)

mistake = 0;
number_of_tries = 0;

while (mistake < allowed_mistakes+1) and ((word_length+mistake) > number_of_tries ) :

    number_of_tries += 1

    guess = input('\n\nInput your guess: ');

    word_index:int = -1

    try:
        word_index = word.index(guess)
    except:
        mistake += 1
        print("\nGuessed word is wrong mistakes remained: ",(allowed_mistakes-mistake))

    if word_index > -1:
        guessed_word = helper.replacer(guessed_word, word[word_index], word_index)
        word = helper.replacer(word, '*', word_index)

    print('State: ', end=' ')

    for i in guessed_word:
        print(i,end=' ')

#print ('\n',number_of_tries , mistake, allowed_mistakes,word_length)

if mistake <= allowed_mistakes and ((number_of_tries - mistake) >= word_length):
    print ('\n\n.:: Damn Son, you won ::.')
else:
    print ('\n\nYou lose sucka... Wanna lose again!')




