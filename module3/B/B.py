sequence = []
strl = input()
number = int(strl)

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
			length = len(temp)/2

			for i in range(int(length), len(temp) - 1):
				if temp[i] > temp1[i]:
					sequence.append('dec')
					number += 1
					break
				if temp[i] < temp1[i] or len(temp1) < len(temp):
					sequence.append('inc')
					number -= 1
					break
		else:
			number -= 1
			sequence.append('inc')
			
sequence.reverse()
for i in sequence:
	print(i)