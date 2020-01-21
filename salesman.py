import math

### Basic data -- doesn't chagnge ###

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

#distance calculator


def distance(path):
    dist = 0
    for i in range(0, len(path)-2):
        dist = dist + calcDist(cityCoords[path[i]], cityCoords[path[i+1]])
    dist = dist + calcDist(cityCoords[path[0]], cityCoords[path[len(path)-1]])
    return dist


def calcDist(coord1, coord2):
    dist = 0
    dist = math.sqrt(math.pow(coord1[0] - coord2[0],2) + math.pow(coord1[1] - coord2[1],2))
    return dist





path = [9,8,7,6,5,4,3,2,1]

print(distance(path))

