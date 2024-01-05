#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        # This will raise a ValueError for negative width
        r1 = Rectangle(-10, 2)
    except ValueError as e:
        print("[ValueError] {}".format(e))

    try:
        # This will raise a ValueError for negative width
        r2 = Rectangle(10, 2)
        r2.width = -10
    except ValueError as e:
        print("[ValueError] {}".format(e))

    try:
        # This will raise a TypeError for assigning a dictionary to x
        r3 = Rectangle(10, 2)
        r3.x = {}
    except TypeError as e:
        print("[TypeError] {}".format(e))

    try:
        # This will raise a ValueError for negative y
        r4 = Rectangle(10, 2, 3, -1)
    except ValueError as e:
        print("[ValueError] {}".format(e))
