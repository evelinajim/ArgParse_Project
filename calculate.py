# -*- coding: utf-8 -*-
"""
Spyder Editor

Programmer: Eve Jimenez Sagastegui
Class: Independent Study
Date: 06/10/19
"""

"""
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("-a","--add",nargs="+",help="adds numbers together")
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)

"""
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
"""

import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-a","--add", help="adds two given numbers together. type -add")
group.add_argument("-m","--multiply", help="multiplies two given numbers together.type -multiply")
parser.add_argument("x", type=int, help="first integer")
parser.add_argument("y", type=int, help="second integer")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
summation = args.x+args.y
product = args.x*args.y

if args.add:
    if args.verbosity >= 2:
        print("{} plus {} equals {}".format(args.x, args.y, summation))
    elif args.verbosity >= 1:
        print("{}+{} == {}".format(args.x, args.y, summation))
    else:
        print(summation)
elif args.multiply:
    if args.verbosity >= 2:
        print("{} multiplied by {} equals {}".format(args.x, args.y, product))
    elif args.verbosity >= 1:
        print("{}*{} == {}".format(args.x, args.y, product))
    else:
        print(product)
else:
    print(summation)

"""
#untouched verbo
if args.verbosity >= 2:
    print("{} plus {} equals {}".format(args.x, args.y, summation))
elif args.verbosity >= 1:
    print("{}+{} == {}".format(args.x, args.y, summation))
else:
    print(summation)
"""
