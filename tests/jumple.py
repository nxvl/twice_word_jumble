# coding=utf-8
"""
Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports

# 3rd party imports
import pytest

# Local imports
import jumble


def test_get_word():
    """
    Test get command.
    """
    inputs = ['Foo', 'bar', 'moo', 'cow']
    for value in inputs:
        jumble.raw_input = lambda _: '%s\n' % value
        ret = jumble.get_word()

        assert ret == value


class JumbleMock(jumble.Jumble):
    """
    Jumble mock class.
    """
    def __init__(self):
        self._read_wordlist('test_wordlist')


def test_jumble_read_wordlist():
    """
    Test wordlist reader.
    """
    mock = JumbleMock()

    assert mock._wordlist == {
        'dgoo': ['good'],
        'dgo': ['god', 'dog'],
        'do': ['do'],
        'go': ['go']
    }


def test_jumble_letters_set():
    """
    Test jumble letter set generator
    """
    obj = jumble.Jumble()

    words = (
        ('dog', 'dgo'),
        ('awesome', 'aeemosw'),
        ('computer', 'cemoprtu'),
        ('cocoon', 'ccnooo')
    )

    for word in words:
        assert obj._letters_set(word[0]) == word[1]


def test_powerset_generator():
    """
    Test powerset generator.
    """
    obj = JumbleMock()

    assert sorted([x for x in obj._powerset_generator('abc')]) == [
        'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'
    ]


def test_jumble_solve():
    """
    Test the puzzle solver.
    """
    obj = JumbleMock()

    assert obj.solve('dog') == 'dog: do, go, god'
    assert obj.solve('good') == 'good: do, dog, go, god'