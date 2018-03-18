import time
import random
import datetime

__author__ = 'Elisey Sharov aka ZerZ™(or ZerZru)'
version = str('0.0.1 alfa')
language = 'python, english version'
country = 'Russian Federation'
copyright = 'Elisey Sharov'

try:
	import DLC
	import DLC_Lada
	import DLC_Audi
	import DLC_Skoda
	import DLC_BMW
	import DLC_Nissan
	import DLC_Toyota
	import DLC_F1
	print('Detected DLC')
except Exception as dlc_er:
	print('DLC is not detected. You can got it on official site or repository on github.com', dlc_er)

try:
	nickname = input('Input name(or nickname): ')
	company = input('Input title of company: ')
	#trying running game for insert to log.txt
	#now = datetime.datetime.now()
	#def logs(filename, content, mode='a'):
			#print('New log has been added!')
	#		with open(filename, mode=mode) as f:
	#			f.write(content)
	#print('Work')
	#logs('log.txt', now.strftime("[%d-%m-%Y %H:%M] Game has been run. Nickname: {}, company: {}.".format(nickname, company)))

	def ghelp():
		print('1) Commands: help: ghelp() \n 2) Get money: how_get_a_money() \n 3) Create a new car: new_car() \n 4) Name of details, who added for this moment: details() \n 5) Найти работу: works()')
		return None

	def how_get_a_money():
		print('1) Sell auto: very costly, but very profitable. \n 2) Work: very longer: if yp want get 1000$, you can should spend 20 min(if you at work with high class). At work middle-low class you sholud spen 30 and more min.')
		#at this moment you can create only best car. Badly car added coming soon. Stop! You don't can create auto, sorry.
		#maybe I add resell auto: you buy car from another company and resell it.
		# 3) Оставить игру в фоне. За каждый час, проведённый в игре, даётся 100$
		return None

	def work():
		money = int('1000')
		print('Choose work: \n 1) Clean streets \n 2) Wash cars \n 3) Seller of food products \n 4) Get education') #education is not added
		class work:
			w1 = int('1') #10$
			w2 = int('2') #15$
			w3 = int('3') #30$
			#w4 = print('In this be a getting education')
			a = int(input('Input number of your choice: '))

			if a == w1:
				print('You want clean streets. You get 10$ after 5 minuts.') #in test version time down into 10 sec
				time.sleep(10)
				print('You ended work. You get 10$. Status of your cash: input [money]')
				money + int('10')
			elif a == w2:
				print('You want to wash cars. You get 15$ after 10 minuts') #in test version time down into 15 sec
				time.sleep(15)
				print('You ended work. you get 15$. Status of your cash: input [money]')
				money + int('15')
			elif a ==w3:
				print('You want to be a seller of food products. You get 30$ after 20 minuts') #in test version time down into 20 sec
				time.sleep(20)
				print('You ended work. You get 30$. Status of your cash: input [money]')
				money + int('30')
			else:
				print('You input a non avialable number. Try again or write me, if you have idea for my project')
				work()
except:
	#print("Don't work")
	logs('log.txt', now.strftime("[%d-%m-%Y %H:%M] Game has been crashed. Check code or re-installing game."))
