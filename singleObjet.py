import numpy as np


class object() :
    def __init__ (self, coordinates, rechabilityDistance=-1, coreDistance=-1, processed = False) :
        #self.dimension = coordinates.size
        self.coordinates = coordinates
        self.rechabilityDistance = rechabilityDistance
        self.coreDistance = coreDistance
        self.processed = processed
        
    def distance(self, secondObject) :
        return 1
        
        
    def computeCoreDistance(self, neighbours, epsilon, MinPts) :
        if len(neighbours) < MinPits : return None
        else : 
            sortedNeighbour = sorted(neighbour, self.distance)
            self.coreDistance = distance(sortedNeighbour[MinPts-1])
            
        
    def computeRechabilityDistance(self, secondObject) :
        if len(neighbour) < MinPts : return None
        else :
            max(distance(secondObject), coreDistance)
            
        
        
        
        
class setOfObjects() :   
    
    def __init__(self, fileName = None) :
            self.objectCollection = []
            if fileName :
                dataFile = open(fileName, 'r')
                lines = dataFile.readlines()
                for line in lines :
                    dataObj_as_string = line.split("\t")
                    self.dimension = len(dataObj_as_string)-1
                    x = np.zeros(self.dimension)
                    for n in range(self.dimension) :
                        x[n] = float(dataObj_as_string[n])
                    print(x)
                    self.objectCollection.append(x)

                

        
        
        
        
y = np.ones(3)

x = object(y)
print(x.coordinates)
setOfObjects("output.txt")
print("pippo")
