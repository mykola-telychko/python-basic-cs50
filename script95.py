import argparse 

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow", type=int)
args = parser.parse_args()

# for _ in range(int(args.n)):
for _ in range(args.n):
    print("meow")

# python .\script95.py -n 7
# python .\script95.py -h