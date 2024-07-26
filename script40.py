import sys

if len(sys.argv) < 2: 
    sys.exit("Too few args")

# python .\script40.py name1 name2
for arg in sys.argv[1:]:
    print("hi, my name is", arg)


# 1 exmpl
# if len(sys.argv) < 2: 
#     sys.exit("Too few args")
# elif len(sys.argv) > 2: 
#     sys.exit("Too many args")

# print("hi, my name is", sys.argv[1])