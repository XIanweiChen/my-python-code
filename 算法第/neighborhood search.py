import copy

class Item:
	"""docstring for Item"""
	def __init__(self,weight,value,decision = 0):
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
	def PutIntoKnapsack(self,item):
		self.weight = self.weight - item.getWeight();
		# item.makeDecision(num);
	def release(self,num):
		self.weight = self.weight + num;


#find find Highest Relative
def findHighestRelative(arys):
	goal = 0
	if(len(arys) != 1):
		for i in range(1,len(arys)):
			# print(i);
			if (arys[i].getRelative() > arys[goal].getRelative()):
				# print("change");
				goal = i;
	
	return goal;


#calculate total value
def totalValue(item):
	result = 0
	for i in item:
		if i.getResult()!=0:
			result = result + i.getValue();
	return  result;

# 1.把一个物品从一个包放到另一个包
def putIntoAnother(last,now,item,num):
	# for x in range(0,len(arys)):
	# 	if (x+1) == item.getResult():
	# 		continue;
	# 	elif (item.getWeight() < J[x].getCurrentWeight()):
	# 		J[x].PutIntoKnapsack(item,x+1);
	# 		# print(J[x].getCurrentWeight());
	# 		return True;
	# return False;
	last.release(item.getWeight());
	now.PutIntoKnapsack(item,num);


# 把物品从包中拿掉
def Remove(item,arys):
	arys[item.getResult()-1].release(item.getWeight());
	item.makeDecision(0);

# 把物品放入包中
def Putinto(numofP,arys,item):
	arys[numofP-1].PutIntoKnapsack(item,numofP+1)




# def neighborhoodSolutions2(arys,item):
# 	value = 0;
# 	for i in arys:
# 		if i.getResult()!=0:
# 			Remove(arys,item);
# 			if totalValue(item) > value:
# 				pass
# 初始化item
i1 = Item(4,9);
i2 = Item(5,5);
i3 = Item(3,8);
# 初始化knapsack
k1 = Knapsack(10);
k2 = Knapsack(6);
k3 = Knapsack(4);

I = [i1,i2,i3];   			#array of item
J = [k1,k2,k3];		   #array of knapsack


i1.makeDecision(0);
i2.makeDecision(0);
i3.makeDecision(0);

R = copy.deepcopy(I);

def PrintResult(arys):
	i = 1;
	for x in arys:
		print("item"+str(i)+" is in knapsack:",x.getResult());
		i=1+i;

def isFeasible(knapsack):
	result = True;
	for i in knapsack:
		if i.getCurrentWeight() < 0:
			result = False;
	return result;

def ok(Item):
	R = copy.deepcopy(J);
	for i in Item:
		if i.getResult()!=0:
			R[i.getResult()-1].PutIntoKnapsack(i);

	result = True;
	for i in R:
		# print(i.getCurrentWeight());
		if i.getCurrentWeight() < 0:
			result = False;
	return result;



def Operation(item,knapsack):
	value = totalValue(item);
	result = [];
	for i in item:
		print("______");
		temp = i.getResult();
		for j in range(0,len(knapsack)):
			i.makeDecision(j);
			print(totalValue(item));
			if ok(item) == True:
				if totalValue(item) >= value:
					value = totalValue(item);
				else:
					i.makeDecision(temp);
			else:
					i.makeDecision(temp);
		tempitem = copy.deepcopy(item);	 #拷贝一份现在的状态
		result.append(tempitem);	
		i.makeDecision(temp)	#还原
	goal = item;
	for i in result:
		# print(totalValue(i));
		if totalValue(i) >= value:
			value = totalValue(i);
			goal = i;
	return goal;

# last = I;
# while True:
# 	now = Operation(last,J);
# 	if totalValue(now) == totalValue(last):
# 		# print(totalValue(now));
# 		PrintResult(now);
# 		break;
# 	last =now;
# 	Operation(last,J);
	
# print(ok(I));

a = Operation(I,J);
# PrintResult(a);
b = Operation(a,J);
# PrintResult(b);
# print(isFeasible(J));
# print(k3.getCurrentWeight());
c = Operation(b,J);
# PrintResult(c);
d = Operation(c,J);
# print(totalValue(c) == totalValue(d));
# b = Operation(a,J);
# print(Operation(I,J));
# print(totalValue(a));


# Remove(i3,J);
# print(i3.getResult());
# Putinto(2,J,i3);
# print(i3.getResult());