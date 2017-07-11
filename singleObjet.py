import numpy as np
import math
%matplotlib inline
import matplotlib.pyplot as plt


class object() :
    def __init__ (self, coordinates, rechabilityDistance=-1, coreDistance=-1, processed = False) :
        #self.dimension = coordinates.size
        self.coordinates = coordinates
        self.rechabilityDistance = rechabilityDistance
        self.coreDistance = coreDistance
        self.processed = processed
        
    def distance(self, secondObject) :
        return math.sqrt(np.sum((secondObject.coordinates - self.coordinates)**2))
        
        
    def setCoreDistance(self, neighbours, epsilon, MinPts) :
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
            self.objectsCollection = []
            self.dimension = 0
            if fileName :
                dataFile = open(fileName, 'r')
                lines = dataFile.readlines()
                for line in lines :
                    dataObj_as_string = line.split("\t")
                    self.dimension = len(dataObj_as_string)-1
                    obj_coord = np.zeros(self.dimension)
                    for n in range(self.dimension) :
                        obj_coord[n] = float(dataObj_as_string[n])
                    obj = object(obj_coord)
                    self.objectsCollection.append(obj)

    def __call__ (self) :
        print("ane")
        
    def neighbours (self, obj, epsilon) :
        listOfNeighbour = []
        for obj_neighbour in self.objectsCollection :
            if obj.distance(obj_neighbour) < epsilon :
                listOfNeighbour.append(obj_neighbour)
        return listOfNeighbour
            
        
        
y = np.ones(3)

x = object(y)
print(x.coordinates)
a = setOfObjects("output.txt")
print(a.objectsCollection[0].coordinates)
a()
neigh = a.neighbours(a.objectsCollection[0], 0.1)
print(neigh)
a.objectsCollection[0]
X = np.zeros(2)
print(X, X.shape)
for o in neigh : 
    X = np.concatenate((X,o.coordinates))
Y = X.reshape(len(neigh)+1, 2)

plt.scatter(Y[:,0],Y[:,1],marker='o',s=10,color='r')
#hold on
plt.scatter(a.objectsCollection[0].coordinates[0], a.objectsCollection[0].coordinates[1],marker='o',s=10,color='b')


def ExpandClusterOrder (objectSet, obj, epsilon, MinPts, orderedFile) :
    neighbours = objectSet.neighbours(obj,epsilon)
    obj.processed = True
    obj.rechabilityDistance = None
    obj.setCoreDistance(neighbours, epsilon, MinPts)
    #orderedFile.writelines.()    RIORDIAMOI DI SRIVERE IL FILE ALLA FINE
    OrderSeeds = []
    
    
#if __name__ == main() :
def OPTICS(dataFile, epsilon, MinPts, OrderedFile) :
    orderedFile = open(OrderedFile, 'w')
    objectSet = setOfObjects(dataFile)
    for obj in objectSet.objectsCollection :
        if not obj.processed :
            ExpandClusterOrder (objectSet, obj, epsilon, MinPts, orderedFile)
    
    
