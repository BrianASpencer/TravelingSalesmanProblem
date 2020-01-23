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
        return 50.0/self.dist

if __name__ == "__main__":
    
    # generating our population of size n

    n = 10000
    population = []

    for i in range(0, n):
        population.append(Chromosome())