list = [9, 10 , 50, 33, 1, 2, 8, 7, 67, 4, 6, 101, 5, 0]
largest_number_so_far = -100
for iter in list:
	if iter > largest_number_so_far:
		largest_number_so_far = iter
print(largest_number_so_far)