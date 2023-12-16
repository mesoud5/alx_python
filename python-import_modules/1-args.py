import sys

def print_arguments():
    # Get the total number of arguments
    num_arguments = len(sys.argv) - 1  # The first argument is the script name

    # Get the list of arguments
    arguments_list = sys.argv[1:]

    # Print the results
    print(f"{num_arguments} argument{'' if num_arguments == 1 else 's'}:")
    for i, arg in enumerate(arguments_list, start=1):
        print(f"{i}: {arg}")
    
    # Calculate the length of the first argument
    first_arg_length = len(arguments_list[0]) if num_arguments >= 1 else 0

    print(f"\n({first_arg_length} )")

if __name__ == "__main__":
    print_arguments()
