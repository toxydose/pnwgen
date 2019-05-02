VERSION = '0.2.7'

HELP = '''
=== phone number wordlist generator version 0.2.7 ===
https://github.com/toxydose
https://awake.pro/
------------------------------------------------------
-Generates SNs (subscriber numbers) from 4 to 10 digits as raw output:

4 digits: from 0000 to 9999 
5 digits: from 00009 to 99999
...
10 digits: from 0000000000 to 9999999999
-Standard raw output is 7 digits

-Allows to add any prefixes (e.g CC, NDC)

-You have to set prefixes manually, just write them to the file "prefix.txt"

-Each prefix should be written in a new line put your custom prefixes in the file "prefix.txt"

$ python3 pnwgen.py

-Allows to add permanent suffix. Just put your suffix in the argument when script is launching.

$ python3 pnwgen.py [suffix]

Quick launch:

$ python3 pnwgen.py [prefix] [suffix] [length]

'''
