def findapeak(num) : 
	start = 0
	end = len(num)-1
	while (start+1<end):
		mid = start+(end-start)//2
		if (num[mid]>=num[mid+1] & num[mid]>=num[mid-1]):
			return num[mid]
		elif (num[mid] < num[mid-1]):
			end = mid
		else:
			start = mid
	if ((start == 0 | num[start] >= num[start - 1]) & num[start] >= num[start + 1]) :
		return num[start]

	elif ((end == length - 1 | num[end] >= num[end + 1]) & num[end] >= num[end - 1]) :
		return num[end]
	else :
		return -1;


num = [3,5,23,5,2,3]
print(findapeak(num))