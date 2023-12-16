import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    plural_suffix = 's' if argc != 1 else ''
    print(f"{argc} argument{plural_suffix}:", end='\n')
    if argc == 0:
        print('.')
    else:
        print()
        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")