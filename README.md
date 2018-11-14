# A Genetic Algorithm for Images
# Overview
Genetic Algorithms are a form of Machine Learning that use the process of Natural Selection to generate an ideal solution to a problem. The flexibility of Genetic Algorithms make it ideal for situations that are NP-Hard or not representable by other forms of Machine Learning. For a Genetic Algorithm to work, the only necessary components are that solutions must be representable in a way that can be recombined and that there must be a way to quantifiably say how ‘good’ a solution is.
# Steps to a generic Genetic Algorithm
Initialization
A population of possible solutions is generated
In most cases, the population is randomly generated, but it is possible to start the population with already known solutions so the algorithm can further optimize them.
Fitness Calculation
Each solution in the population has a ‘fitness’ score computed. This score is based on how correct the solution is.
Note that the correctness of the solution must be on a quantifiable spectrum, not simply yes or no
Fitness can be calculated in any number of ways, so long as it is a reliable measure of how ‘good’ the solution is
Many algorithms can calculate error using the concept of Mean Squared Error (Calculate error between the solution and the ideal, then square it). Squaring the error allows for greater distinction between ‘good’ and ‘not good’ items for when the algorithm is picking solutions
Create a New Population - 3 Steps to creating the new generation
Selection:
Pick which solutions should be used for breeding. This can be done in many different ways, but usually done by randomly picking individuals with a weight probability. Individuals with more fitness are more likely to be picked for breeding. An ‘elite population’ can also be implemented where the top few solutions are automatically selected for breeding, ensuring that the best solutions are not discarded by chance.
Cross Over:
The solutions selected for breeding are crossed together in almost the same way that it occurs in Prophase-1 of meiosis. Two ‘parent’ solutions that were replace parts of their own solution with part of the other parent’s solution. You can visualize this as crossing ‘abcd’ and ‘1234’ to create ‘ab34’. The point where the solutions are split is usually picked randomly.
Mutate:
To ensure that the population does not settle into local minima, random mutation is applied to solutions. The process of breeding can make it possible that something necessary for convergence to be discarded if was initialized as part of a poor solution. Mutation allows for genetic variation to exist so that the population does not eventually become homogeneous.
Replace
Discard the previous population and replace it with the new population generated
Repeat steps 2 - 4 until convergence

While very abstract, the takeaway is that Genetic Algorithms follow the steps of Natural Selection almost to the tee. Granted, the digital representation of the population differs, but the key steps of selection, crossing-over, and mutations make Genetic Algorithms able to solve problems not able to be optimized by other means of Machine Learning.

# My Project
	As a challenge, I decided to make my own Genetic Algorithm that starts with a population of randomly generated ‘images’ and converges it towards a final (pre-specified) picture. The videos are compilations of the top rated solution from each generation, over the course of approximately 8,000 generations. Whereas the original image starts out mostly as static, you can see how the algorithm gets closer and closer over time to the checkerboard pattern it was set to converge to. As a bonus, I included a compilation of my algorithm doing the same for a “Creeper” from Minecraft, but the algorithm didn’t run long enough for the image to fully converge.
