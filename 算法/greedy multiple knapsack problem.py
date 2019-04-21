import copy

class Item:
	"""docstring for Item"""
	def __init__(self,weight,value,decision = "0"):
		self.weight = weight;
		self.value = value;
		self.decision = decision;
	def getWeight(self):
		return self.weight;
	def getValue(self):
		return self.value;
	def getRelative(self):
		return self.value/self.weight;
	def getResult(self):
		return self.decision;
	def makeDecision(self,decision):
		self.decision = decision;
class Knapsack:
	"""docstring for ClassName"""
	def __init__(self, weight):
		self.weight = weight;
	def getCurrentWeight(self):
		return self.weight;
	def PutIntoKnapsack(self,item,num):
		self.weight = self.weight - item.getWeight();
		item.makeDecision(num);

#find Highest Relative
def findHighestRelative(arys):
	goal = arys[0];
	for i in I:
		if (i.getRelative() > goal.getRelative()):
			goal = i;
	return goal;
	# goal = 0
	# for i in range(1,len(arys)):
	# 	# print(i);
	# 	if (arys[i].getRelative() > arys[goal].getRelative()):
	# 		# print("change");
	# 		goal = i;
	# return arys[goal];

# 初始化item
i1 = Item(4,9);
i2 = Item(5,5);
i3 = Item(3,8);
# 初始化knapsack
k1 = Knapsack(10);
k2 = Knapsack(6);
k3 = Knapsack(15);


I = [i1,i2,i3];   			#array of item
J = [k1,k2];		   #array of knapsack



R = copy.copy(I);
def PrintResult(arys):
	i = 1;
	for x in arys:
		print("item"+str(i)+" is in knapsack:",x.getResult());
		i=1+i;


def Putinto(arys,item):
	for x in range(0,len(arys)):
		if (item.getWeight() < J[x].getCurrentWeight()):
			J[x].PutIntoKnapsack(item,x+1);
			# print(J[x].getCurrentWeight());
			return True;
	return False;

# print(Putinto(J,findHighestRelative(I)));
# print(J[0].getCurrentWeight());

while (len(I)!=0):
	Putinto(J,findHighestRelative(I));
	I.remove(findHighestRelative(I));
PrintResult(R);