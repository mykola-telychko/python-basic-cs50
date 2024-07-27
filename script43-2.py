import sys
from script43 import hello

# python .\script43-2.py someText
if len(sys.argv) == 2:
    hello(sys.argv[1]);