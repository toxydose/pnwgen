#phone number wordlist generator version 0.2.3
#https://github.com/toxydose

from __future__ import print_function
import sys
import logging

if hasattr(__builtins__, 'raw_input'):
    input=raw_input

logging.basicConfig(level=logging.INFO)

def main():
	global d
	d = input('\nPlease, choose the digits quantity of generated raw output:\n(min 4, max 10, 7 by default - just press ENTER)\n\n>>> ')
	if d == '' or d == '7':
		d = '7'	
		digits()
	if d == '4':
		digits4()
	if d == '5':
		digits5()
	if d == '6':
		digits6()
	if d == '8':
		digits8()
	if d == '9':
		digits9()
	if d == '10':
		digits10()
	if d != '4' and d !='5' and d !='6' and d !='7' and d !='8' and d != '9' and d != '10' and d != '': 
		print('Error: digits quantity must be set between 4 and 10\n.............................')
		main()
	
def verbose():
	logging.info(d + ' digits raw output was choosed\n')
	logging.info('generating '+l[0]+"..."+l[3])

def digits():
	global z
	z = len(open('prefix.txt', "r").readlines())
	global l
	verbose()
	sys.stdout = open('wordlist.txt', 'w')
	while z > 1:
		print(l[0]+'0000000'+l[3])
		for i in range(9999999):
			l[2]+=1
			if l[2]<10:
				l[1]='000000'
			elif l[2]<100 and l[2]>9:
				l[1]='00000'
			elif l[2]<1000 and l[2]>99:	
				l[1]='0000'
			elif l[2]<10000 and l[2]>999:
				l[1]='000'
			elif l[2]<100000 and l[2]>9999:
				l[1]='00'
			elif l[2]<1000000 and l[2]>99999:
				l[1]='0'
			elif l[2]>999999:
				l[1]=''
			for items in l:
				print(items, end='')			
			print('')
		l[2] = 0
		l[0] = text_file.readline().replace('\n', '')
		z = z-1
	text_file.close()
	
def digits4():
	global z
	z = len(open('prefix.txt', "r").readlines())
	sys.stdout = open('wordlist.txt', 'w')
	while z > 1:
		verbose()		
		print(l[0]+'0000'+l[3])
		for i in range(9999):
			l[2]+=1
			if l[2]<10:
				l[1]='000'
			elif l[2]<100 and l[2]>9:
				l[1]='00'
			elif l[2]<1000 and l[2]>99:	
				l[1]='0'
			elif l[2]>999:
				l[1]=''
			for items in l:
				print(items, end='')			
			print('')
		l[2] = 0
		l[0] = text_file.readline().replace('\n', '')
		z = z-1
	text_file.close()

def digits5():
	global z
	z = len(open('prefix.txt', "r").readlines())
	verbose()
	sys.stdout = open('wordlist.txt', 'w')
	while z > 1:
		print(l[0]+'00000'+l[3])
		for i in range(99999):
			l[2]+=1
			if l[2]<10:
				l[1]='0000'
			elif l[2]<100 and l[2]>9:
				l[1]='000'
			elif l[2]<1000 and l[2]>99:	
				l[1]='00'
			elif l[2]<10000 and l[2]>999:
				l[1]='0'
			elif l[2]>9999:
				l[1]=''
			for items in l:
				print(items, end='')			
			print('')
		l[2] = 0
		l[0] = text_file.readline().replace('\n', '')
		z = z-1
	text_file.close()

def digits6():
	global z
	z = len(open('prefix.txt', "r").readlines())
	verbose()
	sys.stdout = open('wordlist.txt', 'w')
	while z > 1:
		print(l[0]+'000000'+l[3])
		for i in range(999999):
			l[2]+=1
			if l[2]<10:
				l[1]='00000'
			elif l[2]<100 and l[2]>9:
				l[1]='0000'
			elif l[2]<1000 and l[2]>99:	
				l[1]='000'
			elif l[2]<10000 and l[2]>999:
				l[1]='00'
			elif l[2]<100000 and l[2]>9999:
				l[1]='0'
			elif l[2]>99999:
				l[1]=''
			for items in l:
				print(items, end='')			
			print('')
		l[2] = 0
		l[0] = text_file.readline().replace('\n', '')
		z = z-1
	text_file.close()

def digits8():
	global z
	z = len(open('prefix.txt', "r").readlines())
	verbose()
	sys.stdout = open('wordlist.txt', 'w')
	while z > 1:
		print(l[0]+'00000000'+l[3])
		for i in range(99999999):
			l[2]+=1
			if l[2]<10:
				l[1]='0000000'
			elif l[2]<100 and l[2]>9:
				l[1]='000000'
			elif l[2]<1000 and l[2]>99:
				l[1]='00000'
			elif l[2]<10000 and l[2]>999:
				l[1]='0000'
			elif l[2]<100000 and l[2]>9999:
				l[1]='000'
			elif l[2]<1000000 and l[2]>99999:
				l[1]='00'
			elif l[2]<10000000 and l[2]>999999:
				l[1]='0'	
			elif l[2]>9999999:	
				l[1]=''
			for items in l:
				print(items, end='')			
			print('')
		l[2] = 0
		l[0] = text_file.readline().replace('\n', '')
		z = z-1
	text_file.close()

def digits9():
	global z
	z = len(open('prefix.txt', "r").readlines())
	verbose()
	sys.stdout = open('wordlist.txt', 'w')
	while z > 1:
		print(l[0]+'000000000'+l[3])
		for i in range(999999999):
			l[2]+=1
			if l[2]<10:
				l[1]='00000000'
			elif l[2]<100 and l[2]>9:
				l[1]='0000000'
			elif l[2]<1000 and l[2]>99:	
				l[1]='000000'
			elif l[2]<10000 and l[2]>999:
				l[1]='00000'
			elif l[2]<100000 and l[2]>9999:
				l[1]='0000'
			elif l[2]<1000000 and l[2]>99999:
				l[1]='000'
			elif l[2]<10000000 and l[2]>999999:
				l[1]='00'
			elif l[2]<100000000 and l[2]>9999999:
				l[1]='0'
			elif l[2]>99999999:
				l[1]=''
			for items in l:
				print(items, end='')			
			print('')
		l[2] = 0
		l[0] = text_file.readline().replace('\n', '')
		z = z-1
	text_file.close()

def digits10():
	global z
	z = len(open('prefix.txt', "r").readlines())
	verbose()
	sys.stdout = open('wordlist.txt', 'w')
	while z > 1:
		print(l[0]+'0000000000'+l[3])
		for i in range(9999999999):
			l[2]+=1
			if l[2]<10:
				l[1]='000000000'
			elif l[2]<100 and l[2]>9:
				l[1]='00000000'
			elif l[2]<1000 and l[2]>99:	
				l[1]='0000000'
			elif l[2]<10000 and l[2]>999:
				l[1]='000000'
			elif l[2]<100000 and l[2]>9999:
				l[1]='00000'
			elif l[2]<1000000 and l[2]>99999:
				l[1]='0000'
			elif l[2]<10000000 and l[2]>999999:
				l[1]='000'
			elif l[2]<100000000 and l[2]>9999999:
				l[1]='00'
			elif l[2]<1000000000 and l[2]>99999999:
				l[1]='0'	
			elif l[2]>999999999:	
				l[1]=''
			for items in l:
				print(items, end='')			
			print('')
		l[2] = 0
		l[0] = text_file.readline().replace('\n', '')
		z = z-1
	text_file.close()

logging.basicConfig(level=logging.INFO)

l=['','',0,'']

text_file = open("prefix.txt", "r")
l[0] = text_file.readline().replace('\n', '')
l[0] = text_file.readline().replace('\n', '')

if len(sys.argv) == 2:
	l[3] = sys.argv[1]

#-------------quick launch------------------------
elif len(sys.argv) == 4:
	l[0] = sys.argv[1]
	l[3] = sys.argv[2]
	lenght = sys.argv[3]	
	d = lenght
	print (lenght)
	if lenght == '4':
		try:
			digits4()
			logging.info('Finished!!!')
			exit()
		except KeyboardInterrupt:
			logging.info('Bye!')	
			exit()
		exit()
	elif lenght == '5':
		try:
			digits5()
			logging.info('Finished!!!')
			exit()
		except KeyboardInterrupt:
			logging.info('Bye!')	
			exit()
		exit()
	elif lenght == '6':
		try:
			digits6()
			logging.info('Finished!!!')
			exit()
		except KeyboardInterrupt:
			logging.info('Bye!')	
			exit()
		exit()
	elif lenght == '7':
		try:
			digits()
			logging.info('Finished!!!')
			exit()
		except KeyboardInterrupt:
			logging.info('Bye!')	
			exit()
		exit()
	elif lenght == '8':
		try:
			digits8()
			logging.info('Finished!!!')
			exit()
		except KeyboardInterrupt:
			logging.info('Bye!')	
			exit()
		exit()
	elif lenght == '9':
		try:
			digits9()
			logging.info('Finished!!!')
			exit()
		except KeyboardInterrupt:
			logging.info('Bye!')	
			exit()
		exit()
	elif lenght == '10':
		try:
			digits10()
			logging.info('Finished!!!')
			exit()
		except KeyboardInterrupt:
			logging.info('Bye!')	
			exit()
		exit()
	else:
		print('the lenght should be from 4 to 10')
		exit()
#-------------------------------------------------	

elif len(sys.argv)==1:
	pass
else:
	print(

'''incorrect arguments!
The input should be:
pnwgen.py 
or:
pnwgen.py [suffix]
or:
pnwgen.py [prefix] [suffix] [generating lenght]
''')

	exit()

try:
	logging.info('--------------------------------')
	logging.info("Creating a wordlist file...")
	main()
	logging.info('Finished!!!')

except KeyboardInterrupt:
	print('\nBye!')
