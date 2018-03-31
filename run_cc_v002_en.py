# -*- coding: utf-8 -*-

#import'ы, которые гарантированно сработают
import os
import time
import json
import random
import smtplib
import datetime

#жизненно важная информация
__author__ = 'Elisey Sharov aka ZerZ™(or ZerZru)'
version = '0.0.2'
program_language = 'python'
game_language = 'english'
country = 'Russian Federation'
license = 'Creative Commons BY-NC'
patch_version = '0.7'

#try:
	#проверка наличия DLC у пользователя
#	import DLC
#	import DLC_Lada
#	import DLC_Audi
#	import DLC_Skoda
#	import DLC_BMW
#	import DLC_Nissan
#	import DLC_Toyota
#	import DLC_F1
#	print('Обнаружены DLC')
#except:
#	print('DLC не обнаружены. Вы можете приоберсти их на официальном сайте.')

global money
global count_cars
count_cars = int('0')
money = int('1000')

try:
	with open('save.json', 'r') as fh:
		data = json.load(fh)
		nickname = data['nickname']
		company = data['company']
		workshop = data['workshop']
		money = data['money']
	print('Detected saved data. Nickname(name): {}, company name: {}, workshop name: {}, capital: {}$'.format(nickname, company, workshop, money))
except:
	nickname = input('Input your name(or nickname): ')
	company = input('Input company name: ')
	a1 = input('')
	f = open('game_news.txt', 'a')
	f.write(a1)
	f.close()
try:
	now = datetime.datetime.now()
	def logs(filename, content, mode='a'):
			#print('New log has been added!')
			with open(filename, mode=mode) as f:
				f.write(content)
	logs('log.txt', now.strftime("[%d-%m-%Y %H:%M] Game has been run. Nickname: {}, company: {}, money: {}. \n".format(nickname, company, money)))
	def stggns():
		a1 = now.strftime("[%d-%m-%Y] \n")
		f = open('game_news.txt', 'a')
		f.write(a1)
		f.close()
	stggns()

	def gaming_news():
		print('Welcome to the publisher GamePublishers! Every time we log in to game_news.txt interesting facts and news of the gaming industry. Sometimes visit our magazine, you can read something interesting!')
		return None

	def details():
		print('Details list: ')
		print('Engines:\n 1) 4A-FE \n 13) 4E-GE 16V \n 14) 8A-FE \n 15) 7A-FE LB \n 16) Alfa Romeo V6 Busso')
		print('Salon: \n 1) Leither \n 2) Soviet classic \n 3) Wooden')
		print('Wheels: \n 1) Steel \n 2) Michelin \n 3) Gold GTA')
		return None

	def ghelp():
		print('1) Help: ghelp() \n 2) How get a money: how_get_a_money() \n 3) Create new car: new_car() \n 4) Name of details: details() \n 5) Search work: works() \n 6) Quit game with save data: gquit() \n 7) Tutorial for car create: how_create_a_auto() \n 8) Mail for your messages: mail() \n 9) Who is competitors: competitors() \n 10) Server hack: virus() \n 11) Support: support() \n 12) Save data: save() \n 13) Delete data: clear() \n 14) Donate(DONT USE IT!): money_help() \n')
		return None

	def money_help():
		a1 = 'НОВОСТИ: Company {} starts his charity! \n'.format(company)
		f = open('game_news.txt', 'a')
		f.write(a1)
		f.close()
		print('You want donate me? THANKS! Donate give motivation for work => updates and path be release faster!')
		print('Yandex.Money: 410013018225939 \n Qiwi: +79889413270')
		print('THANKS!')
		return None

	def save():
		print('Saving data. Please, wait...')
		dict = {}
		dict['nickname'] = nickname
		dict['company'] = company
		dict['money'] = money
		with open('save.json', mode='w') as f:
			json.dump(dict, f)
		time.sleep(5)
		print('Data saved.')
		return None

	def gquit():
		print('You want to quit from game. Saving data. Please, wait...')
		dict = {}
		dict['nickname'] = nickname
		dict['company'] = company
		dict['workshop'] = workshop
		dict['money'] = money
		with open('save.json', mode='w') as f:
			json.dump(dict, f)
		time.sleep(5)
		quit()
		return None

	def how_get_a_money():
		print('1) Sell cars: very costly, but gainful. \n 2) Work: very long time: if you want reach 1000$, you need wait 20 mins(if you on hightest-level work). On work middle-low-level you should spend 1 hour and more.') #in test version time down to seconds
		# 3) Оставить игру в фоне. За каждый час, проведённый в игре, даётся 100$
		return None

	def competitors():
		print('I decided to complicate the game, because otherwise it would be too easy and quickly lose interest. Competitors are your enemies. They can affect the sales of your cars, affect the pricing and popularity of your company. The only way to beat them is to hack into their servers. You can learn more by writing a virus(). Good luck with the capture of the market!')
		pass

	def virus():
		global servers_hacked
		servers_hacked = int('0')
		print('Do you want to get data from your competitors database? Quite a bold move. Select the competitor you want to hack from the list below. Hacking can cost you a lot, so think about it before you start.')
		print('1) BMW \n 2) Audi \n 3) Lada \n 4) Skoda \n 5) Nissan \n 6) Toyota \n 7) Subaru')
		a_v = input('Input competitors name company: ')
		c_1 = 'BMW'
		c_2 = 'Audi'
		c_3 = 'Lada'
		c_4 = 'Skoda'
		c_5 = 'Nissan'
		c_6 = 'Toyota'
		c_7 = 'Subaru'

		if a_v == c_1:
			a_v_c = input('You decided to hack the database BMW. Since this is a large German company, hacking can cost you a fine of $5000. Are you sure? (Yes/No): ')
			yes = 'Yes'
			no = 'No'
			if a_v_c == yes:
				print('You have confirmed your choice. If your break-in will notice, your account will be debited the $5000. If you do not have such a sum, you lose.')
				print('Wait, trying hack...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('The hacking attempt failed. Have you found your attempt? Reaction will know in 10 seconds...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. Your account was debited $5000')
						count = int('5000')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							a1 = 'The cause of the loss: attempted break-in. Statistics: nickname(name): {}, company name: {}, capital: {}. Good luck at another attempt!!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
				elif res == int('1'):
					print('Your hacking attempt was successful!\n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC automatically hacking servers detected. Now the program will pick up passwords.')
						server_hack()
					except:
						print('You do not have the DLC to automatically hacking servers. You will have to find the password and then rewrite it manually. To buy DLC on the site https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. Your account was debited $5000')
						count = int('5000')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							#сохранение результата в файл
							a1 = 'The cause of the loss: the penalty for hacking. Statistics: nickname(nick): {}, company name: {}, capital: ${}. Good luck at another attempt! \n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
			elif a_v_c == 'No':
				print('You decided not to hack into the company database. Your conscience is clear.')
				pass

		if a_v == c_2:
			a_v_c = input('You decided to hack into the Audi database. Since this is a large German company, hacking can cost you a fine of $5000. Are you sure? (Yes/No): ')
			yes = 'Yes'
			no = 'No'
			if a_v_c == yes:
				print('You have confirmed your choice. If your break-in will notice, your account will be debited the $5000. If you do not have such a sum, you lose.')
				print('Wait, there is an attempted break-in...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('The hacking attempt failed. Have you found your attempt? Reaction will know in 10 seconds...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. Your account was debited for $5000')
						count = int('5000')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							a1 = 'The cause of the loss: attempted break-in. Statistics: nickname(name): {}, company name: {}, capital: {}. Good luck next time!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
				elif res == int('1'):
					print('Your hacking attempt was successful!\n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC automatically hacking servers detected. Now the program will pick up passwords.')
						server_hack()
					except:
						print('You do not have the DLC to automatically hacking servers. You will have to find the password and then rewrite it manually. To buy DLC on the site https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. Your account was debited for $5000,')
						count = int('5000')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							#сохранение результата в файл
							a1 = 'The cause of the loss: the penalty for hacking. Statistics: name(nickname): {}, company name: {}, capital: {}$. Good luck next time!\n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
			elif a_v_c == 'No':
				print('You decided not to hack into the company database. Your conscience is clear.')
				pass

		if a_v == c_3:
			a_v_c = input('You decided to hack the database of Lada. Because this company needed only in Russia, hacking can cost you a fine of only $100. Are you sure? (Yes/No): ')
			yes = 'Yes'
			no = 'No'
			if a_v_c == yes:
				print('You have confirmed your choice. If your break-in will notice, your account will be charged a $100. If you do not have such a sum, you lose.')
				print('Wait, there is an attempted break-in...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('The hacking attempt failed. Have you found your attempt? Reaction will know in 10 seconds...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. With your account was debited $100')
						count = int('100')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							a1 = 'The cause of the loss: attempted break-in. Statistics: nick(name): {}, company name: {}, capital: {}. Good luck next time!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
				elif res == int('1'):
					print('Your hacking attempt was successful!\n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC automatically hacking servers detected. Now the program will pick up passwords.')
						server_hack()
					except:
						print('You do not have the DLC to automatically hacking servers. You will have to find the password and then rewrite it manually. To buy DLC on the site https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. With your account was debited $100')
						count = int('100')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							#сохранение результата в файл
							a1 = 'The cause of the loss: the penalty for hacking. Statistics: name(nickname): {}, company name: {}, capital: {}$. Good luck next time!\n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
			elif a_v_c == 'No':
				print('You decided not to hack into the company database. Your conscience is clear.')
				pass

		if a_v == c_4:
			a_v_c = input('You decided to hack into the Skoda database. Since this is a Czech company, hacking can cost you a fine of $2500. Are you sure? (Yes/No): ')
			yes = 'Yes'
			no = 'No'
			if a_v_c == yes:
				print('You have confirmed your choice. If your break-in will notice, your account will be charged 2500$. If you do not have such a sum, you lose.')
				print('Wait, there is an attempted break-in...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('The hacking attempt failed. Have you found your attempt? Reaction will know in 10 seconds...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. Your account was debited $2500')
						count = int('2500')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have ${} left..'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							a1 = 'The cause of the loss: attempted break-in. Statistics: nick(name): {}, company name: {}, capital: {}. Good luck next time!'.format(nickname, company, money)
							f = open('result.txt', 'w')
							f.write(a1)
							f.close()
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
				elif res == int('1'):
					print('Your hacking attempt was successful!\n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC automatically hacking servers detected. Now the program will pick up passwords.')
						server_hack()
					except:
						print('You do not have the DLC to automatically hacking servers. You will have to find the password and then rewrite it manually. To buy DLC on the site https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. Your account was debited for $5000,')
						count = int('2500')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have ${} left..'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							#сохранение результата в файл
							a1 = 'The cause of the loss: the penalty for hacking. Statistics: name(nickname): {}, company name: {}, capital: ${}. Good luck next time!\n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
			elif a_v_c == 'No':
				print('You decided not to hack into the company database. Your conscience is clear.')
				pass
		if a_v == c_5:
			a_v_c = input('You decided to hack into the Nissan database. Since this is a large Japanese company, hacking can cost you a fine of$5,700. Are you sure? (Yes/No): ')
			yes = 'Yes'
			no = 'No'
			if a_v_c == yes:
				print('You have confirmed your choice. If your break-in will notice, your account will be debited $5700. If you do not have such a sum, you lose.')
				print('Wait, there is an attempted break-in...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('The hacking attempt failed. Have you found your attempt? Reaction will know in 10 seconds...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. With your account was debited $5700')
						count = int('5700')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have ${} left.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							a1 = 'The cause of the loss: attempted break-in. Statistics: nick(name): {}, company name: {}, capital: {}. Good luck next time!'.format(nickname, company, money)
							f = open('result.txt', 'w')
							f.write(a1)
							f.close()
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
				elif res == int('1'):
					print('Your hacking attempt was successful!\n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC automatically hacking servers detected. Now the program will pick up passwords.')
						server_hack()
					except:
						print('You do not have the DLC to automatically hacking servers. You will have to find the password and then rewrite it manually. To buy DLC on the site https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. With your account was debited $5700')
						count = int('5700')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							#сохранение результата в файл
							a1 = 'The cause of the loss: the penalty for hacking. Statistics: name(nickname): {}, company name: {}, capital: {}$. Good luck next time!\n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
			elif a_v_c == 'No':
				print('You decided not to hack into the company database. Your conscience is clear.')
				pass
		if a_v == c_7:
			a_v_c = input('You decided to hack into the Toyota database. Since this is a large Japanese company, hacking can cost you a fine of $4900. Are you sure? (Yes/No): ')
			yes = 'Yes'
			no = 'No'
			if a_v_c == yes:
				print('You have confirmed your choice. If your hacking attempt is noticed, your account will be charged $4900. If you do not have such a sum, you lose.')
				print('Wait, there is an attempted break-in...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('The hacking attempt failed. Have you found your attempt? Reaction will know in 10 seconds...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. Your account was debited $4900')
						count = int('4900')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							a1 = 'The cause of the loss: attempted break-in. Statistics: nick(name): {}, company name: {}, capital: {}. Good luck next time!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
				elif res == int('1'):
					print('Your hacking attempt was successful!\n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC automatically hacking servers detected. Now the program will pick up passwords.')
						server_hack()
					except:
						print('You do not have the DLC to automatically hacking servers. You will have to find the password and then rewrite it manually. To buy DLC on the site https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. Your account was debited $4900')
						count = int('4900')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left {}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							#сохранение результата в файл
							a1 = 'The cause of the loss: the penalty for hacking. Statistics: name(nickname): {}, company name: {}, capital: {}$. Good luck next time!\n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
			elif a_v_c == 'No':
				print('You decided not to hack into the company database. Your conscience is clear.')
				pass
		if a_v == c_6:
			a_v_c = input('You decided to hack into the Toyota database. Since this is a large German company, hacking can cost you a fine of $5900. Are you sure? (Yes/No): ')
			yes = 'Yes'
			no = 'No'
			if a_v_c == yes:
				print('You have confirmed your choice. If your break-in will notice, your account will be debited $5900. If you do not have such a sum, you lose.')
				print('Wait, there is an attempted break-in...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('The hacking attempt failed. Have you found your attempt? Reaction will know in 10 seconds...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. With your account was debited $5900')
						count = int('5900')
						if money > count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} went bankrupt after trying to hack the servers of its competitor. It was a very stupid act. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							a1 = 'The cause of the loss: attempted break-in. Statistics: nick(name): {}, company name: {}, capital: {}. Good luck next time!'.format(nickname, company, money)
							f = open('result.txt', 'w')
							f.write(a1)
							f.close()
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
				elif res == int('1'):
					print('Your hacking attempt was successful!\n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC automatically hacking servers detected. Now the program will pick up passwords.')
						server_hack()
					except:
						print('You do not have the DLC to automatically hacking servers. You will have to find the password and then rewrite it manually. To buy DLC on the site https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						a1 = 'NEWS: Company {} noticed the attempted break-in one of the largest car companies! Forecasts: the credibility of this company will fall, which will create for her ouchen major material difficulties. \n'.format(company)
						f = open('game_news.txt', 'a')
						f.write(a1)
						f.close()
						print('Your attempt was discovered. With your account was debited $5900')
						count = int('5900')
						if money > count:
							count_res = money - count
							money = count_res
							print('You have left ${}.'.format(count_res))
						elif money < count:
							a1 = 'NEWS: the company {} was able to pay a fine. We recommend not to buy their shares. \n'.format(company)
							f = open('game_news.txt', 'a')
							f.write(a1)
							f.close()
							print('The fine was higher than your capital. You are bankrupt. We will now save your data to the file result.txt and you will be able to see your statistics. After the save, the game closes. Please wait...')
							#сохранение результата в файл
							a1 = 'The cause of the loss: the penalty for hacking. Statistics: name(nickname): {}, company name: {}, capital: ${}. Good luck next time!\n'.format(nickname, company, money)
							f = open('result.txt', 'w')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('You are out of money. You can go to work and catch up.')
							pass
					elif reaction == int('3'):
						print('You are in luck. Your attempt to not discovered. You can continue to live in peace.')
						pass
			elif a_v_c == 'No':
				print('You decided not to hack into the company database. Your conscience is clear.')
				pass
				
	def works():
		print('Choose the work you are interested in: \n 1) Sweep the yards \n 2) Wash cars \n 3) "Free cash" \n 4) Get an education(not available)')
		class work:
			w1 = int('1') #10$
			w2 = int('2') #15$
			w3 = int('3') #30$
			#w4 = print('Чтобы получить образование, введите ptu()') #поняли, типо функция ПТУ называется
			a = int(input('Input number: '))
			if a == w1:
				print('You wanted to sweep the yards. For this work you will be paid$ 10 after 5 minutes')
				time.sleep(10)
				print('You finish the work.') #в тестовой версии время снижено до 10 секунд 
				global money
				money = money + int('10')
				print('You have earned $10! Your account balance is: ${}'.format(money))
			elif a == w2:
				print('You wanted to wash the cars. For this work you will be paid$ 15 after 10 minutes') #в тестовой версии время снижено до 15 секунд
				time.sleep(15)
				print('You finish the work.')
				money = money + int('15')
				print('You earned $15! Your account balance is: ${}'.format(money))
			elif a ==w3:
				print('You wanted to be a cashier. For this work you will be paid $30 after 20 minutes')  #в тестовой версии время снижено до 20 секунд
				time.sleep(20)
				print('You finish the work.')
				money = money + int('30')
				print('You have earned $30! Your account balance is: ${}'.format(money))
			else:
				print('You have entered the wrong number. Try again or email me if you have an idea for my project.')
				work()
		return None

#	def ptu():
#		print('Вы решили получить о образование.')

	def clear():
		a = input('Do you really want to delete the save file? (Yes/No): ')
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
		yes = 'Yes'
		no = 'No'
		if a == yes:
			try:
				answer = input('Why do you want to delete the save?: ')
				a1 = "NEWS: Company {} is closing. Maybe they couldn't compete. Maybe they have serious material problems? Or all at once? That's how the head of the company comments {}: {}\n".format(company, nickname, answer)
				f = open('game_news.txt', 'a')
				f.write(a1)
				f.close()
				os.remove(path)
				print('Your save file has been deleted')
			except:
				print('The save file was not deleted. It may no already be.')
		elif a == no:
			print('You have decided not to delete the save file.')
		return None

	def how_create_a_auto():
		print('Welcome to the manual for creating a car!')
		print('Getting started: \n when you start the new_car () function, you will be prompted to give a name for your workshop. If the name is occupied, you will have to enter a different value. After creating a workshop you will be offered to give the name, number and ID of the car. This is done to create a collection and history of your cars: your game way up. After creating the passport of the car, you go to the technical part. \ n Technical part \ n in version 0.0.2 3 types of parts are available: engine, interior and wheels. To the engine are 16 parts, interior and wheels - 3. You can find the list and part names by entering details(). So: you will be prompted to enter names for 3 types of parts. After processing, the passport of the car will be updated: it will contain the ID, number, model name and components. You can throw out the passport and create a new car, or take changes and release the car. After confirmation you will be prompted to write a clean car, which you want to produce. After graduation, you will receive money in the account. And this is all over, so you have to wait for updates. You can help the release, if you are going to support me financially. Read more: money_help (). Thank you for playing in CarCreator!')
		return None

	def mail():
		print('Mail for your suggestions: scg-publicmail@yandex.ru')
		pass

	def support():
		print('If you have a technical problem, some function does not work or you have another question or suggestion, you can send us an email(enter mail()) or use this form. If this form does not suit you, visit scgofficial.esy.es/GitHub/#support.')
		a1 = input('Enter your question. Please provide any information that will help us resolve your problem. It is desirable to send log file to e-mail.txt and screenshots of the error. So: ')
		f = open('question.txt', 'w')
		f.write(a1)
		f.close()
		print('Your question is recorded in the question file.txt. Please send it to our mail. You can find it by writing a mail()')
		pass
		
	def new_car():
		global workshop
		global count_cars
		count_cars = int('0')
		try:
			with open('save.json', 'r') as fh:
				data = json.load(fh)
				workshop = data['workshop']
		except:
			workshop = input('Enter a name for the workshop: ')
			a1 = 'NEWS: the company {} opens its workshop! Soon we will know what cars they will produce!\n'.format(company)
			f = open('game_news.txt', 'a')
			f.write(a1)
			f.close()
		w1 = 'Steam'
		while workshop == w1:
			print('This name is already occupied or is a registered trademark.')
			workshop = input('Enter a name for the workshop: ')
		print('Welcome to the workshop {}! Read the manual for creating cars, if you have not already done so.'.format(workshop))
		car_name = input('Enter a model name: ')
		car_name_ver = int(input('Enter the number of the car: '))
		car_id = int(input('Enter the ID of the car: '))
		print('You have created a car with ID: {}, name {} and number {}. Now lets start to assemble the car!'.format(car_id, car_name, car_name_ver))
		engine = input('Enter the engine: ')
		salon = input('Enter the salon: ')
		wheel = input('Enter thw wheels: ')
		e1 = '4A-FE'
		e2 = '4E-GE 16V'
		e3 = '8A-FE'
		e4 = '7A-FE LB'
		e5 = 'Alfa Romeo V6 Busso'
		e6 = 'Alfa Romeo V6 Busso'
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
		elif engine == e6:
			e_input = 'Alfa Romeo V6 Busso'
		else:
			print('In the database does not match with your part. Check that the part is inserted correctly or if you want to add it. You can find out the mail for offers by entering mail()')
			pass
		if salon == s1:
			s_input = 'Leither'
		elif salon == s2:
			s_input = 'Soviet classic'
		elif salon == s3:
			s_input = 'Wooden'
		else:
			print('In the database does not match with your part. Check that the part is inserted correctly or if you want to add it. You can find out the mail for offers by entering mail()')
			pass
		if wheel == w1:
			w_input = 'Steel'
		elif wheel == w2:
			w_input = 'Michelin'
		elif wheel == w3:
			w_input = 'Gold GTA'
		else:
			print('In the database does not match with your part. Check that the part is inserted correctly or if you want to add it. You can find out the mail for offers by entering mail()')
			pass
		global money
		car_points = int('0')
		car_points_engine = int('0')
		car_points_salon = int('0')
		car_points_wheels = int('0')
		if e_input == e1:
			car_points_engine = car_points + int('5')
		elif e_input == e2:
			car_points_engine = car_points + int('5')
		elif e_input == e3:
			car_points_engine = car_points + int('10')
		elif e_input == e4:
			car_points_engine = car_points + int('10')
		elif e_input == e5:
			car_points_engine = car_points + int('15')
		elif e_input == e6:
			car_points_engine = car_points + int('15')

		if s_input == s1:
			car_points_salon = car_points + int('10')
		elif s_input == s2:
			car_points_salon = car_points + int('3')
		elif e_input == s3:
			car_points_salon = car_points + int('15')
		if w_input == w1:
			car_points_wheels = car_points + int('3')
		elif w_input == w2:
			car_points_wheels = car_points + int('5')
		elif e_input == w3:
			car_points_wheels = car_points + int('20')
		global result_car_points
		result_car_points = car_points_engine + car_points_salon + car_points_wheels
		print('Your car scored {} points!'.format(result_car_points))

		if e_input == e1:
			detail_engine_count = int('500')
		elif e_input == e2:
			detail_engine_count = int('500')
		elif e_input == e3:
			detail_engine_count = int('1000')
		elif e_input == e4:
			detail_engine_count = int('1000')
		elif e_input == e5:
			detail_engine_count = int('1500')
		elif e_input == e6:
			detail_engine_count = int('1500')

		if s_input == s1:
			detail_salon_count = int('1000')
		elif s_input == s2:
			detail_salon_count = int('300')
		if w_input == w1:
			detail_wheel_count = int('300')
		elif w_input == w2:
			detail_wheel_count = int('500')
		elif w_input == w3:
			detail_wheel_count = int('2000')
		end_count_car = detail_engine_count + detail_salon_count + detail_wheel_count
		number_car = int(input('The price of your car is ${}. The state of your account: ${}. How many cars do you want to release?: '.format(end_count_car, money)))
		count_car_of_number_car = end_count_car * number_car
		global budjet
		budjet = money - count_car_of_number_car
		print('You have released {} cars worth ${}. The rest of your budget: ${}'.format(number_car, count_car_of_number_car, budjet))

		def compilar_car():
			global money
			car_answer = input('You have created a car with the number {}, ID {}, the name {}, the engine {}, {} interior and {} wheels. Do you confirm your choice? (Yes/No): '.format(car_name_ver, car_id, car_name, e_input, s_input, w_input))
			yes = 'Yes'
			no = 'No'
			if car_answer == yes:
				a1 = 'NEWS: the company {} has released a car called {}. Market value:{}. Total released models: {}. I wonder what will be the demand for these cars? \n'.format(company, car_name, end_count_car, number_car)
				f = open('game_news.txt', 'a')
				f.write(a1)
				f.close()
				print('Your car was released. Waiting for a response to 10 seconds...')
				rp_real = int(random.randint(0, 1000))
				time.sleep(10)
				global budjet
				earnings = rp_real - count_car_of_number_car
				money = budjet + rp_real
				if earnings == int('0'):
					print('You do business at 0. Profit is equal to costs.')
				elif earnings < int('0'):
					print('Lost: {}$'.format(earnings))
				elif earnings > int('0'):
					print('Income: {}$'.format(earnings))
				print('You earned ${}! Your account balance is: ${}.'.format(rp_real, money))
				a1 = 'Model: {}, number: {}, ID: {}. Earned: {}$, Parts: wheels: {}, engine: {}, salon: {} \n'.format(car_name, car_name_ver, car_id, rp_real, w_input, e_input, s_input)
				f = open('cars.txt', 'a')
				f.write(a1)
				f.close()
				print('Statistics about your machine were recorded in the file cars.txt')
				if money < int('0'):
					print('You spent more on the car than you had money. Unfortunately, you are bankrupt. Now we are writing your statistics to the file result.txt. Good luck next time.')
					a1 = 'The reason for the loss: bankruptcy. Statistics: name(nickname): {}, company name: {}, capital: {}$. Good luck next time!'.format(nickname, company, money)
					f = open('result.txt', 'w')
					f.write(a1)
					f.close()
					path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
					os.remove(path)
					quit()
			elif car_answer == no:
				print('You threw the project in the trash. Your condition: {}$'.format(money))
				a1 = 'NEWS: the company {} will not release such an expected car. Fans disappointed. \n'.format(company)
				f = open('game_news.txt', 'a')
				f.write(a1)
				f.close()
				money = money + budjet
				print('You threw the project in the trash. Your condition ${} :'.format(money))
			else:
				print('Your answer is not found. Verify that the data is entered correctly.')
				pass
		compilar_car()
		return None

except Exception as er:
	#print("Don't work")
	logs('log.txt', now.strftime("[%d-%m-%Y %H:%M] Game has been crashed. Check code or re-installing game. Maybe you write not-valid nick or name of company?\n"))
	logs('log.txt', er)