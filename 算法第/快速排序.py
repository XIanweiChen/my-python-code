
def quickSort(array):
	if len(array)>=2:
		base = array[0]
		left,right=[],[]
		array.remove(base)
		for num in array:
			if num > base:
				right.append(num)
			else:
				left.append(num)
		print(left+["",base,""]+right)
		return quickSort(left)+[base]+quickSort(right)
	else:
		return array
		
		












array1 = [5,2,11,9]
print(quickSort(array1))