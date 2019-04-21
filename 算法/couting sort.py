

# 百度找的
def couting_sort_baidu(a):
	n=len(a)
	b=[None]*n	#创建于a等长的list
	for i in range(n):
		# 每次取一个值放入数组
		p=0		#定位，开始位置
		q=0		#相同元素个数
		for j in range(n):
			if a[j]<a[i]:	#如果有比他小的就向后移一位
				p+=1
			elif a[j]==a[i]:	#检测值相同的元素
				q+=1
		for k in range(p,p+q):	#放入结果list
				b[k]=a[i]

	print(b)

# 自己写的
def couting_sort(a):
n=max(a)
b=[0]*n	
for i in a:
	b[i-1]=b[i-1]+1;

for i in range(n):
	if b[i] != 0:
		print(i+1)



couting_sort([1,21,32,21,27])

couting_sort([1,21,32,21,27])



