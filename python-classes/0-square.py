"""This module creates class square with
    -private instance attribute 
    -Instantiation with size (no type/value verification)
    -with oout importing any module
    """
class square:
    """In this class we will create 
        a private instance attribute called size"""
    def __init__(self, size):
        self.__size = size