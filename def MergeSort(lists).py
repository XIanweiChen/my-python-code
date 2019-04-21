import numpy as np
import time
import matplotlib.pyplot as plt
def createRandomList(range,size):
    return list(np.random.randint(0,range,size));

def bubble_sort(nums):
    for i in range(len(nums) - 1):  # time of for loop
        for j in range(len(nums) - i - 1):  
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

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

def bubble_sort_times(r,s):     #r is range,s is size
    a =createRandomList(r,s);
    start = time.time();
    for i in range(10):
        bubble_sort(a);
    end = time.time();
    return (end - start)/10

def MergeSort_times(r,s):
    a =createRandomList(r,s);
    start = time.time();
    for i in range(10):
         MergeSort(a);
    end = time.time();
    return (end - start)/10

#r is range,s is size
r=1000;
s=500;

# Initializing data on X axis and Y axis
x=range(10,s,10);
y1=[];
y2=[];
for i in range(10,s,10):
    y1.append(bubble_sort_times(r,i));
    y2.append(MergeSort_times(r,i));

# plot
plt.figure(num="compare",figsize=(8,6));
plt.plot(x,y1,color="red",label="Bubble Sort");
plt.plot(x,y2,color="blue",label="Merge Sort");
plt.ylabel("second");
plt.xlabel("lists length");
plt.legend()
plt.show();

