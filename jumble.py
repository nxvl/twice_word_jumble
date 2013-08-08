# coding=utf-8
"""
Word Jumble solver. http://en.wikipedia.org/wiki/Jumble

Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports
import sys

# Framework imports

# 3rd party imports

# Local imports


class Jumble(object):
    """ Jumble object """
    def __init__(self):
        self._read_wordlist('wordlist')

    def solve(self, word):
        """ Solve the puzzle """
        letters = self._letters_set(word)
        solution = []
        for elem in self._powerset_generator(letters):
            if elem in self._wordlist:
                solution += [
                    x for x in self._wordlist[elem] if not x == word
                ]

        csv_string = ', '.join(sorted(list(set(solution))))
        return "%s: %s" % (word, csv_string)

    def _powerset_generator(self, word):
        """
        Generate all posible combinations of a letter set.
        """
        pairs = [(2**index, char) for index, char in enumerate(word)]
        for index in xrange(1, 2**len(word)):
            yield ''.join(char for mask, char in pairs if mask & index)

    def _letters_set(self, word):
        """ Return an ordered string with the letters in word """
        letters = tuple(word.strip())
        return ''.join(sorted(list(letters)))

    def _read_wordlist(self, filename):
        """
        Create a dict of words from wordlist text file.
          Key: set of letters in the word
          Value: words that contain only those letters
        """
        print "Reading word database, this might take a few minutes"
        self._wordlist = {}
        with open(filename, 'r') as f:
            for word in f.readlines():
                letters = self._letters_set(word)

                if letters in self._wordlist:
                    self._wordlist[letters].append(word.strip())
                else:
                    self._wordlist[letters] = [word.strip()]


def get_word():
    """
    Get a word from stdin.
    """
    try:
        word = raw_input("Please enter a word: ").strip()
    except KeyboardInterrupt:
        sys.exit()
    else:
        return word


def main():
    """
    Main loop.
    Loop until END is entered.
    """
    jumble = Jumble()
    while True:
        word = get_word()
        if word == 'END':
            break
        else:
            print jumble.solve(word)


if __name__ == '__main__':
    main()