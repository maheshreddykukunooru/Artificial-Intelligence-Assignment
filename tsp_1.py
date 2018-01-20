import random
import math
import numpy as np
from copy import deepcopy

citiesDistance = {}
crossOverProbability = 0.8
mutationProbability = 0.8
iterations = 0
f = open('./final/sahara.tsp','r')

flag1=0
for line in f:
	line = line[:-1]
	if line!='EOF':
		if flag1==1:
			# print line
			row = line.split(' ')
			citiesDistance[int(row[0])-1] = {'x':float(row[1]),'y':float(row[2])}

	if line == 'NODE_COORD_SECTION':
		flag1=1 


def pathDistance(path):
	length = len(path)
	dist = euclidianDistance(citiesDistance[path[0]],citiesDistance[path[length-1]])
	for i in range(1,len(path)):
		dist+= euclidianDistance(citiesDistance[path[i]],citiesDistance[path[i-1]])
	return dist


def euclidianDistance(node1, node2):
	return math.sqrt((node1['x']-node2['x']) ** 2 + (node1['y']-node2['y']) ** 2)

populationSize = 30
totalCities = len(citiesDistance)

population = []

while len(population)<populationSize:
    temp = range(0,totalCities)
    random.shuffle(temp)
    population.append(temp)


globalMinDistance = 9999999999
globalMinPath = []
curMinDistance = 9999999999
curMinPath = []

for each in population:
	dist = pathDistance(each) 
	if curMinDistance > dist:
		curMinDistance = dist
		curMinPath = deepcopy(each)

if curMinDistance < globalMinDistance:
	globalMinPath = deepcopy(curMinPath)
	globalMinDistance = curMinDistance


flag=1
count=0
while flag==1:
	iterations+=1
	# print "########################################\n"
	print "Iteration ",iterations," minDistance " ,globalMinDistance
	count+=1
	fitness_values = []
	sumValues = 0.0


	#### Computing the fitness values to build the roulette wheel
	for parentIndex in range(0,populationSize):
		dist = pathDistance(population[parentIndex]) 
		fitness_values.append(1/dist)
		sumValues += 1.0/dist

	for i in range(0,populationSize):
		fitness_values[i] = fitness_values[i]/sumValues

	for i in range(1,populationSize):
		fitness_values[i]+=fitness_values[i-1]

	selectedParents = []



	### Selecting the parents based on the roulette wheel
	selectedParents.append(curMinPath)
	selectedParents.append(globalMinPath)

	for i in range(2,populationSize):
		rouletteNumber = random.uniform(0,1)
		for j in range(0,populationSize):
			if rouletteNumber < fitness_values[j]:
				selectedParents.append(population[j])
				break

	population = deepcopy(selectedParents)

	crossOverArray = []
	for i in range(0,populationSize):
		if random.uniform(0,1) < crossOverProbability:
			crossOverArray.append(i)
	random.shuffle(crossOverArray)

	if len(crossOverArray)%2==1:
		del(crossOverArray[-1])
	i=0


	###### 1 Order Crossover
	while i < len(crossOverArray):

		start = random.randint(0,totalCities-1)
		end = random.randint(0,totalCities-1)

		if start > end:
			tempVar = start
			start = end
			end = tempVar
		temp = []
		citiesTemp = []
		remaining = []
		for k in range(0,totalCities):
			citiesTemp.append(k)

		for j in range(start,end+1):
			temp.append(population[crossOverArray[i]][j])
			citiesTemp.remove(population[crossOverArray[i]][j])

		for j in range(end+1,totalCities):
			if population[crossOverArray[i+1]][j] in citiesTemp:
				citiesTemp.remove(population[crossOverArray[i+1]][j])
				remaining.append(population[crossOverArray[i+1]][j])

		for j in range(0,end+1):
			if population[crossOverArray[i+1]][j] in citiesTemp:
				citiesTemp.remove(population[crossOverArray[i+1]][j])
				remaining.append(population[crossOverArray[i+1]][j])			

		endTemp = end+1
		while endTemp < totalCities and len(remaining)!=0:
			temp.append(remaining[0])
			del(remaining[0])
			endTemp+=1

		crossOverChild1 = remaining + temp

		temp = []
		citiesTemp = []
		remaining = []
		for k in range(0,totalCities):
			citiesTemp.append(k)

		for j in range(start,end+1):
			temp.append(population[crossOverArray[i+1]][j])
			citiesTemp.remove(population[crossOverArray[i+1]][j])

		for j in range(end+1,totalCities):
			if population[crossOverArray[i]][j] in citiesTemp:
				citiesTemp.remove(population[crossOverArray[i]][j])
				remaining.append(population[crossOverArray[i]][j])

		for j in range(0,end+1):
			if population[crossOverArray[i]][j] in citiesTemp:
				citiesTemp.remove(population[crossOverArray[i]][j])
				remaining.append(population[crossOverArray[i]][j])	

		endTemp = end
		while endTemp < totalCities and len(remaining)!=0:
			temp.append(remaining[0])
			del(remaining[0])
			endTemp+=1

		crossOverChild2 = remaining + temp

		if pathDistance(crossOverChild1) < population[crossOverArray[i]]:
			population[crossOverArray[i]] = crossOverChild1
		if pathDistance(crossOverChild2) < population[crossOverArray[i+1]]:
			population[crossOverArray[i+1]] = crossOverChild2

		i+=2


	#### Swap mutation
	for i in range(0,populationSize):
		if random.uniform(0,1) < mutationProbability:

			mutations = set()
			while len(mutations)<2:
				mutationTemp = random.randint(0,totalCities-1)
				mutations.add(mutationTemp)
			mutationsList = list(mutations)

			tempValue = population[i][mutationsList[0]]
			population[i][mutationsList[0]] = population[i][mutationsList[1]]
			population[i][mutationsList[1]] = tempValue



	#### Calculating minimum for this iteration
	for each in population:
		dist = pathDistance(each) 
		if curMinDistance > dist:
			curMinDistance = dist
			curMinPath = deepcopy(each)

	if curMinDistance < globalMinDistance:
		globalMinPath = deepcopy(curMinPath)
		globalMinDistance = curMinDistance
		count = 1

	if count==1000:
		flag=0

	
print "Iteration ",iterations," minDistance " ,globalMinDistance










