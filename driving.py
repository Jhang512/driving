country = input('What is your nationality: ')
age = input('How old are you: ')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('You can learn driving')
	else:
		print('You cannot learn driving')