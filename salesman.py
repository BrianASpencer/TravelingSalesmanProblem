import math
import random

# Brian Spencer
# CSC 320

# a population is a collection or list of chromosomes
# population = [chromosome0, chromosome1, ..., chromosome9999]
# chromosome has components of path, distance, distance normalized, etc.


class Chromosome:
    path = []
    dist = 0.0

    cityCoords = {
      1: [1,1],
      2: [5,4],
      3: [4,8],
      4: [3,5],
      5: [7,6],
      6: [8,7],
      7: [1,8],
      8: [2,4],
      9: [9,2],
    }

    # constructor
    def __init__(self):
        self.path = random.sample(range(1,10), 9)
        self.dist = self.distance()
        self.fitness = self.evalFitness()


    # calculate distance of a path
    def distance(self):
        dist = 0
        for i in range(0, len(self.path)-1):
            dist = dist + self.calcDist(self.cityCoords[self.path[i]], self.cityCoords[self.path[i+1]])
        dist = dist + self.calcDist(self.cityCoords[self.path[0]], self.cityCoords[self.path[len(self.path)-1]])
        return dist


    def calcDist(self, coord1, coord2):
        dist = 0
        dist = math.sqrt(math.pow(coord1[0] - coord2[0],2) + math.pow(coord1[1] - coord2[1],2))
        return dist

    def evalFitness(self):
        return 46.0/self.dist
    
    def mutate(self):
        roll = random.sample(range(1,1000), 1)
        if roll[0] == 1:
            self.path = random.sample(range(1,10), 9)

def crossover(p1, p2):
    c1 = p1[3:6]
    child = []
    path = []
    cnt = 0
    cnt2 = 0
    for i in range(3, len(p1)+3):
        for j in range(0, len(c1)):
            if p2[i%9] == c1[j]:
                cnt = cnt + 1
        if cnt == 0:
            path.append(p2[i%9])
        cnt = 0
    
    for i in range(0, 9):
        if i < 3:
            child.append(path[i])
        elif i < 6:
            child.append(c1[i-3])
        else:
            child.append(path[i-3])
    
    return child

if __name__ == "__main__":

    #https://new.hindawi.com/journals/cin/2017/7430125/
    
    #def repopulate():

    populationSize = 10000
    generations = 6
    minFitness = 1.0
    population = []
    parents = []
    gen = 0
    
    while (gen < generations):
        for i in range(0, populationSize):
            population.append(Chromosome())
        cnt = 0
        while (cnt < populationSize//2):
            for i in range(0, len(population)):
                if population[i].fitness > minFitness:
                    parents.append(population[i])
                if len(parents) == populationSize//2:
                    break
            cnt = len(parents)

        n = len(parents)
        for i in range(0, len(parents), 2):
            npath = crossover(parents[i].path, parents[i+1].path)
            parents.append(Chromosome())
            parents[n].path = list(npath)
            n = n + 1

        for i in range(0, populationSize//4):
            parents.append(Chromosome())

        gen = gen + 1
        minFitness = minFitness + .1
        population = []
        cnt = populationSize - 1
        while (cnt > 0):
            population.append(parents[cnt])
            parents.remove(parents[cnt])
            cnt = cnt - 1
        population.append(parents[0])
            
    length = 40.0
    pathy = []
    cnt = 0
    for i in range(0, populationSize):
        if population[i].dist < length:
            length = population[i].dist
            pathy = population[i].path    
        oof = population[i].fitness
        if oof >= 1.5001483713921:
            cnt = cnt + 1

    print('Path: ', pathy)
    print('Population size: ', populationSize)
    print('Number of generations: ', gen)
    print('Distance of shortest path: ', length)
    print('Proportion with same distance: ', cnt/len(population))


    #general process
    #1. we choose fittest half of population to compose new population
    #2. we breed them to form children (and add that onto newe population)
    #3. we repopulate with random ones to origninal popualation length
    #4. do at til we got a satisfactory result