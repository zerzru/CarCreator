#import'ы, которые гарантированно сработают
import time
import random
import datetime

#жизненно важная информация
__author__ = 'Elisey Sharov aka ZerZ™(or ZerZru)'
version = str('0.0.1 alfa')
language = 'python'
country = 'Russian Federation'
copyright = 'Elisey Sharov'

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
	print('Обнаружены DLC')
except Exception as dlc_er:
	print('DLC не обнаружены. Вы можете приоберсти их на официальном сайте.', dlc_er)

try:
	nickname = input('Введите имя(или ник): ')
	company = input('Введите название компании: ')
	#проверка запуска игры для дальнейшео написания в лог
	#now = datetime.datetime.now()
	#def logs(filename, content, mode='a'):
			#print('New log has been added!')
	#		with open(filename, mode=mode) as f:
	#			f.write(content)
	#print('Work')
	#logs('log.txt', now.strftime("[%d-%m-%Y %H:%M] Game has been run. Nickname: {}, company: {}.".format(nickname, company)))

	def ghelp():
		print('1) Вызвать help: ghelp() \n 2) Узнать, как зарабатывать: how_get_a_money() \n 3) Создать новую машину: new_car() \n 4) Узнать названия деталей, доступных на данный момент: details() \n 5) Найти работу: works()')
		return None

	def how_get_a_money():
		print('1) Продавать автомобили: самый дорогостоящий способ, но очень прибыльный. \n 2) Быть на работе: самый долгий способ: чтобы накопить 1000$, потребуется около 20 минут(если вы на самой престижной работе). На работе средне-низкого уровня понадобится от часа и более.')
		# 3) Оставить игру в фоне. За каждый час, проведённый в игре, даётся 100$
		return None

	def work():
		money = int('1000')
		print('Выберете интересующую вас работу: \n 1) Подметать дворы \n 2) Мыть автомобили \n 3) "Свободная касса" \n 4) Получить образование')
		class work:
			w1 = int('1') #10$
			w2 = int('2') #15$
			w3 = int('3') #30$
			w4 = print('Чтобы получить образование, введите ptu()') #поняли, типо функция ПТУ называется
			a = int(input('Введите номер: '))

			if a == w1:
				print('Вы захотели подметать дворы. За эту работу вам заплатят 10$ по истечении 5 минут')
				time.sleep(10)
				print('Вы закончили работу. На ваш счёт было переведено 10$. Узнать состояние своего счёта можно, введя money') #в тестовой версии время снижено до 10 секунд 
				money + int('10')
			elif a == w2:
				print('Вы захотели мыть автомобили. За эту работу вам заплатят 15$ по истечении 10 минут') #в тестовой версии время снижено до 15 секунд
				time.sleep(15)
				print('Вы закончили работу. На ваш счёт было переведено 15$. Узнать состояние своего счёта можно, введя money')
				money + int('15')
			elif a ==w3:
				print('Вы захотели быть кассиром. За эту работу вам заплатят 30$ по истечении 20 минут')  #в тестовой версии время снижено до 20 секунд
				time.sleep(20)
				print('Вы закончили работу. На ваш счёт было переведено 30$. Узнать состояние своего счёта можно, введя money')
				money + int('30')
			else:
				print('You input a non avialable number. Try again or write me, if you have idea for my project')
				work()

except:
	#print("Don't work")
	logs('log.txt', now.strftime("[%d-%m-%Y %H:%M] Game has been crashed. Check code or re-installing game."))