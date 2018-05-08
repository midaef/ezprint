
import time
import sys
import os


def p(value = ''):
	print(value)


def pwd(s = '', t = 0.01):
	strtoprint = ''
	for i in s:
		strtoprint = strtoprint + str(i)
		sys.stdout.write('\r\r' + (strtoprint) + '')
		time.sleep(t)


def cls():
	os.system('cls')



def pwi(s, width = 50):
	otstup = (width - len(s)) // 2
	return(otstup * ' ' + s)
