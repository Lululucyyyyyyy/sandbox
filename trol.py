def start():
	print('===== Welcome to the worlds most boring game =====')
	print('===== To proceed, press enter =====')
	random = input()
	print('===== Ok now that you have officially began, please type in qwertyuiopasdfghjklzxcvbnm =====')
	if input() == 'qwertyuiopasdfghjklzxcvbnm':
		pass
	else:
		print(' omg I cant believe you failed already good job.' )
		exit()
	print('===== Congrats on completing the first task. Your hp is now 100. Power 200. and coins 0. =====')
	x = input()
	print('===== You are poor. Please choose a way to earn money =====')
	x = input()
	print(' (1) work (2) spending is earning (3) lotteryyyyy (4) why should I even care ')
	my_input = input()
	if my_input == 1:
		print('===== You diligent soul you would never survive in the real world =====')
		x = input()
		print('game over you are too nice')
	elif my_input == 2:
		print('===== Thats the spirit, except it wont get you anywhere =====')
		x = input()
		print('game over you are too optimistic')
	elif my_input == 3:
		print('===== Good job go big or go home right? =====')
		x = input()
		print('in this case you go home game over')
	else:
		print('===== It seems like you dont care about this game and neither do I=====')
		x = input()
		print('game over go be productive')
	exit()

start() 
