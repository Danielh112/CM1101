from itertools import chain, combinations
import textwrap
import string
import re

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would', 'using']


def filter_words(words, skip_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    For example:
    >>> filter_words(["help", "me", "please"], ["me", "please"])
    ['help']
    >>> filter_words(["go", "south"], skip_words)
    ['go', 'south']
    >>> filter_words(['how', 'about', 'i', 'go', 'through', 'that', 'little', 'passage', 'to', 'the', 'south'], skip_words)
    ['go', 'passage', 'south']
    """

    valid_words = []
    for word in words:
        if not (word in skip_words):
            valid_words.append(word)
    return valid_words


def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:
    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned. For example:
    >>> normalise_input("  Go   south! ")
    ['go', 'south']
    >>> normalise_input("!!!  tAkE,.    LAmp!?! ")
    ['take', 'lamp']
    >>> normalise_input("HELP!!!!!!!")
    ['help']
    >>> normalise_input("Now, drop the sword please.")
    ['drop', 'sword']
    >>> normalise_input("Kill ~ tHe :-  gObLiN,. wiTH my SWORD!!!")
    ['kill', 'goblin', 'sword']
    >>> normalise_input("I would like to drop my laptop here.")
    ['drop', 'laptop']
    >>> normalise_input("I wish to take this large gem now!")
    ['take', 'gem']
    >>> normalise_input("How about I go through that little passage to the south...")
    ['go', 'passage', 'south']
    """
    no_punc = remove_punct(user_input)
    no_punc_lower = no_punc.lower()
    words = re.findall(r"\w+", no_punc_lower)
    return filter_words(words, skip_words)


def wrap_text(string):
    return textwrap.fill(string).strip()


def wrap_print(string):
    print(wrap_text(string))


def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss) + 1)))


def get_multi_word_string(word_list, list_of_valid_phrases):
    """This function takes a list of words as input, it then checks combinations
    of words to see if a valid pharse can be found in list_of_valid_phrases.
    This allows support for names's with multiple words.
    """
    for subset in all_subsets(word_list):
        if " ".join(subset) in list_of_valid_phrases:
            return " ".join(subset)
    return False


def cls():
    print("\n" * 100)
