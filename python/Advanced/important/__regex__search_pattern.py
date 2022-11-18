"""
    :return: The Match object has properties and methods used to retrieve information
             about the search, and the result:

    .span() returns a tuple containing the start-, and end positions of the match.
    .string returns the string passed into the function
    .group() returns the part of the string where there was a match
"""

import re as regex
import math


def _check_string_start_to_end():
    _dummy_string_1 = "The rain is Spain"
    _search__logarithm = regex.search("^The.*Spain$", _dummy_string_1)
    print(_search__logarithm)

    if _search__logarithm:
        print("Yup! We got a flaw")
    else:
        print("Sorry, we didn't find anything!!!")


def __find_all_attribute_func():
    """
    :return: Return a list containing every occurrence of "AI" in data.
    """
    __find_all_string = "The main thing is that i'm out"
    find_str__output = regex.findall('in', __find_all_string)
    print(find_str__output)
    # Returns an empty string.
    _returns__empty_string = regex.findall("Company", __find_all_string)
    print(_returns__empty_string)


def __search_first_white_space__character():
    __find_all_string = "The main thing is that i'm out"
    _find_space_string = regex.search("\s", __find_all_string)
    print("White space located at : ", _find_space_string.start())


def __sub_split_function():
    __find_all_string = "The main thing is that i'm out"
    _re_split = regex.split("\s", __find_all_string, maxsplit=4)
    print(_re_split)


def __match_objection():
    """
    :return: Fault in match objects.
    """
    __find_all_string = "The main thing is that i'm out"
    __string_notation = regex.search(r"\bS\w+", __find_all_string)
    print(__string_notation.group())  # Returns tuple


__match_objection()
