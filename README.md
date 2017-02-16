# Phonenumber Wordlist Generator v.0.1

A wery flexible phonenumber wordlist generator based on python
Obviously, more than 30% users have their mobile phone numbers setted as passwords.
Sometimes you need to get a phone-numbers based wordlist for choosen region, but you have very slow internet connection.

This is a simple but flexible python script that allows you to operatively generate needed wordlist depending on your current situation.
For example, the new mobile network code appears in your country, you have not wait when a new wordlist appears, you can generate the the new sequence with the new code in a new file, and attach this file to your old wordlist using CLI.

Usage:
-Generates SNs (subscribe numbers) from 0000000 to 9999999 
-allows to add any prefixes (e.g CC, NDC):
    --you have to set prefixes manually, just write them to the file "prefix.txt"
    --each prefix should be written in a new line
    --you can input the prefixes in any format
                              (e.g 093, 8093, 8-093, +38(093) e.t.c)
    --if you dont want to use any prefixes, just leave the prefix.txt empty
    --if you want to generate just one sequence without any prefix, one of the lines in prefix.txt should be empty.	

Launching:
-Download program
-cd to the program's directory
-put your custom prefixes in the file "prefix.txt"
-type:
python3 pnwgen.py

output wordlist.txt size:
--without prefixes ~ 80 Mb
--with two 3-digits prefixes ~ 300Mb

generating speed depends on your PC

In the next version:
compability with python 2.*
