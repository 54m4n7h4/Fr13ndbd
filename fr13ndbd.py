#!/usr/bin/python
import codecs
from argparse import ArgumentParser
from os import system
from time import sleep

red="\033[1;31m"
gris="\033[1;30m"
transparent="\033[0m"
Fiuscha="\033[0;35m"


def display():
	system('clear || cls')
	print("\n\n")

	print("""       oooooooooooo            .o    .oooo.                     .o8 			""")
	sleep(0.1)
	print("""       `888'     `8          o888  .dP""Y88b                   "888 			""")
	sleep(0.1)
	print("""        {0}888         oooo d8b  888        ]8P' ooo. .oo.    .oooo888 			{1}""".format(gris,transparent))
	sleep(0.1)
	print("""        {0}888oooo8    `888""8P  888      <88b.  `888P"Y88b  d88' `888 			{1}""".format(gris,transparent))
	sleep(0.1)
	print("""        {0}888    "     888      888       `88b.  888   888  888   888 			{1}""".format(gris,transparent))
	sleep(0.1)
	print("""        {0}888          888      888  o.   .88P   888   888  888   888 			{1}""".format(Fiuscha,transparent))
	sleep(0.1)
	print("""       {0}o888o        d888b    o888o `8bd88P'   o888o o888o `Y8bod88P"			{1}""".format(Fiuscha,transparent))
	sleep(0.1)
	print("\n                       {0}))){1}  Decoder  {0}((({1}                           ".format(Fiuscha,transparent))
	sleep(0.1)
	print("\n                                                        {}by 54m{}               ".format(Fiuscha,transparent))


def argpass():
	ap = ArgumentParser(add_help=False,usage='')
	ap.add_argument("-h", "--help",nargs='*')
	ap.add_argument("-d", "--decode",nargs='?',const='setd',type=str)
	ap.add_argument("-e", "--encode",nargs='?',const='sete',type=str)
	ap.add_argument("-c", "--crypt",nargs='?',const='setc',type=str)
	return vars(ap.parse_args())


def helps():
	display()
	print('\n\n{}		Welcome in the help Friend ! {}\n\n'.format(gris,transparent))
	print("""-h,--help : show this help message and exit\n""")
	print("""-d,--decode : Decoding""")
	print("""-e,--encode : Encoding""")
	print("""-c,--crypt : crypt message (require)\n\n""")
	exit(0)

def debug(bug,cmt=''):
	display()
	print("\n\n{0}[-]{1} Debug :{0} {2} {1}#{0} {3}{1}\n\n".format(red,transparent,bug,cmt))
	print('Use fr13ndbd -h for help \n\n')
	exit(0)


argsp = argpass()

for i in argsp.keys():
	if type(argsp[i]) is list:argsp[i]=''.join(argsp[i])


def decode(argsp):
	d_in = ['base64','base32','rot13']
	print("\n\n		{}Decoding{}\n\n".format(gris,transparent))
	if argsp['decode'] in d_in:
		print('{} :	{}'.format(argsp['decode'],codecs.decode(argsp['crypt'],argsp['decode'])))
		return 0
	else:
		for i in d_in:
			try:
				print('{} :	{}\n'.format(i,codecs.decode(argsp['crypt'],i)))

			except:print(i+' :	None\n')
	print('\n\n')

def encode(argsp):
	e_in = ['base64','base32','rot13']
	print("\n\n		{}Encoding{}\n\n".format(gris,transparent))

	if argsp['encode'] in e_in:
		print('{} :	{}'.format(argsp['encode'],codecs.encode(argsp['crypt'],argsp['encode'])))
		return 0
	else:
		for i in e_in:
			try:
				print('{} :	{}\n'.format(i,codecs.encode(argsp['crypt'],i)))
			except:
				print('{} :	{}\n'.format(i,'None'))
	print('\n\n')

try:
	if argsp['help'] is not None:helps()
	elif len(set(list(argsp.values()))) == 1:helps()
except Exception as e:debug(e)


if len(set(list(argsp.values()))) == 2:
	if argsp['crypt'] != 'setc' and argsp['crypt'] is not None:
		display()
		decode(argsp)
		encode(argsp)
	else:debug('Argument Error','crypt message missing')
elif len(set(list(argsp.values()))) == 3:
	if argsp['crypt'] != 'setc' and argsp['crypt'] is not None:
		if argsp['decode'] is not None:
			display()
			decode(argsp)
		elif argsp['encode'] is not None:
			display()
			encode(argsp)
		else:debug('Argument Error')
	else:debug('Argument Error','crypt message missing')
elif len(set(list(argsp.values()))) == 4:
	if argsp['crypt'] != 'setc' and argsp['crypt'] is not None:
		display()
		decode(argsp)
		encode(argsp)
	else:debug('Argument Error','crypt message missing')
else:
	debug('Argument Error')