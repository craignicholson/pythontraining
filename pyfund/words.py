#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>

help() can retrieve the doc strings.... <kewl>
"""
import sys
from urllib.request import urlopen


# #! on mac or linux we must mark the .py file as executable
# helps users see the correct version of python to use with this .py
# chmod +x words.py
# now we can run: $> ./words.py http://sixty-north.com/c/t.txt
# pylauncher will help run the run env for your code

# Creating a function example
# Open REPL type: import words
# type words.fetch_words()
# we can only call this within the py REPL
def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document

    Returns:
        A list of strings containing the words
        from a document.
    """
    with urlopen(url) as story:
        # with blocks
        story_words_byte = []
        story_words = []

        for line in story:
            line_words_byte = line.split()
            line_words = line.decode('UTF-8').split()

            for word in line_words_byte:
                story_words_byte.append(word)

            for word in line_words:
                story_words.append(word)

    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        An iterable series of printable items.S
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


# To make this a module we can call form the system prompt
# we need to have the double underscores with the name
# __main__ as an example
# this print(__name__) module level code is executed only once on first import
# this will print __main__
# to get this to execute out function we will add in if statement
if __name__ == '__main__':
    main(sys.argv[1])  # The 0th arg is the module filename not the module name

# print(story_words)
# print(story_words_byte)
