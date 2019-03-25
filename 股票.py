def findbest(input):
	# best_couple = ""
	if len(input) <= 1:
		return 0,""
	mid = len(input)//2
	left = input[:mid]
	right = input[mid:]

	# print(left,right)
	best_couple=""

	best_left = findbest(left)[0]
	best_right = findbest(right)[0]
	best_cross = max(right) - min(left)
	if max(best_cross,best_right,best_left) == best_cross:
		best_couple = (str(max(right))+'-'+str(min(left)))
		# print(best_couple)


	# if left == input[:len(input)//2]:
	# 	print(max(right),'-',min(left))
	# print([max(best_cross,best_right,best_left),max(right),min(left)])
	# print([max(best_cross,best_right,best_left),max(right),min(left)][-1]  )
	# print(max(right),min(left))
	return max(best_cross,best_right,best_left),best_couple



A = [2,5,8,18,12,9,16]
print(findbest(A))
