import argparse
from functools import lru_cache
import sys

if __name__ == '__main__':
    def _calcArgs(args):
        if args.o == 'add':
            return int(args.x + args.y)
        elif args.o == 'sub':
            return args.x - args.y
        elif args.o == 'mul':
            return args.x * args.y
        elif args.o == 'divide':
            return args.x / args.y

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', help="Enter first number", default=1.0, type=float)
    parser.add_argument('-y', help="Enter second number", default=1.0, type=float)
    parser.add_argument('-o', help="Enter Operation", type=str, default=1.0)

    parseAdd = parser.parse_args()
    sys.stdout.write(str(_calcArgs(parseAdd)))