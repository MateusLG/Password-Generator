#!/usr/bin/env python3
"""
Password Generator is a simple program that generates strong passwords for you.
"""

from generator import genPass

if __name__ == "__main__":
    print(genPass(lenght=int(input("How many characters do you want your password to be? "))))
