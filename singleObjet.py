import numpy as np


class object() :
    def __init__ (self, coordinates, rechabilityDistance=-1, coreDistance=-1, processed = False) :
        self.dimension = coordinates.size
        self.coordinates = coordinates
        self.rechabilityDistance = rechabilityDistance
        self.coreDistance = coreDistance
        self.processed = processed
        
    def distance(self, 2ndObject) :
        
        
    def computeCoreDistance(self, neighbours, epsilon, MinPts) :
        if len(neighbours) < MinPits : return None
        else : 
            sortedNeighbour = sorted(neighbour, self.distance)
            self.coreDistance = distance(sortedNeighbour[MinPts-1])
            
        
    def computeRechabilityDistance(self, 2ndObject) :
        if len(neighbour) < MinPts : return None
        else :
            max(distance(2ndObject), coreDistance)
            
        
        
        
        
class setOfObjects() :
    self.TanteCose = []
    
    
    
        def __init__(self, filename) :
            
        
        
        
        
        
y = np.ones(3)

x = object(y)
print(x.coordinates)
