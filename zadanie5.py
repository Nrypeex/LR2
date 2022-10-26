from math import sqrt

def isPrime():
    print ("input number")
    digit = int(input())
    if digit>10000 | digit<0 : print("wrong input!") 
    i = 2
    while i<=sqrt(digit):
        if(digit%i == 0):
            print("false")
            break
        i += 1
    if(digit%i != 0):print("true")
