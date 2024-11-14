import random

def get_word():
    with open('Student Files/flow-control/data/words.txt') as f:
        words = f.read().splitlines()


    """Returns random word."""
    # words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
    #          'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def check(word, guesses):
    """Creates and returns string representation of word
    displaying asterisks for letters not yet guessed."""
    status = '' # Current status of guess
    last_guess = guesses[-1]
    matches = 0 # Number of occurrences of last_guess in word

# for every letter in the word and ALL guessed words: the status will be updated
# with the letter. When this condition == False (letter not in word and all guessed words),
# status will be updated with * character. When letter equals the last guess: match gets +1
# and var guessed_letter gets char from letter.
    for letter in word: 
        if letter in guesses:
            if letter == last_guess:
                guessed_letter = letter
                matches +=1

            status +=letter
            # print('You have matched {} letter(s) from the {}-letter word.'.format(matches, len(word)))
        else:
            status+= '*'

# for every letter matched:
    if matches == 1:
        print('The letter {} matched one time.'.format(guessed_letter))

    if matches > 1:
        print('The letter {} matched {} times.'.format(guessed_letter, matches))
    
    if not matches:
        print('Sorry, the word has no {}s.'.format(guesses[-1]))


        

    return status

    # Loop through word checking if each letter is in guesses
    #  If it is, append the letter to status
    #  If it is not, append an asterisk (*) to status
    # Also, each time a letter in word matches the last guess,
    #  increment matches by 1.

    # Write a condition that outputs one of the following when
    #  the user's last guess was "A":
    #   'The word has 2 "A"s.' (where 2 is the number of matches)
    #   'The word has one "A".'
    #   'Sorry. The word has no "A"s.'

    

def main():
    word = get_word() # The random word
    n = len(word) # The number of letters in the random word
    guesses = [] # The list of guesses made so far
    guessed = False
    print('The word contains {} letters.'.format(n))

    while not guessed:
        guess = input('Guess a letter or a {}-letter word: '.format(n))
        guess = guess.upper()

# when the length of quess equals the length of the word, the quess will be added 
# to the guesses list. When the guessed length and char's matches the word: guessed 
# is true and while loop ends. Word was guessed right!
        if len(guess) == n:
            if guess == word:
                guesses.append(guess)
                guessed = True
                break
            guesses.append(guess)
            print('wrong word but {} length word is right.'.format(n))

        guesses.append(guess)
        status = check(word, guesses)

        if status == word:
            guessed = True
        
        print(status,'\n')


        # Write an if condition to complete this loop.
        # You must set guessed to True if the word is guessed.
        # Things to be looking for:
        #  - Did the user already guess this guess?
        #  - Is the user guessing the whole word?
        #     - If so, is it correct?
        #  - Is the user guessing a single letter?
        #     - If so, you'll need your check() function.
        #  - Is the user's guess invalid (the wrong length)?
        #
        # Also, don't forget to keep track of the valid guesses.

    print('{} is it! It took {} tries.'.format(word, len(guesses)))

main()