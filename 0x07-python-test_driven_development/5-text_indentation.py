#!/usr/bin/python3
""" This module prints a text with 2 new lines. """


def text_indentation(text):
    """ The function text_indentation prints a text with 2
    new lines after each of these characters: ., ? and :
    Parameter: text(must be a string)
    Raise: typeerror.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    alpha = 0
    while alpha < len(text) and text[alpha] == " ":
        alpha += 1
    while alpha < len(text):
        print(text[alpha], end="")
        if text[alpha] == "\n" or text[alpha] in ".?:":
            if text[alpha] in ".?:":
                print("\n")
            alpha += 1
            while alpha < len(text) and text[alpha] == " ":
                alpha += 1
            continue
        alpha += 1
