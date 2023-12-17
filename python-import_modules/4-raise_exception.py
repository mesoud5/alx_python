def raise_exception():
    x = 1 + '1'
if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError:
        print("exception raised")    
