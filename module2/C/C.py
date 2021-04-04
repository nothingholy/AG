class MinHeap:
	def __init__(self):
		pass

	def add(self, key, value):
		pass

	def set(self, key, value):
		pass

	def search(self, key):
		pass

	def delete_elem(self, key):
		pass

	def min(self):
		pass

	def max(self):
		pass

	def extract(self):
		pass

	def print(self):
		pass




flag = True
heapmin = MinHeap()
while flag:
	try:
		strl = input()
		temp = strl.split(' ', 2)

		if strl == '':
			continue

		if len(temp) == 3:
			if temp[0] == 'add':
				heapmin.add(int(temp[1]), temp[2])
			elif temp[0] == 'set':
				heapmin.set(int(temp[1]), temp[2])
			else:
				print('error')
		elif len(temp) == 2:
			if temp[0] == 'search':
				heapmin.search(int(temp[1]))
			elif temp[1] == 'delete':
				heapmin.delete_elem(int(temp[1]))
			else:
				print('error')
		elif len(temp) == 1:
			if temp[0] == 'min':
				heapmin.min()
			elif temp[0] == 'max':
				heapmin.max()
			elif temp[0] == 'extract':
				heapmin.extract()
			elif temp[0] == 'print':
				heapmin.print()
			else:
				print('error')
		else:
			print('error')


	except Exception:
		flag = False