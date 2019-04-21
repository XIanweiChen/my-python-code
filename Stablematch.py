class People:

	def __init__(self,name,lovepeoles):
		self.name = name
		self.lovepeoles = lovepeoles
	def getName(self):
		return self.name
	def getLovepeoples(self,num):
		return self.lovepeoles[num]
	def Lovepeoples(self):
		return self.lovepeoles
def makeHashlists1(list1):
	hashlists1 = {}
	size = len(list1)
	for x in range(size):
		hashlists1[list1[x].getName()] = list1[x]

	return hashlists1

def whoismorepopular(name1,name2,w):
	lists = w.Lovepeoples() 
	r1 = lists.index(name1)
	r2 = lists.index(name2)
	if(r1>r2):
		return name2
	else:
		return name1


def stablematch(man,woman,size):
	pair = []
	result = {}
	 
	hashlistspeople = makeHashlists1(man+woman) #reate a hash list

	while len(pair)<2*size :
		for turn in range(size) :
			for i in range(size):
				if (man[i].getLovepeoples(turn) in pair) :  # 这个男的所喜欢的女孩是否有男盆友了
					currentwomen=hashlistspeople[man[i].getLovepeoples(turn)]  #这个男的所喜欢的女孩
					# print(currentwomen.Lovepeoples()) 		#这个男的所喜欢的女孩对各个男生的好感度
					# print(man[i].getName(),result[currentwomen.getName()])
					rst = whoismorepopular(man[i].getName(),result[currentwomen.getName()],currentwomen)
					result[currentwomen.getName()] = rst
				else:
					result[man[i].getLovepeoples(turn)]=man[i].getName()
					pair.append(man[i].getName())
					pair.append(man[i].getLovepeoples(turn))

				# print('result=',result)
				# print(len(pair))

	return result


#输入数据
# size = 3

# m1 = People('m1',['w1','w2','w3'])
# m2 = People('m2',['w1','w3','w2'])
# m3 = People('m3',['w1','w3','w2'])
# man = [m1,m2,m3]

# w1 = People('w1',['m2','m1','m3'])
# w2 = People('w2',['m1','m2','m3'])
# w3 = People('w3',['m3','m2','m1'])
# woman = [w1,w2,w3]

size = 4

m1 = People('m1',['w1','w2','w3','w4'])
m2 = People('m2',['w1','w3','w2','w4'])
m3 = People('m3',['w1','w3','w2','w4'])
m4 = People('m4',['w3','w2','w1','w4'])
man = [m1,m2,m3,m4]

w1 = People('w1',['m2','m1','m3','m4'])
w2 = People('w2',['m1','m2','m3','m4'])
w3 = People('w3',['m3','m2','m1','m4'])
w4 = People('w4',['m4','m1','m3','m2'])
woman = [w1,w2,w3,w4]


print(stablematch(man,woman,size))