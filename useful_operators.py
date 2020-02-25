my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in range(0,25):
	print(num)
print('\n')
for num in range(0,25,1):
	print(num)
print('\n')
for num in range(0,25,2):
	print(num)
print('\n')

index_count = 0
for letter in 'alphabet':
	print('at index {}, letter is {}'.format(index_count, letter))
	index_count +=1

index_count = 0
word = 'alphabet'
for letter in word:
	print(index_coun,tword[index_count])
	index_count +=1

word = 'alphabet'
for letter in enumerate(word):
	print(letter)