#### Artificial Intelligence assignment

### Hill Climbing Algorithm

Here's the implementation of Hill Climbing Algorithm to find the minimum value of Ackley's function. Initial position was randomly chosen, then the next positions were using the following equations

    X' = (rand() – 0.5) * 0.1 + X
    Y' = (rand() – 0.5) * 0.1 + Y

At every point, the value of the function is calculated and checked it with the minimum value which is updated whenever it finds a lesser value. The iteration is terminated when a value minimum than the minimum is not found till now in continuous 100 steps. This process is repeated 100 times and minimum value is found in every iteration.

**Analysis** : Observing the minimum values of 100 iterations, we see that the function reaches the original minimum value of Ackley's function only a handful of times (<10), we see that most of the times, it terminates at a value of 20.

![Hill Climbing Algorithm]('./figure_1.jpeg')

*We can clearly see that, Hill Climbing Algorithm gets struck at a local minimum rather than reaching Global Optimum every time.*


### Differential Evolution Algorithm

In this part, Evolutionary algorithm is used to find the minimum value of Ackley's function starting from a random point.
As the algorithm used was evolutionary, it has the following parts, *reproduction, mutation, evalution and selection*.

Here a total of 20 random points are selected at first, then for every point, three other points are selected which are different from the former and then a mutation is done using,

    Donor vector(V') = v1 + Mutation factor (v2 − v3)  
    where v1,v2 and v3 are three vectors chosen randomly

A random number is generated and compared with Cross Over Probability to check if it is eligible for crossover.
If it is, then the donor vector replaces the original vector and then the Ackley's function is calculated for the new vector.

At every step, we compare the minimum value of the iteration with the minimum found till now, and the program is terminated when the minimum doesn't change till 100 steps.

*Using this algorithm we can observe that, we reach the global optimal value -22.7 obtained at (0,0) almost everytime. So it is clear that it doesn't get struck at local optima's now and then, as it is continuously learning from the previous values as we are generating values from the parents.*

![Evolutionary Algorithm]('./figure_2.jpeg')
