
import time
import sys
import os


def p(value = ''):
	print(value)


def pvd(s = ''):
	strtoprint = ''
	for i in s:
		strtoprint = strtoprint + str(i)
		sys.stdout.write('\r\r' + (strtoprint) + '')
		time.sleep(0.01)


def cls():
	os.system('cls')