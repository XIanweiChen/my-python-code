A = [18,17,19,6,11,21,23,15]

def Maximum_increasing_subset(A):
	A.insert(0,0)
	dp = {}
	dp[0] = 0
	for i,inum in enumerate(A):
		for j,jnum in enumerate(A[:i]):
			if inum > jnum:
				dp[i] = dp[j]+1

	print(dp)
	print("最大递增子集个数为：",max(dp.values()))

Maximum_increasing_subset(A)
