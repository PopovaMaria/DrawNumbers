#!/usr/bin/env python
import sys

string = []

Zero = ["  ***  ",
        " *   * ",
        " *   * ",
        " *   * ",
        " *   * ",
        " *   * ",
        "  ***  ", ]

One = ["  * ",
       "* * ",
       "  * ",
       "  * ",
       "  * ",
       "  * ",
       " ***"]

Two = [" *** ",
       "*   *",
       "*   *",
       "   * ",
       " *   ",
       "*    ",
       "*****"]

Three = [" *** ", "* *", " *", " ** ", " *", "* *", " *** "]

Four = [" * ", " ** ", " * * ", "* * ", "******", " * ", " * "]

Five = ["*****", "* ", "* ", " *** ", " *", "* *", " *** "]

Six = [" *** ", "* ", "* ", "**** ", "* *", "* *", " *** "]

Seven = ["*****", " *", " * ", " * ", " * ", "* ", "* "]

Eight = [" *** ", "* *", "* *", " *** ", "* *", "* *", " *** "]


Nine = [" ****", "* *", "* *", " ****", " *", " *", " *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

p=sys.argv[1]
numbers = [int(char) for char in p]
for line in range (7):
    for number in numbers:
                temp = Digits[number]
                string.append(temp[line])
    print(' '.join(string))
    string[:] = []
        
