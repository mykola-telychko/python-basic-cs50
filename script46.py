def main(): 
    name = input("Whats your name? ")
    # hello(name)
    print(hello(name))

def hello(to="world"): 
    # print("hi,", to)
    return f"hi, {to}"

if __name__ == "__main__":
    main()