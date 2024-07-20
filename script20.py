def main(): 
    number = get_number()
    meow_fn(number)

def get_number():
    while True: 
        n = int(input("Whats n? "))
        if n > 0: 
            return n

def meow_fn(n): 
    for _ in range(n): 
        print("meow")

main()