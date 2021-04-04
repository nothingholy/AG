from collections import Counter

sequence = []
sequence1 = []
strl = input()
number = int(strl)
number1 = number

while number != 0:
	if number % 2 == 0:
		number = number / 2
		sequence.append('dbl')

	if number == 1:
		number -= 1
		sequence.append('inc')

	if number % 2 == 1:
		temp = bin(int(number + 1))[2:]
		temp1 = bin(int(number - 1))[2:]

		if temp.count('1') < temp1.count('1'):
			sequence.append('dec')
			number += 1
		elif temp.count('1') == temp1.count('1'):
			if len(temp) < len(temp1):
				number += 1
				sequence.append('dec')
			elif len(temp) > len(temp1):
				number -= 1
				sequence.append('inc')
			else:
				print('jopa')
				index = 0
				for i in temp[::-1][3:]:
					if i == 1:
						index += 1
				if index <= 2:
					sequence.append('inc')
					number -= 1
				else:
					sequence.append('dec')
					number += 1
		else:
			number -= 1
			sequence.append('inc')

while number1 != 0:
	if number1 % 2 == 0:
		number1 = number1 / 2
		sequence1.append('dbl')

	if number1 == 1:
		number1 -= 1
		sequence1.append('inc')

	if number1 % 2 == 1:
		temp = bin(int(number1 + 1))[2:]
		temp1 = bin(int(number1 - 1))[2:]

		if temp.count('1') < temp1.count('1'):
			sequence1.append('dec')
			number1 += 1
		else:
			number1 -= 1
			sequence1.append('inc')
			
sequence.reverse()
sequence1.reverse()

print('1: ', len(sequence), '2: ', len(sequence1))
if len(sequence1) < len(sequence):
	for i in sequence1:
		print(i)
else:
	for i in sequence:
		print(i)