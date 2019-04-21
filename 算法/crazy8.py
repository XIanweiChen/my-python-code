import numpy as np


card =["花7","红7","花k","黑1","红8","红6"]

# 根据记录parent卡牌的dict找到parent卡牌
def findcard(parent,first,card):
	include_card = []
	result_card = []
	include_card.append(first)
	for x in include_card:
		if parent[x] != None :
			include_card.append(parent[x])
	for x in sorted(include_card):
		result_card.append(card[x])
	print(result_card)

# 判断是否能够连接
def is_trick(ci,cj):
	result = False
	if ci[0] == cj[0]:
		result = True
	if ci[1] == cj[1]:
		result = True
	if ci[1] =="8":
		result = True
	if cj[1] =="8":
		result = True
	return result

def crazy_eight(card):
	trick = {}			#记录每张牌的相连数
	parent = {}			#记录父节点
	trick[0] = 1
	parent[0] = None
	for i,ci in enumerate(card):
		temp_trick = []
		if i > 0:
			for j,cj in enumerate(card[:i]):
				if is_trick(ci,cj):
					temp_trick.append(trick[j])
				else:
					temp_trick.append(0)
			max_trick = max(temp_trick)
			trick[i] = max_trick + 1
			index_max = np.argmax(temp_trick)
			parent[i] = index_max
			if trick[i] == 1 :		#如果是单张的就把父节点设为None
				parent[i] = None

	
	max_num = max(trick.values())
	print (max_num)
	trans_trick = {v: k for k, v in trick.items()}   #反转stick，找到最大序列的最后一张牌
	first = trans_trick[max_num]
	findcard(parent,first,card)


crazy_eight(card)