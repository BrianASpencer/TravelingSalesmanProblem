import math
import random

# a population is a collection or list of chromosomes
# population = [chromosome0, chromosome1, ..., chromosome9999]
# chromosome has components of path, distance, distance normalized, etc.


class Chromosome:
    path = []
    dist = 90.0

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
    generations = 5
    minFitness = 1.0
    population = []
    parents = []
    flag = False
    cnt = 0
    for j in range(0, generations):
        for i in range(0, populationSize):
            population.append(Chromosome())
            print(population[i])
            if population[i].fitness > minFitness:
                parents.append(population[i])
        if len(parents)/(len(population)*1.0) < 0.45:
            generations = generations + 1
            flag = True
        elif len(parents)/(len(population)*1.0) > 0.55:
            minFitness = minFitness + 0.1
            generations = generations + 1
            flag = True
        else:
            while (len(newpopulation) < 10000)

        if flag:
            parents = []
            flag = False

    """ This code generates a parent population
    populationSize = 100
    generations = 5
    minFitness = 1.0
    population = []
    parents = []
    
    for i in range(0, populationSize):
        population.append(Chromosome())
    cnt = 0
    while (cnt < 50):
        for i in range(0, len(population)):
            if population[i].fitness > minFitness:
                parents.append(population[i])
            if len(parents) == 50:
                break
        cnt = len(parents)
            
    for i in range(0, len(parents)):
        print(parents[i].fitness, i)
    """


    #general process
    #1. we choose fittest half of population to compose new population
    #2. we breed them to form children (and add that onto newe population)
    #3. we repopulate with random ones to origninal popualation length
    #4. do at til we got a satisfactory result