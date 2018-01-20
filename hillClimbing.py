import random
import math
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def ackley(x,y):
    return -20 * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)))

iteration=0
resultArray = []

while iteration<100:

	initX = (random.uniform(-5, 5)-0.5)*0.1
	initY = (random.uniform(-5, 5)-0.5)*0.1

	flag=1

	initAckley = ackley(initX,initY)

	productiveStepsCount = 0
	while flag:

		newX = (random.uniform(0,1) - 0.5) * 0.2 + initX
		newY = (random.uniform(0,1) - 0.5) * 0.2 + initY

		newAckley = ackley(newX,newY)

		if newAckley < initAckley:
			intitAckley = newAckley
			productiveStepsCount = 0
		else:
			productiveStepsCount+=1
			if productiveStepsCount == 100:
				flag = 0
		initX = newX
		initY = newY

	print "Iteration " + str(iteration+1) + " Min Value " + str(initAckley), "x ", initX, " y ", initY
	resultArray.append(initAckley)


	iteration+=1

 
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
plt.title('Hill Climbing Algorithm')
 
plt.show()
