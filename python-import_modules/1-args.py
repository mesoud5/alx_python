#!/usr/bin/env python3
from sys import argv

def print_arguments():
    num_arguments = len(argv) - 1

    # Print the number of arguments
    print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}:", end='')

    if num_arguments == 0:
        print('.')
    else:
        print()

        # Print each argument
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments()
