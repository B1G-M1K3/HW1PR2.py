# CSCI1010: Lab 1, Problem 1
# Filename: hw1pr2.py
# Name:Michael Terrano
# Problem description: Solving the quadratic equation!

from math import *

a = input("Supply a value for a: ")
b = input("supply a value for b: ")
c = input("supply a value for c: ")

a = float(a)
b = float(b)
c = float(c)

x = -b+sqrt(((b**2)-(4*a*c))/2*a)

print("The the solutions for x are",sqrt(x)),"and",-sqrt(x)
