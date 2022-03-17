
# if & for pratice 1

# for i in range(1, 101):
# 	if not i%2 or not i%11:
# 		print(i, end= ' ')

###############################


a = [22,1,3,4,7,98,21,55,87,99,19,20,45]
max_num = a[0]
min_num = a[0]
sum_num = 0

for i in a:
	if i > max_num:
		max_num = i
	if i < min_num:
		min_num = i
	sum_num += i

print(max_num, min_num, int(sum_num/len(a)))