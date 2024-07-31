def main(): 
    # try without int()
    x = input("Whats x? ")
    print("x square is", square(x))

def square(n): 
    # for test 2 /> return n + n
    return n * n


if __name__ == "__main__": 
    main()