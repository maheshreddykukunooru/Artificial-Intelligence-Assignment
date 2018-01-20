import random
import math
import numpy as np
from copy import deepcopy

citiesDistance = {}
crossOverProbability = 0.9
mutationProbability = 0.4
iterations = 0
f = open('uy734.tsp','r')

flag1=0
for line in f:
	line = line[:-2]
	if line!='EOF':
		if flag1==1:
			# print line
			row = line.split(' ')
			citiesDistance[int(row[0])-1] = {'x':float(row[1]),'y':float(row[2])}

	if line == 'NODE_COORD_SECTION':
		flag1=1 

def euclidianDistance(node1, node2):
	return math.sqrt((node1['x']-node2['x']) ** 2 + (node1['y']-node2['y']) ** 2)



populationSize = 30
totalCities = len(citiesDistance)

def pathDistance(path):
	length = len(path)
	dist = euclidianDistance(citiesDistance[path[0]], citiesDistance[path[length-1]])
	for i in range(1,len(path)):
		dist+= euclidianDistance(citiesDistance[path[i]], citiesDistance[path[i-1]])
	return dist

population = []

while len(population)<populationSize:
    temp = range(0,totalCities)
    random.shuffle(temp)
    population.append(temp)
    # print len(population)

# print population


globalMinDistance = 9999999999
globalMinPath = []
curMinDistance = 9999999999
curMinPath = []

for each in population:
	dist = pathDistance(each) 
	# print dist
	if curMinDistance > dist:
		curMinDistance = dist
		curMinPath = deepcopy(each)
		# print "found lesser value"

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



	#### Selecting the parents using the roulette wheel
	selectedParents = []

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


	###### Selecting the parents for crossover using crossover probability
	for i in range(0,populationSize):
		if random.uniform(0,1) < crossOverProbability:
			crossOverArray.append(i)
	random.shuffle(crossOverArray)

	if len(crossOverArray)%2==1:
		del(crossOverArray[-1])
	i=0


	#### Crossover method adopted from the web where the distances between cities are also considered
	while i < len(crossOverArray):
  		solution = []
  		px = deepcopy(population[i])
  		py = deepcopy(population[i+1])
  		c = px[random.randint(0,len(px)-1)]
		solution.append(c)
		while len(px)>1:
			if px.index(c) == len(px)-1:
				dx = px[0]
			else:
				dx = px[px.index(c)+1]
			if py.index(c) == len(py)-1:
				dy  = py[0]
			else:
				dy = py[py.index(c)+1]
			px.remove(c)
			py.remove(c)

			if euclidianDistance(citiesDistance[c],citiesDistance[dx]) < euclidianDistance(citiesDistance[c],citiesDistance[dy]):
				c = dx
			else:
				c = dy 
			solution.append(c)

		child1 = solution

		solution = []
  		px = deepcopy(population[i])
  		py = deepcopy(population[i+1])
  		# c = px[random.range(len(px))]
  		c = px[random.randint(0,len(px)-1)]
		solution.append(c)
		while len(px)>1:
			if px.index(c) == 0:
				dx = px[-1]
			else:
				dx = px[px.index(c)-1]
			if py.index(c) == 0:
				dy  = py[-1]
			else:
				dy = py[py.index(c)-1]
			px.remove(c)
			py.remove(c)

			if euclidianDistance(citiesDistance[c],citiesDistance[dx]) < euclidianDistance(citiesDistance[c],citiesDistance[dy]):
				c = dx
			else:
				c = dy 
			solution.append(c)

		child2 = solution

		population[i] = deepcopy(child1)
		population[i+1] = deepcopy(child2)



		i+=2



	##### Scramble Mutation
	for i in range(0,populationSize):
		if random.uniform(0,1) < mutationProbability:

			mutations = set()
			while len(mutations)<2:
				mutationTemp = random.randint(0,totalCities-1)
				mutations.add(mutationTemp)
			mutationsList = list(mutations)
			mutationsList.sort()

			start = mutationsList[0]
			end = mutationsList[1]

			while(start<end):
				tempValue = population[i][start]
				population[i][start] = population[i][end]
				population[i][end] = tempValue
				start+=1
				end-=1

	for each in population:
		dist = pathDistance(each) 

		if curMinDistance > dist:
			curMinDistance = dist
			curMinPath = deepcopy(each)

	if curMinDistance < globalMinDistance:
		globalMinPath = deepcopy(curMinPath)
		globalMinDistance = curMinDistance
		count = 1

	if count==500:
		flag=0

	
print "Iteration ",iterations," minDistance " ,globalMinDistance










