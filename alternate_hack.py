import random
import time

def server_hack():
	server_password = 'PzgY3PqhP59$XZ2a?sihhFozdnNM428OC6bQBXIj4xFmY'
	pass_answer = input('Input server password: ')
	rt = random.randint(0, 10)
	c_1 = 'BMW'
	c_2 = 'Audi'
	c_3 = 'Lada'
	c_4 = 'Skoda'
	c_5 = 'Nissan'
	c_6 = 'Toyota'
	c_7 = 'Subaru'

	if pass_answer != server_password:
		print('The password does not match...')
		time.sleep(rt)
		
		if pass_answer != server_password:
			print('The password does not match...')
			time.sleep(rt)
			pass_answer = input('Input server password: ')
			if pass_answer == server_password:
				print('Hacking carried out.')
				print('A competitor {} will no longer influence your company.'.format(c_1))
				print('Did they find your break-in? We will know in 10 seconds....')
			elif pass_answer != server_password:
				print('The server is too secure. If you try to hack the server for the 4th time, your hacking attempt will be detected with a 100% probability.')
				print('Server-request: 177.181.101.237. User: admin. Password: ******************. Acces denied.')
				print('Did they find your break-in? We will know in 10 seconds...')
		elif pass_answer == server_password:
			print('Hacking carried out.')
			print('A competitor {} will no longer influence your company.'.format(c_1))
			print('Did they find your break-in? We will know in 10 seconds....')
	elif pass_answer == server_password:
		print('Hacking carried out')
		print('Did they find your break-in? We will know in 10 seconds....')
		print('A competitor {} will no longer influence your company.'.format(c_1))
	return None