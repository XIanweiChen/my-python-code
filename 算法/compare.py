import numpy as np
a = [1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45];
b = [4, 5, 1, 2, 36, 5, 6, 7,7];
c =list(np.random.randint(0,1000,size=30));
# print(a[:5]);
# print(a[5:]);
print((c));
def MergeSort(lists):
    if len(lists) <= 1:
        return lists;
    middle = len(lists) // 2;
    left = MergeSort(lists[:middle]);
    right = MergeSort(lists[middle:]);
    return Merge(left,right);

def Merge(left,right):
	i, j=0,0;
	result = [];
	while i<len(left) and j<len(right):
		if left[i] < right[j]:
			result.append(left[i]);
			i = i + 1;
		else:
			result.append(right[j]);
			j = j + 1;
	# Add the rest.
	result = result + list(left[i:]);
	result = result + list(right[j:]);
	return result;

print(MergeSort(c));