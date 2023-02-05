#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a Sample Python file."""


from __future__ import annotations


def hello_world(i: int = 0) -> str:
    """
    Doc String for hello_world.
    :param i: value to return
    :type i: int
    :return: a string of the value
    :rtype: str
    """

    print("hello world")
    return f"string-{i}"


def good_night() -> str:
    """
    Doc String.
    :return: a string
    :rtype: str
    """
    print("good night")
    return "string"


def hello_goodbye():
    """
    Runs both hello_world and good_night.
    :return: nothing
    """
    hello_world(1)
    good_night()
