
### Travelling Salesman Problem

Here we use genetic algorithm to find the path that covers all the cities given using least cost. At every point, we choose the best paths among the set and pass the genes to the off springs and so on.

At first, paths were generated randomly using random.shuffle() among the city indices as each path is a permutation of the total cities. Population size of 30 was taken. A roulette is computed using the inverse of the cost for each path. Generally, area in a roulette is proportional to the cost of the path if our goal is to find the maximum cost path. Here we are looking for a path which has the least value, which means we need to consider inverse of the path cost while building the roulette to make selection.

Then among the 30 paths, a decision has to be made whether it has to be selected for crossover or not. So a random number is generated and compared with crossover probability. This way we get n out of 30 paths which are ready for crossover.

In this assignment, order 1 crossover and Partially Mapped Crossover(PMX) are implemented. After crossover, the next step is mutation where I implemented Scramble mutation, after which the least cost is calculated in the population after the recombination methods to see if it is less than what we've obtained till now. We use the same termination condition as we've used for the above part, but the number was increased to 5000 for better results.

**Order 1 crossover and PMX, scramble mutation were discuseed in class.**

Analysis: In the beginning, the algorithm used to terminate at a stage where every path in the population is same. To overcome this problem, I did something like adding global minimum path found till now, local minimum path of the last population and 2 mutations of the global minimum path to the selected 30 paths always. This way, we ensure that we've 4 paths which lead to better results quickly.

I observed that for the given test cases, sahara.tsp terminated in no time with a minimum value of about 28000 where as it fails to terminate in a similiar pace for the bigger test cases. It ran about one hour with the distance went upto 400000 starting from 1500000 for uy734.tsp. Same is the case with the other bigger file.

According to me, there is still a possibility of optimizing the code insted of code running for about an hour. I think the problem is with the crossover technique which produces off springs needs to have something involved with the distance between cities rather than just considering merging the values from two parents.

I found this way of crossover on the web, where a random city is selected and it's index is found in both the parents, and then the cities present next to that city are taken and the distance is calculated between the city selected and these two. The one with minimum is added next to the offspring and then this city is considered to find the next cities till the parents get emptied.

This way, the solution was found exponentially faster than the one's previous. The solution for the bigger files was found in less than a minute with the number of iterations too a lot lesser than the former methods. I think this method of crossover where the off springs are generated considering the distances is the best technique in these kind of problems.

**Run time:  Sahara.tsp -- 10seconds to reach the minimum value
             uy734.tsp -- minimum value a lot lesser than the other methods where PMX and 1 order crossover are used, the value went upto 95k in less than 90seconds whereas it took 1 hour to reach a value of 400,000 in the former cases.

I've named this file as best.py where the crossover method was adopted from the web which was not discussed in class.**
