import sys
import os
def findbest(input,cout=0):
	best_couple = ""
	if len(input) <= 1:
		return 0
	mid = len(input)//2
	left = input[:mid]
	right = input[mid:]
	best_left = findbest(left)
	best_right = findbest(right) 
	best_cross = max(right) - min(left)
	if max(best_cross,best_right,best_left) == best_cross:
		best_couple = (max(right),'-',min(left))
	if len(input) == cout:
		print(max(right),'-',min(left))
		print(best_couple)
	return max(best_cross,best_right,best_left)


A = [2,5,18,12,9,16,11]
print(findbest(A,len(A)))
# print(max(A))