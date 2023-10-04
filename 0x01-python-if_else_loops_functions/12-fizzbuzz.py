#!/usr/bin/python3

def fizzbuzz():
    "Prints FizzBuzz in numbers"
    for num in range(1, 101):
        if num % 3 != 0 and num % 5 != 0:
            print(num, end=" ")
        elif num % 3 == num % 5:
            print("FizzBuzz", end=" ")
        else:
            print("{}".format("Fizz" if num % 3 == 0 else "Buzz"), end=" ")
