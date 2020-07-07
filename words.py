""" Function to Fetch a word for Hangman Game """

import random


def get_word(min_word_length):
    """ Get random word from the file """
    no_words_processed = 0
    curr_word = None
    with open('wordlist.txt', 'r') as fp:
        for word in fp:
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            no_words_processed += 1
            if random.randint(1, no_words_processed) == 1:
                curr_word = word
    return curr_word
