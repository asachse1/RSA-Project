#Name: Adam Sachsel
#Date: 04/15/2020
#Assn: Quiz3
#Class: Marron CS441

NULL_NUMBER = -100

class Package:
    def __init__(self, weight, value, ratio):
        self.weight = weight
        self.value = value
        self.ratio = self.value/self.weight


def constantValueAlgo(constantPrice, maxWeight, warehouseWeights):
   # SORT O(nlogn)
    warehouseWeights.sort()
    currentWeight = 0
    ctr = 0

    # Worst Case O(n)
    while (currentWeight < maxWeight):
        #none left
        if (ctr >= len(warehouseWeights)):
            return (ctr * constantPrice)
        #add one more
        elif (currentWeight + warehouseWeights[ctr] <= maxWeight):
            currentWeight += warehouseWeights[ctr]
            ctr += 1
        else:
            return (ctr * constantPrice)
        #at or over capacity
        if (currentWeight >= maxWeight):
            return (ctr * constantPrice)

def propValueAlgo(maxWeight, i, objWeights, objValues, optimalValues):
    
    if (maxWeight == 0 or i == 0):
        return 0
    
    if optimalValues[i-1][maxWeight] != NULL_NUMBER:
        return (optimalValues[i-1][maxWeight])
    
    # current "i" doesn't fit (SUBPROBLEM)
    if (objWeights[i - 1] > maxWeight):
        optimalValues[i-1][maxWeight] = propValueAlgo(maxWeight, i-1, objWeights, objValues, optimalValues)
        return optimalValues[i-1][maxWeight]
    
    # current "i" can fit!!!
    elif(objWeights[i - 1] <= maxWeight):
        
        # current object + SUBPROBLEM of leftover weight
        option1 = objValues[i-1] + propValueAlgo((maxWeight - objWeights[i-1]), i-1, objWeights, objValues, optimalValues)
        # same capacity WITHOUT current item (SUBPROBLEM)
        option2 = propValueAlgo(maxWeight, i-1, objWeights, objValues, optimalValues)
        # return SUBPROBLEM max Value
        optimalValues[i-1][maxWeight] = (max(option1, option2))
        return optimalValues[i-1][maxWeight]



# wi1, wi2, wi3... wim
warehouseWeights = [1, 3, 4, 5]

# W
maxWeight = 7

# C
constantPrice = 1

# Vi
propValues = [0 for x in range(len(warehouseWeights))]


for x in range(len(warehouseWeights)):
    propValues[x] = (warehouseWeights[x] * constantPrice)

constValueStr = "Max value possible with constant value is: "
propValueStr = "Max value possible with proportional value is: "


print (constValueStr + str(constantValueAlgo(constantPrice, maxWeight, warehouseWeights)))

optimalValues = []
for i in range(len(warehouseWeights)):
    optimalValues.append([])
    for j in range(maxWeight + 1):
        optimalValues[i].append(NULL_NUMBER)

print (propValueStr + str(propValueAlgo(maxWeight, len(warehouseWeights), warehouseWeights, propValues, optimalValues)))
print("hello")