#import'ы, которые гарантированно сработают
import time
import random
import datetime

#жизненно важная информация
__author__ = 'Elisey Sharov aka ZerZ™(or ZerZru)'
version = '0.0.1'
language = 'python'
country = 'Russian Federation'
license = 'GNU GPL 3.0'
update_name = "The 'Basic Update'"

try:
	#проверка наличия DLC у пользователя
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
		print('1) Commands: help: ghelp() \n 2) Get money: how_get_a_money() \n 3) Create a new car: new_car() \n 4) Name of details, who added for this moment: details() \n 5) Search work: works() \n 6) EXit from game with save data: gquit() \n 7) How create a car: how_create_a_auto()')
		return None

	def details():
		print('List details of version 0.0.1: ')
		print('Engines: 1) 4A-FE \n 2) 4E-GE 16V \n 3) 8A-FE \n 4) 7A-FE LB \n 5) Alfa Romeo V6 Busso')
		print('Salon: \n 1) Leither \n 2) Soviet classic \n 3) Wooden')
		print('Wheels: \n 1) Steel \n 2) Michelin \n 3) Gold GTA')
		return None

	def support():
		print("If you have a problem, any function don't work or you have another question, you can write me to my mail(input function mail()) or use this form. If you don't want use this form or they don't work, visit scgofficial.esy.es/GitHub/#support.")
		a1 = input('Введите ваш вопрос. Пожалуйста, указывайте любую информацию, которая нам поможет решить вашу проблему. Итак: ')
		f = open('question.txt', 'w')
		f.write(a1)
		f.close()
		print('Ваш вопрос записан в файл question.txt. Пожалуйста, отправьте его на нашу почту. Узнать её можно, написав mail()')
		pass

	def mail():
		print('Mail for your applications: scg-publicmail@yandex.ru')
		pass

	def how_get_a_money():
		print('1) Sell auto: very costly, but very profitable. \n 2) Work: very longer: if yp want get 1000$, you can should spend 20 min(if you at work with high class). At work middle-low class you sholud spen 30 and more min.')
		#at some moment you can create only best car. Badly car added coming soon. Stop! You don't can create auto, sorry.
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

	def new_car():
		workshop = input('Input workshop name: ')
		w1 = 'Steam'
		if workshop == w1:
			print('Its name already taken or be a trade mark')
			workshop = input('Input workshop name: ')
			pass
		print("Welcome to workshop {}! Read help to create auto, if you don't this.".format(workshop))
		car_name = input('Input model name: ')
		car_name_ver = int(input('Input number car: '))
		car_id = int(input('Input car ID: '))
		print("You create auto with ID: {}, name {} and number {}. Now let's create auto!".format(car_id, car_name, car_name_ver))
		engine = input('Input engine: ')
		salon = input('Input salon: ')
		wheel = input('Input wheels: ')
		e1 = '4A-FE'
		e2 = '4E-GE 16V'
		e3 = '8A-FE'
		e4 = '7A-FE LB'
		e5 = 'Alfa Romeo V6 Busso'
		s1 = 'Leither'
		s2 = 'Soviet classic'
		s3 = 'Wooden'
		w1 = 'Steel'
		w2 = 'Michelin'
		w3 = 'Gold GTA'
		if engine == e1:
			e_input = '4A-FE'
		elif engine == e2:
			e_input = '4E-GE 16V'
		elif engine == e3:
			e_input = '8A-FE'
		elif engine == e4:
			e_input = '7A-FE LB'
		elif engine == e5:
			e_input = 'Alfa Romeo V6 Busso'
		else:
			print("In database don't searched your details. Check correct detail name or write me to add your detail. Mail for applications may be know, input mail()")
			engine = input('Input engine: ')
			pass
		if salon == s1:
			s_input = 'Leither'
		elif salon == s2:
			s_input = 'Soviet classic'
		elif salon == s3:
			s_input = 'Wooden'
		else:
			print("In database don't searched your details. Check correct detail name or write me to add your detail. Mail for applications may be know, input mail()")
			salon = input('Input salon: ')
			pass
		if wheel == w1:
			w_input = 'Steel'
		elif wheel == w2:
			w_input = 'Michelin'
		elif wheel == w3:
			w_input = 'Gold GTA'
		else:
			print("In database don't searched your details. Check correct detail name or write me to add your detail. Mail for applications may be know, input mail()")
			wheel = input('Input wheel: ')
			pass
		def compilar_car():
			car_answer = input('You create auto with number {}, ID {}, name {}, engine {}, {} salon and {} wheels. Do you confirm your choice? (Yes/No): '.format(car_name_ver, car_id, car_name, e_input, s_input, w_input))
			yes = 'Yes'
			no = 'No'
			if car_answer == yes:
				print('Your car be released. wait reaction after 10 seconds...')
				rp_real = int(random.randint(0, 1000))
				time.sleep(10)
				print('You reached {} dollars!'.format(rp_real))
			elif car_answer == no:
				print('You give up ypur project.')
			else:
				print('Your answer dont be search. Check correctly data.')
				car_answer = input('Do you confirm your choise? (Yes/No):')
				return money + rp_real
		compilar_car()
		return None
except:
	#print("Don't work")
	logs('log.txt', now.strftime("[%d-%m-%Y %H:%M] Game has been crashed. Check code or re-installing game."))
