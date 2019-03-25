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

m1 = People('m1',['w1','w2','w3'])
m2 = People('m2',['w1','w3','w2'])
m3 = People('m3',['w1','w3','w2'])
man = [m1,m2,m3]

w1 = People('w1',['m2','m1','m3'])
w2 = People('w2',['m1','m2','m3'])
w3 = People('w3',['m3','m2','m1'])
woman = [w1,w2,w3]

# hashlistsman = makeHashlists1(man)
# hashlistswoman = makeHashlists1(woman)
hashlistspeople = makeHashlists1(man+woman)
print(hashlistspeople)
# print(man[0].getName(),man[0].getLovepeoples(0))

size = 3
pair = []
result = {}
 
# first turn
for i in range(2):
	# if i == 0 :
		result[man[i].getLovepeoples(0)]=man[i].getName()
		pair.append(man[i].getName())
		pair.append(man[i].getLovepeoples(0))
		# print(result)
		# print(man[i].getLovepeoples(0))
	# else:
		if (man[i].getLovepeoples(0) in pair) :  # 这个男的所喜欢的女孩是否有男盆友了
			currentwomen=hashlistspeople[man[i].getLovepeoples(0)]  #这个男的所喜欢的女孩
			print(currentwomen.Lovepeoples()) 		#这个男的所喜欢的女孩对各个男生的好感度
			print(man[i].getName(),result[currentwomen.getName()])
			rst = whoismorepopular(man[i].getName(),result[currentwomen.getName()],currentwomen)
			result[currentwomen.getName()] = rst
			print(result)
			# print(result[man[i].getLovepeoples(0)])
			# print(hashlists1[result[man[i].getLovepeoples(0)]].getLovepeoples(0))