#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:16:08 2021

@author: miguelcastilh
"""
def is_prime():
    n = int(input("Enter a positive integer (-1 to quit): "))
    while n > 0:
   
        if n == 2 or n == 3 or n == 5 or n == 7:
            print(f"{n} is a prime number.")
            n = int(input("Enter a positive integer (-1 to quit): "))
            return(True)
    
        elif n == 1:
            print(f"{n} is not a prime number.")
            n = int(input("Enter a positive integer (-1 to quit): "))
            return(False)
    
        elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0 or n % 13 ==0 or n%17 ==0:
            print(f"{n} is not a prime number.")
            n = int(input("Enter a positive integer (-1 to quit): "))
            return(False)
    
        else:
            print(f"{n} is a prime number.")
            n = int(input("Enter a positive integer (-1 to quit): "))
            return(True)
    print("quitted u hav")
    
def main():
    is_prime() 
    
main()