# Phone number Wordlist Generator v.0.2.7

A very flexible phone number wordlist generator based on Python.
Obviously, more than 30% users have their mobile phone numbers set as passwords.
Sometimes you need to get a phone-numbers based wordlist for choosen region, but you have a very slow internet connection.

This is a simple but flexible python script that allows you to operatively generate needed wordlist depending on your current situation.
For example, the new mobile network code appears in your country, you do not have to wait when a new wordlist appears, you can generate the new sequence with the new code in a new file, and append this file to your old wordlist using CLI.

##### Requirements:
 Python3*

##### Usage:

-Generates SNs (subscriber numbers) from 4 to 10 digits as raw output:

    4 digits: from 0000 to 9999 
    5 digits: from 00009 to 99999
    ...
    10 digits: from 0000000000 to 9999999999

-Standard raw output is 7 digits

-Allows to add any prefixes (e.g CC, NDC)

-You have to set prefixes manually, just write them to the file "prefix.txt"
    
-Each prefix should be written in a new line
    
-You can input the prefixes in any format (e.g 093, 8093, 8-093, +38(093) e.t.c). For example, if you chosed two prefixes 063 and 093 and the standart raw 7 digits output, the general output in the file "wordlist.txt" will be the next:

    0630000000
    0630000001
    0630000002
    [...]
    0639999999
    0930000000
    0930000001
    0930000002
    [...]
    0939999999
    
It means that the custom prefixes will be switched automatically, and all of generated output you will find in one wordlist file. This feauture differs this script from most other generators, where you have to "set prefix => generate => wait => set prefix => generate => wait => merge two wordlists".

   
-If you want to generate the raw sequence without any prefix, the next line after comment in "prefix.txt" should be empty.

-Allows to add permanent suffix. Just put your suffix in the argument when script is launching.
    
    python3 pnwgen.py [suffix]

Launching:

-Download program

-cd to the program's directory

-put your custom prefixes in the file "prefix.txt"

-type:
    
    python3 pnwgen.py

Quick launch:

    python3 pnwgen.py [prefix] [suffix] [length]

Note: the length you should specify is the length of generated sequence benween the prefix and the suffix, but not the length of the entire numbers that should appear in your wordlist

    
output wordlist.txt size with standard 7-digits raw output:

--without prefixes ~ 80 Mb

--with two 3-digits prefixes ~ 300Mb


##### Performance:
Depends on your PC

##### DISCLAIMER:

Usage of this program is only allowed within boundaries of law. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

https://awake.pro/