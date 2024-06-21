#!/usr/bin/env python3

# phone number wordlist generator version 0.5
# https://github.com/toxydose

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


def main(suffix):
    global digits_number
    digits_number = input(
        '\nChoose the number of digits in generated raw output:\n(min 4, max 10, 7 (by default) - press ENTER)\n\n>>> ')
    logging.info(' Generating worlist file...')
    if digits_number == '' or digits_number == '7':
        logging.info(' 7 digits raw output chosen\n')
        digits_number = '7'
        digits(7, suffix=suffix)
    elif digits_number == '4':
        logging.info(' ' + digits_number + ' digits raw output chosen\n')    
        digits(4, suffix=suffix)
    elif digits_number == '5':
        logging.info(' ' + digits_number + ' digits raw output chosen\n')
        digits(5, suffix=suffix)
    elif digits_number == '6':
        logging.info(' ' + digits_number + ' digits raw output chosen\n')
        digits(6, suffix=suffix)
    elif digits_number == '8':
        logging.info(' ' + digits_number + ' digits raw output chosen\n')
        digits(8, suffix=suffix)
    elif digits_number == '9':
        digits(9, suffix=suffix)
        logging.info(' ' + digits_number + ' digits raw output chosen\n')
    elif digits_number == '10':
        logging.info(' ' + digits_number + ' digits raw output chosen\n')
        logging.info(' WARNING 10 digits output generation might take a lot of time and consume about 300 GB of disk space!')
        digits(10, suffix=suffix)
    else:
        print('Error: number of digits must be set between 4 and 10\n.............................')
        main(suffix)


# def verbose():
#     logging.info('generating ' + gen_form[0] + "***" + gen_form[3])


def digits(pow, prefix_from_file=True, prefix="", suffix=""):
    prefixes = []
    if prefix_from_file:
        with open('prefix.txt', 'r') as file_prefix:
            for line in iter(file_prefix.readline, ''):
                if not line.lstrip().startswith('#'):
                    prefixes.append(line.rstrip('\n'))
    else:
        prefixes.append(prefix)
    if not prefixes:
        prefixes.append("")

    n = 10 ** pow
    step = 10000
    with open('wordlist.txt', 'w') as file_out:
        for prefix in prefixes:
            for i in range(n//step):
                out_list = []
                for j in range(step):
                    out_list.append("{}{}{}\n".format(prefix, str(i*step+j).zfill(pow), suffix))
                file_out.write("".join(out_list))


# logging.basicConfig(level=logging.INFO)

prefix = ""
suffix = ""

if len(sys.argv) == 2:
    suffix = sys.argv[1]

# -------------quick launch------------------------
elif len(sys.argv) == 4:
    prefix = sys.argv[1]
    suffix = sys.argv[2]
    length = sys.argv[3]
    digits_number = int(length)
    if (digits_number >= 4) and (digits_number <= 10):
        try:
            digits(digits_number, prefix_from_file=False, prefix=prefix, suffix=suffix)
            logging.info(' ' + str(digits_number) + ' digits raw output chosen\n')    
            logging.info(' Generating worlist file...')
            logging.info(' Finished!!!')
            exit()
        except KeyboardInterrupt:
            logging.info(' Bye!')
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
    print('Phone number Wordlist Generator v.' + VERSION)
    main(suffix)
    logging.info(' Finished!!!')

except KeyboardInterrupt:
    print('\nBye!')
