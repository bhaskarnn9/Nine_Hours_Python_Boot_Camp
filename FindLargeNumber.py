list = [9, 10 , 50, 33, 1, 2, 8, 7, 67, 4, 6, 101, 5, 0]
i = 0
largest_number_so_far = list[i]
while i < len(list):
	y = list[i]
	if y > largest_number_so_far:
		largest_number_so_far = y
	i +=1
print(largest_number_so_far)