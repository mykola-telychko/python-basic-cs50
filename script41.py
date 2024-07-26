import cowsay
import sys

# pip install cowsay
if len(sys.argv) == 2: 
    cowsay.cow("hello " + sys.argv[1])