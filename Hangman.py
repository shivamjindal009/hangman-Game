from words import get_word
from string import ascii_lowercase


def get_num_attempt():
    while True:
        incorrect_attempts = input('How many incorrect attempts you want? [1-25] : ')
        try:
            incorrect_attempts = int(incorrect_attempts)
            if 1 <= incorrect_attempts <= 25:
                return incorrect_attempts
            else:
                print('{} is not in between 1 and 25'.format(incorrect_attempts))
        except ValueError:
            print('{} is not an integer between 1 to 25'.format(incorrect_attempts))


def get_min_word_length():
    while True:
        word_length = input('what minimum word length you want? [4-13] : ')
        try:
            word_length = int(word_length)
            if 4 <= word_length <= 13:
                return word_length
            else:
                print('{} is not in between 4 and 13'.format(word_length))
        except ValueError:
            print('{} is not an integer between 4 to 13'.format(word_length))


def display_word(curr_word, idxs):
    display = ''.join([letter if idxs[i] else '*' for i, letter in enumerate(curr_word)])
    return display


def get_next_letter(letters):
    """ Get the user inputted next letter """
    if len(letters) == 0:
        raise ValueError('There are no more letters to guess')
    while True:
        next_letter = input('choose the next letter : ').lower()
        if len(next_letter) != 1:
            print('{} is not a single letter'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{} not a letter'.format(next_letter))
        elif next_letter not in letters:
            print('{} letter you guessed before'.format(next_letter))
        else:
            letters.remove(next_letter)
        return next_letter


def play_hangman():
    print('Starting a game of Hangman...')
    false_attempts = get_num_attempt()
    minWordLength = get_min_word_length()

    # Randomly selecting a word
    print('Selecting a word...')
    word = get_word(minWordLength)
    print()

    # setting the game state parameter
    idxs = [letters not in ascii_lowercase for letters in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_resolved = False

    # Main Game loop
    while false_attempts > 0 and not word_resolved:
        """ Printing the current Game state"""
        print('word : {}'.format(display_word(word, idxs)))
        print('remaining attempts : {}'.format(false_attempts))
        print('previous Guesses : {0}'.format(' '.join(wrong_letters)))

        # get Player next guess
        next_letter = get_next_letter(remaining_letters)

        # check if guessed letter is n the word or not
        if next_letter in word:
            # guessed correctly
            print('{} is in the word'.format(next_letter))

            # Reveal matching letters
            for i in range(len(word)):
                if next_letter == word[i]:
                    idxs[i] = True
        else:
            # Guessed incorrectly
            print('{} is not in word'.format(next_letter))
            # Decreases no of remaining attempts and append guess to wrong letters
            false_attempts -= 1
            wrong_letters.append(next_letter)

        # check if word is properly resolved or not
        if False not in idxs:
            word_resolved = True
        print()

    # the game is over, Reveal the word
    print('word : {}'.format(word))

    # Result
    if word_resolved:
        print('Congratulations!!! You Won...')
    else:
        print('Better Luck Next Time...')

    # User want to try again or not
    try_again = input('You want to try again [Y / y] : ')
    return try_again.lower() == 'y'


if __name__ == '__main__':
    while play_hangman():
        print()
