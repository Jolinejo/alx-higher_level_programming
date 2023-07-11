#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("{num} ".format(num="FizzBuzz"), end='')
        elif i % 5 == 0:
            print("{num} ".format(num="Buzz"), end='')
        elif i % 3 == 0:
            print("{num} ".format(num="Fizz"), end='')
        else:
            print("{num} ".format(num=i), end='')
