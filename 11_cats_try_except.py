print('How many cats do you have?')
numCats = input()
try:
	if int(numCats) >=4:
		print('That is a lot of cats!')
	else:
		print('You need more cats...')
except ValueError:
	print('You did not enter a number...')
