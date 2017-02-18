#phone number wordlist generator version 0.1.2
#https://github.com/toxydose
from __future__ import print_function
import sys

#if hasattr(__builtins__, 'raw_input'):
#    input=raw_input

z = len(open('prefix.txt', "r").readlines())
z=z-1
print(z, ' prefixes was found')
print("Creating a wordlist file...")
sys.stdout = open('wordlist.txt', 'w')
l=['','',0]
text_file = open("prefix.txt", "r")
l[0] = text_file.readline().replace('\n', '')
l[0] = text_file.readline().replace('\n', '')

while z > 0:
	
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
