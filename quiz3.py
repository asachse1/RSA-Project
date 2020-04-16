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
    
    # Base Case (ground Zero)
    if (maxWeight == 0 or i == 0):
        return 0
    
    # Base Case (Already calculated SUBPROBLEM)
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


modeNum = NULL_NUMBER
# Setting Mode Test
print('\n')
while (modeNum != 0 and modeNum != 1):
    modeNum = int(input("Please enter '0' to test Greedy Algorithm, and '1' to test Recursive/Dynamic/Memoization Algorithm: "))

# wi1, wi2, wi3... wim
warehouseWeights = []
numInput = 0
print('\n')

#Setting package weights
while (numInput >= 0):
    numInput = int(input("Enter the positive weight of each package, pressing 'Enter' after each package. (Enter a negative # when finished): "))
    if (numInput >= 0):
        warehouseWeights.append(numInput)
numInput = NULL_NUMBER
print('\n')

#Setting max weight
while (numInput < 0):
    numInput = int(input("Please enter the max weight the truck can hold. (0 or larger): "))
maxWeight = numInput
numInput = NULL_NUMBER
print('\n')

#Setting Constant Variable
while (numInput < 0):
    numInput = int(input("Please enter a number to represent the CONSTANT price modifier. (0 or larger): "))
constantPrice = numInput

print('\n')
constValueStr = "Weights: " + str(warehouseWeights) + '\n' + "Max Value Possible (Greedy Algorithm): "
propValueStr = "Weights: " + str(warehouseWeights) + '\n' + "Max Value Possible(Dynamic/Recursive Algorithm): "

# Greedy Algorithm
if (modeNum == 0):
    print (constValueStr + str(constantValueAlgo(constantPrice, maxWeight, warehouseWeights)))

# Recursive/Dynamic Algorithm
if (modeNum == 1):
    propValues = [0 for x in range(len(warehouseWeights))]


    for x in range(len(warehouseWeights)):
        propValues[x] = (warehouseWeights[x] * constantPrice)

    #Create Memoization Table
    optimalValues = []
    for i in range(len(warehouseWeights)):
        optimalValues.append([])
        for j in range(maxWeight + 1):
            optimalValues[i].append(NULL_NUMBER)
    #FUNCTION CALL
    print (propValueStr + str(propValueAlgo(maxWeight, len(warehouseWeights), warehouseWeights, propValues, optimalValues)))
