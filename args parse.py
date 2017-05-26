import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=int, default=1, help='blablabla')
    parser.add_argument('--y', type=int, default=1, help='blablabla')
    parser.add_argument('--operation', type=str, default='add', help='blablabla')

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y


if __name__ == '__main__':
    main()