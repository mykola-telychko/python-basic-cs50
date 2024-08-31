import sys

def fibonacci_generator(n):
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <number_of_items>")
        sys.exit(1)

    # Get the number of items from the CLI input
    try:
        num_items = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the number of items.")
        sys.exit(1)

    # Generate and print the Fibonacci numbers
    fib_gen = fibonacci_generator(num_items)
    
    print(f"Fibonacci sequence up to {num_items} items:")
    for num in fib_gen:
        print(num)
        
# python script102.py 12

if __name__ == "__main__":
    main()
