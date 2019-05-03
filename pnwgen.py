#!/usr/bin/env python3

# phone number wordlist generator version 0.2.7
# https://github.com/toxydose
# https://awake.pro/

import sys
import logging
from doc import *

if '-v' in sys.argv:
    print('Phone number Wordlist Generator v.' + VERSION)
    exit()
elif '-h' in sys.argv:
    print(HELP)
    exit()

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


def main():
    global digits_number
    digits_number = input(
        '\nChoose the number of digits in generated raw output:\n(min 4, max 10, 7 (by default) - press ENTER)\n\n>>> ')
    logging.info(digits_number + ' digits raw output was choosed\n')

    if digits_number == '' or digits_number == '7':
        digits_number = '7'
        digits()
    elif digits_number == '4':
        digits4()
    elif digits_number == '5':
        digits5()
    elif digits_number == '6':
        digits6()
    elif digits_number == '8':
        digits8()
    elif digits_number == '9':
        digits9()
    elif digits_number == '10':
        digits10()
    else:
        print('Error: number of digits must be set between 4 and 10\n.............................')
        main()


def verbose():
    logging.info('generating ' + gen_form[0] + "***" + gen_form[3])


def digits():
    global prefix_len
    prefix_len = len(open('prefix.txt', "r").readlines())
    global gen_form
    sys.stdout = open('wordlist.txt', 'w')
    while prefix_len > 1:
        verbose()
        print(gen_form[0] + '0000000' + gen_form[3])
        for i in range(9999999):
            gen_form[2] += 1
            if gen_form[2] < 10:
                gen_form[1] = '000000'
            elif gen_form[2] < 100 and gen_form[2] > 9:
                gen_form[1] = '00000'
            elif gen_form[2] < 1000 and gen_form[2] > 99:
                gen_form[1] = '0000'
            elif gen_form[2] < 10000 and gen_form[2] > 999:
                gen_form[1] = '000'
            elif gen_form[2] < 100000 and gen_form[2] > 9999:
                gen_form[1] = '00'
            elif gen_form[2] < 1000000 and gen_form[2] > 99999:
                gen_form[1] = '0'
            elif gen_form[2] > 999999:
                gen_form[1] = ''
            for items in gen_form:
                print(items, end='')
            print('')
        gen_form[2] = 0
        gen_form[0] = text_file.readline().replace('\n', '')
        prefix_len = prefix_len - 1
    text_file.close()


def digits4():
    global prefix_len
    prefix_len = len(open('prefix.txt', "r").readlines())
    sys.stdout = open('wordlist.txt', 'w')
    while prefix_len > 1:
        verbose()
        print(gen_form[0] + '0000' + gen_form[3])
        for i in range(9999):
            gen_form[2] += 1
            if gen_form[2] < 10:
                gen_form[1] = '000'
            elif gen_form[2] < 100 and gen_form[2] > 9:
                gen_form[1] = '00'
            elif gen_form[2] < 1000 and gen_form[2] > 99:
                gen_form[1] = '0'
            elif gen_form[2] > 999:
                gen_form[1] = ''
            for items in gen_form:
                print(items, end='')
            print('')
        gen_form[2] = 0
        gen_form[0] = text_file.readline().replace('\n', '')
        prefix_len = prefix_len - 1
    text_file.close()


def digits5():
    global prefix_len
    prefix_len = len(open('prefix.txt', "r").readlines())
    sys.stdout = open('wordlist.txt', 'w')
    while prefix_len > 1:
        verbose()
        print(gen_form[0] + '00000' + gen_form[3])
        for i in range(99999):
            gen_form[2] += 1
            if gen_form[2] < 10:
                gen_form[1] = '0000'
            elif gen_form[2] < 100 and gen_form[2] > 9:
                gen_form[1] = '000'
            elif gen_form[2] < 1000 and gen_form[2] > 99:
                gen_form[1] = '00'
            elif gen_form[2] < 10000 and gen_form[2] > 999:
                gen_form[1] = '0'
            elif gen_form[2] > 9999:
                gen_form[1] = ''
            for items in gen_form:
                print(items, end='')
            print('')
        gen_form[2] = 0
        gen_form[0] = text_file.readline().replace('\n', '')
        prefix_len = prefix_len - 1
    text_file.close()


def digits6():
    global prefix_len
    prefix_len = len(open('prefix.txt', "r").readlines())
    sys.stdout = open('wordlist.txt', 'w')
    while prefix_len > 1:
        verbose()
        print(gen_form[0] + '000000' + gen_form[3])
        for i in range(999999):
            gen_form[2] += 1
            if gen_form[2] < 10:
                gen_form[1] = '00000'
            elif gen_form[2] < 100 and gen_form[2] > 9:
                gen_form[1] = '0000'
            elif gen_form[2] < 1000 and gen_form[2] > 99:
                gen_form[1] = '000'
            elif gen_form[2] < 10000 and gen_form[2] > 999:
                gen_form[1] = '00'
            elif gen_form[2] < 100000 and gen_form[2] > 9999:
                gen_form[1] = '0'
            elif gen_form[2] > 99999:
                gen_form[1] = ''
            for items in gen_form:
                print(items, end='')
            print('')
        gen_form[2] = 0
        gen_form[0] = text_file.readline().replace('\n', '')
        prefix_len = prefix_len - 1
    text_file.close()


def digits8():
    global prefix_len
    prefix_len = len(open('prefix.txt', "r").readlines())
    sys.stdout = open('wordlist.txt', 'w')
    while prefix_len > 1:
        verbose()
        print(gen_form[0] + '00000000' + gen_form[3])
        for i in range(99999999):
            gen_form[2] += 1
            if gen_form[2] < 10:
                gen_form[1] = '0000000'
            elif gen_form[2] < 100 and gen_form[2] > 9:
                gen_form[1] = '000000'
            elif gen_form[2] < 1000 and gen_form[2] > 99:
                gen_form[1] = '00000'
            elif gen_form[2] < 10000 and gen_form[2] > 999:
                gen_form[1] = '0000'
            elif gen_form[2] < 100000 and gen_form[2] > 9999:
                gen_form[1] = '000'
            elif gen_form[2] < 1000000 and gen_form[2] > 99999:
                gen_form[1] = '00'
            elif gen_form[2] < 10000000 and gen_form[2] > 999999:
                gen_form[1] = '0'
            elif gen_form[2] > 9999999:
                gen_form[1] = ''
            for items in gen_form:
                print(items, end='')
            print('')
        gen_form[2] = 0
        gen_form[0] = text_file.readline().replace('\n', '')
        prefix_len = prefix_len - 1
    text_file.close()


def digits9():
    global prefix_len
    prefix_len = len(open('prefix.txt', "r").readlines())
    sys.stdout = open('wordlist.txt', 'w')
    while prefix_len > 1:
        verbose()
        print(gen_form[0] + '000000000' + gen_form[3])
        for i in range(999999999):
            gen_form[2] += 1
            if gen_form[2] < 10:
                gen_form[1] = '00000000'
            elif gen_form[2] < 100 and gen_form[2] > 9:
                gen_form[1] = '0000000'
            elif gen_form[2] < 1000 and gen_form[2] > 99:
                gen_form[1] = '000000'
            elif gen_form[2] < 10000 and gen_form[2] > 999:
                gen_form[1] = '00000'
            elif gen_form[2] < 100000 and gen_form[2] > 9999:
                gen_form[1] = '0000'
            elif gen_form[2] < 1000000 and gen_form[2] > 99999:
                gen_form[1] = '000'
            elif gen_form[2] < 10000000 and gen_form[2] > 999999:
                gen_form[1] = '00'
            elif gen_form[2] < 100000000 and gen_form[2] > 9999999:
                gen_form[1] = '0'
            elif gen_form[2] > 99999999:
                gen_form[1] = ''
            for items in gen_form:
                print(items, end='')
            print('')
        gen_form[2] = 0
        gen_form[0] = text_file.readline().replace('\n', '')
        prefix_len = prefix_len - 1
    text_file.close()


def digits10():
    global prefix_len
    prefix_len = len(open('prefix.txt', "r").readlines())
    sys.stdout = open('wordlist.txt', 'w')
    while prefix_len > 1:
        verbose()
        print(gen_form[0] + '0000000000' + gen_form[3])
        for i in range(9999999999):
            gen_form[2] += 1
            if gen_form[2] < 10:
                gen_form[1] = '000000000'
            elif gen_form[2] < 100 and gen_form[2] > 9:
                gen_form[1] = '00000000'
            elif gen_form[2] < 1000 and gen_form[2] > 99:
                gen_form[1] = '0000000'
            elif gen_form[2] < 10000 and gen_form[2] > 999:
                gen_form[1] = '000000'
            elif gen_form[2] < 100000 and gen_form[2] > 9999:
                gen_form[1] = '00000'
            elif gen_form[2] < 1000000 and gen_form[2] > 99999:
                gen_form[1] = '0000'
            elif gen_form[2] < 10000000 and gen_form[2] > 999999:
                gen_form[1] = '000'
            elif gen_form[2] < 100000000 and gen_form[2] > 9999999:
                gen_form[1] = '00'
            elif gen_form[2] < 1000000000 and gen_form[2] > 99999999:
                gen_form[1] = '0'
            elif gen_form[2] > 999999999:
                gen_form[1] = ''
            for items in gen_form:
                print(items, end='')
            print('')
        gen_form[2] = 0
        gen_form[0] = text_file.readline().replace('\n', '')
        prefix_len = prefix_len - 1
    text_file.close()


# logging.basicConfig(level=logging.INFO)

gen_form = ['', '', 0, '']

text_file = open("prefix.txt", "r")
gen_form[0] = text_file.readline().replace('\n', '')
gen_form[0] = text_file.readline().replace('\n', '')

if len(sys.argv) == 2:
    gen_form[3] = sys.argv[1]

# -------------quick launch------------------------
elif len(sys.argv) == 4:
    gen_form[0] = sys.argv[1]
    gen_form[3] = sys.argv[2]
    length = sys.argv[3]
    digits_number = length
    print(length)
    if length == '4':
        try:
            digits4()
            logging.info('Finished!!!')
            exit()
        except KeyboardInterrupt:
            logging.info('Bye!')
            exit()
        exit()
    elif length == '5':
        try:
            digits5()
            logging.info('Finished!!!')
            exit()
        except KeyboardInterrupt:
            logging.info('Bye!')
            exit()
        exit()
    elif length == '6':
        try:
            digits6()
            logging.info('Finished!!!')
            exit()
        except KeyboardInterrupt:
            logging.info('Bye!')
            exit()
        exit()
    elif length == '7':
        try:
            digits()
            logging.info('Finished!!!')
            exit()
        except KeyboardInterrupt:
            logging.info('Bye!')
            exit()
        exit()
    elif length == '8':
        try:
            digits8()
            logging.info('Finished!!!')
            exit()
        except KeyboardInterrupt:
            logging.info('Bye!')
            exit()
        exit()
    elif length == '9':
        try:
            digits9()
            logging.info('Finished!!!')
            exit()
        except KeyboardInterrupt:
            logging.info('Bye!')
            exit()
        exit()
    elif length == '10':
        try:
            digits10()
            logging.info('Finished!!!')
            exit()
        except KeyboardInterrupt:
            logging.info('Bye!')
            exit()
        exit()
    else:
        print('the length should be from 4 to 10')
        exit()
# -------------------------------------------------

elif len(sys.argv) == 1:
    pass
else:
    print(

        '''incorrect arguments!
The input should be:
pnwgen.py 
or:
pnwgen.py [suffix]
or:
pnwgen.py [prefix] [suffix] [generating length]

Please use -h for help
''')

    exit()

try:
    logging.info('--------------------------------')
    logging.info("Creating a wordlist file...")
    main()
    logging.info('Finished!!!')

except KeyboardInterrupt:
    print('\nBye!')
