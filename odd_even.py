#!/bin/python3

N = int(input())

if N % 2 == 1:
  print('Weird') # Odd
else:
  if N in range(2,6):
    print('Not Weird')
  elif N in range (6,21):
    print('Weird')
  elif N > 20:
    print('Not Weird')


# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
