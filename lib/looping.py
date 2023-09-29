#!/usr/bin/env python3

def happy_new_year():
    sec = 11 
    while sec > 1:
        sec -=1
        print(sec)
        print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    squares = [square ** 2 for square in int_list]
    return squares

square_integers([1,2,3,4,5])

def fizzbuzz():
    x = 0
    while x < 100:
        x+=1
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
fizzbuzz()
        