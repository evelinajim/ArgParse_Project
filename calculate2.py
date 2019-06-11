# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:04:27 2019

@author: Evelina
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

Programmer: Eve Jimenez Sagastegui
Class: Independent Study
Date: 06/10/19
"""


##FINISHED WORK
import argparse
parser = argparse.ArgumentParser()
#group = parser.add_mutually_exclusive_group()
parser.add_argument("-o","--operation",type=str,default="add",
                    help="choose between: add, sub, mult, div")
parser.add_argument("x", type=int, help="first integer")
parser.add_argument("y", type=int, help="second integer")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
summation = args.x+args.y
product = args.x*args.y
difference = args.x-args.y
quotient = args.x / args.y

if args.operation == 'add':
    if args.verbosity >= 2:
        print("{} plus {} equals {}".format(args.x, args.y, summation))
    elif args.verbosity >= 1:
        print("{} + {} == {}".format(args.x, args.y, summation))
    else:
        print(summation)
elif args.operation == 'mult':
    if args.verbosity >= 2:
        print("{} multiplied by {} equals {}".format(args.x, args.y, product))
    elif args.verbosity >= 1:
        print("{} * {} == {}".format(args.x, args.y, product))
    else:
        print(product)
elif args.operation == 'sub':
    if args.verbosity >= 2:
        print("{} subtracted with {} equals {}".format(args.x, args.y, difference))
    elif args.verbosity >= 1:
        print("{} - {} == {}".format(args.x, args.y, difference))
    else:
        print(difference)
elif args.operation == 'div':
    if args.verbosity >= 2:
        print("{} divided by {} equals {}".format(args.x, args.y, quotient))
    elif args.verbosity >= 1:
        print("{} / {} == {}".format(args.x, args.y, quotient))
    else:
        print(quotient)
else:
    print(summation)


