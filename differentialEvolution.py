import random
import math
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt



def ackley(x,y):
    return -20. * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(0.5 * (math.cos(2. * math.pi * x) + math.cos(2. * math.pi * y)))


mutationFactor = 0.5
crossOverProbability = 0.3
iteration=0
totalIterations = 100
lowerBound = -4.9
upperBound = 4.9
populationSize = 10
resultArray = []

while iteration<totalIterations:

	X = []
	Y = []
	for i in range(0,populationSize):
		X.append(random.uniform(lowerBound, upperBound))
		Y.append(random.uniform(lowerBound, upperBound))

	flag=1
	count=0
	while flag==1:

		for i in range(0,populationSize):
			vectors = random.sample(range(0, populationSize), 3)
			tempFlag=1
			while tempFlag ==1:
				if vectors[0]==i or vectors[1]==i or vectors[2]==i:
					vectors=[]
					vectors = random.sample(range(0, populationSize), 3)
				else:
					tempFlag=0


			donorX = X[vectors[0]]+mutationFactor*(X[vectors[1]] - X[vectors[2]])	#Mutation
			donorY = Y[vectors[0]]+mutationFactor*(Y[vectors[1]] - Y[vectors[2]])	#Mutation

			R = random.randint(0,3)
			r = random.uniform(0,1)

			newX = X[i]
			newY = Y[i]

			if random.uniform(0,1)<crossOverProbability or R==0:
				newX = donorX
			if random.uniform(0,1)<crossOverProbability or R==1:
				newY = donorY

			if ackley(newX,newY) < ackley(X[i],Y[i]):
				X[i] = newX
				Y[i] = newY
				count = 1

			count+=1
			if count==100:
				flag=0

	ansX = 0
	ansY = 0
	finalResult = ackley(X[0],Y[0])
	for i in range(1,populationSize):
		if ackley(X[i],Y[i]) < finalResult:
			finalResult = ackley(X[i],Y[i])
			ansX = X[i]
			ansY = Y[i]
	
	iteration+=1
	print "Iteration ", iteration, " Min Value: ", finalResult , " x ", ansX, " y ", ansY
	resultArray.append(finalResult)
	# break

a = ('1')
a = list(a)
for i in range(2,101):
	a.insert(i, str(i))
a = tuple(a)
y_pos = np.arange(100)
performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, resultArray, alpha=0.5)
plt.xticks(y_pos, a)
plt.xticks(rotation=90,fontsize=8)

plt.ylabel('Min Value')
plt.xlabel('Iteration')
plt.title('Differential Evolution Algorithm')
 
plt.show()


