def main(): 
    x = int(input("Whats x?"))
    if is_even(x): 
        print("Even")
    else: 
        print("Odd")

# 1        
# def is_even(n): 
#     if n % 2 == 0: 
#         return True
#     else: 
#         return False

# 2
# def is_even(n): return True if n % 2 == 0 else False

# 3
def is_even(n): 
    return n % 2 == 0

main()