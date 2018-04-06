try:
	import json
	import requests, bs4
except:
	print("You don't have requests and BeautifulSoup4 packages. For use all functions of game, please, install this packages")

try:
	def check_version():
		s = requests.get('http://scgofficial.esy.es/version.html')
		b = bs4.BeautifulSoup(s.text, "html.parser")
		p1 = b.select('.version .p1')
		result_ver = p1[0].getText()
		#print(result_ver)
		version = '003'
		if result_ver != version:
			print('You use old version of CarCreator')
			if version == '001':
				print('This version will be avialable at 23 March, 2018. Please, update your version for get new functions!')
			elif version == '002':
				print('This version will be avialable at 30 March, 2018. Please, update your version for get new functions!')
		elif result_ver == version:
			print('You use latest version of CarCreator')
	check_version()
except:
	print("You don't have internet-connection. Check network and try again")

#info
__author__ = 'Elisey Sharov aka ZerZ™(or ZerZru)'
version = '002'
program_language = 'python'
country = 'Russian Federation'
license = 'CC-BY-NC'
path_version = '0.2'
year = '2018'

en_lang = 'English'
ru_lang = 'Russian'
print('If you have a problem, write support()')

try: #try read language settings
	with open('lang.json', 'r') as fh:
		data = json.load(fh)
		answer = data['lang']
	if answer == en_lang:
		print('Loaded english language')
		def input_function():
			user_function = input('Input function: ')
			if user_function == 'save':
				from en_functions import save
				save()
				input_function()
			elif user_function == 'ghelp':
				from en_functions import ghelp
				ghelp()
				input_function()
			elif user_function == 'gquit':
				from en_functions import gquit
				gquit()
				input_function()
			elif user_function == 'virus':
				from en_functions import virus
				virus()
				input_function()
			elif user_function == 'works':
				from en_functions import works
				works()
				input_function()
			elif user_function == 'clear':
				from en_functions import clear
				clear()
				input_function()
			elif user_function == 'how_create_a_auto':
				from en_functions import how_create_a_auto
				how_create_a_auto()
				input_function()
			elif user_function == 'mail':
				from en_functions import mail
				mail()
				input_function()
			elif user_function == 'support':
				from en_functions import support
				support()
				input_function()
			elif user_function == 'new_car':
				from en_functions import new_car
				new_car()
				input_function()
			elif user_function == 'details':
				from en_functions import details
				details()
				input_function()
			elif user_function == 'how_get_a_money':
				from en_functions import how_get_a_money
				how_get_a_money()
				input_function()
			elif user_function == 'competitors':
				from en_functions import competitors
				competitors()
				input_function()
			elif user_function != ghelp or gquit or save or clear or works or virus or how_create_a_auto or mail or support or new_car or details or how_get_a_money or money_help or competitors:
				print('Function name dont searched. Maybe you use ()')
				input_function()
			pass
		input_function()
	elif answer == ru_lang:
		print('Загружен русский язык')
		def input_function():
			user_function = input('Введите функцию: ')
			if user_function == 'save':
				from ru_functions import save
				save()
				input_function()
			elif user_function == 'ghelp':
				from ru_functions import ghelp
				ghelp()
				input_function()
			elif user_function == 'gquit':
				from ru_functions import gquit
				gquit()
			elif user_function == 'virus':
				from ru_functions import virus
				virus()
				input_function()
			elif user_function == 'works':
				from ru_functions import works
				works()
				input_function()
			elif user_function == 'clear':
				from ru_functions import clear
				clear()
				input_function()
			elif user_function == 'how_create_a_auto':
				from ru_functions import how_create_a_auto
				how_create_a_auto()
				input_function()
			elif user_function == 'mail':
				from ru_functions import mail
				mail()
				input_function()
			elif user_function == 'support':
				from ru_functions import support
				support()
				input_function()
			elif user_function == 'new_car':
				from ru_functions import new_car
				new_car()
				input_function()
			elif user_function == 'details':
				from ru_functions import details
				details()
				input_function()
			elif user_function == 'how_get_a_money':
				from ru_functions import how_get_a_money
				how_get_a_money()
				input_function()
			elif user_function == 'competitors':
				from ru_functions import competitors
				competitors()
				input_function()
			elif user_function != ghelp or gquit or save or clear or works or virus or how_create_a_auto or mail or support or new_car or details or how_get_a_money or money_help or competitors:
				print('Имя функции не найдено. Возможно, вы используете скобки()')
				input_function()
			pass
		input_function()
except:
	answer = input('Choose language:\n1) English\n2) Russian\n')
	if answer == en_lang:
		dict = {} #write in language settings information about choosen lang
		dict['lang'] = answer
		with open('lang.json', mode='w') as f:
			json.dump(dict, f)
		print('Loaded english language')
		def input_function():
			user_function = input('Input function: ')
			if user_function == 'save':
				from en_functions import save
				save()
				input_function()
			elif user_function == 'ghelp':
				from en_functions import ghelp
				ghelp()
				input_function()
			elif user_function == 'gquit':
				from en_functions import gquit
				gquit()
				input_function()
			elif user_function == 'virus':
				from en_functions import virus
				virus()
				input_function()
			elif user_function == 'works':
				from en_functions import works
				works()
				input_function()
			elif user_function == 'clear':
				from en_functions import clear
				clear()
				input_function()
			elif user_function == 'how_create_a_auto':
				from en_functions import how_create_a_auto
				how_create_a_auto()
				input_function()
			elif user_function == 'mail':
				from en_functions import mail
				mail()
				input_function()
			elif user_function == 'support':
				from en_functions import support
				support()
				input_function()
			elif user_function == 'new_car':
				from en_functions import new_car
				new_car()
				input_function()
			elif user_function == 'details':
				from en_functions import details
				details()
				input_function()
			elif user_function == 'how_get_a_money':
				from en_functions import how_get_a_money
				how_get_a_money()
				input_function()
			elif user_function == 'competitors':
				from en_functions import competitors
				competitors()
				input_function()
			elif user_function != ghelp or gquit or save or clear or works or virus or how_create_a_auto or mail or support or new_car or details or how_get_a_money or money_help or competitors:
				print('Function name dont searched. Maybe you use()')
				input_function()
			pass
		input_function()
	elif answer == ru_lang:
		dict = {} #see cooment for en_lang
		dict['lang'] = answer
		with open('lang.json', mode='w') as f:
			json.dump(dict, f)
		print('Загружен русский язык')
		def input_function():
			user_function = input('Введите функцию: ')
			if user_function == 'save':
				from ru_functions import save
				save()
				input_function()
			elif user_function == 'ghelp':
				from ru_functions import ghelp
				ghelp()
				input_function()
			elif user_function == 'gquit':
				from ru_functions import gquit
				gquit()
				input_function()
			elif user_function == 'virus':
				from ru_functions import virus
				virus()
				input_function()
			elif user_function == 'works':
				from ru_functions import works
				works()
				input_function()
			elif user_function == 'clear':
				from ru_functions import clear
				clear()
				input_function()
			elif user_function == 'how_create_a_auto':
				from ru_functions import how_create_a_auto
				how_create_a_auto()
				input_function()
			elif user_function == 'mail':
				from ru_functions import mail
				mail()
				input_function()
			elif user_function == 'support':
				from ru_functions import support
				support()
				input_function()
			elif user_function == 'new_car':
				from ru_functions import new_car
				new_car()
				input_function()
			elif user_function == 'details':
				from ru_functions import details
				details()
				input_function()
			elif user_function == 'how_get_a_money':
				from ru_functions import how_get_a_money
				how_get_a_money()
				input_function()
			elif user_function == 'competitors':
				from ru_functions import competitors
				competitors()
				input_function()
			elif user_function != ghelp or gquit or save or clear or works or virus or how_create_a_auto or mail or support or new_car or details or how_get_a_money or money_help or competitors:
				print('Имя функции не найдено. Возможно, вы используете скобки()')
				input_function()
			pass
		input_function()

def mail():
	print('Our mail for support, questions and suggestions: scg-publicmail@yandex.ru')
	pass

def support():
	print('If you have a technical problem, some function does not work or you have another question or suggestion, you can write to us at mail(enter mail() function) or use this form. If this form does not suit you, then visit scgofficial.esy.es/CarCreator/#support.')
	a1 = input('Enter your question. Please provide any information that may help us resolve your issue. It is desirable to send log file to e-mail and screenshots of the error. So: ')
	f = open('question.txt', 'w')
	f.write(a1)
	f.close()
	print('Your question is recorded in the file question.txt. Please send it to our mail. You can find it by writing a mail()')
	pass
