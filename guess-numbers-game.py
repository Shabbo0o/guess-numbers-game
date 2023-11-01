
import random
digits = list(range(10))
random.shuffle(digits)
randomList = digits[:3] 
#print(randomList)

def getNumbers():
    myList = [] 
    for i in range(3):
        number = input("Enter number {} between 0-9:".format(i+1))
        myList.append(number)
    return myList
counterSameNumber  = counterSamePlace = 0

while counterSamePlace != 3:
    counterSameNumber  = counterSamePlace = 0
    myList = getNumbers()
    j=0
    for j in range(3):
        if myList[j] == randomList[j]: 
            counterSamePlace +=1
        if ((myList[j] == randomList[0]) or (myList[j] == randomList[1]) or (myList[j] == randomList[2])): 
            counterSameNumber +=1
        
    print(counterSameNumber, counterSamePlace)
    print ("Hint: You've guessed {} number(s) correctly and {} number(s) in the correct position.".format(counterSameNumber, counterSamePlace))  
print("Match: You've guessed all numbers correctly and in the correct positions.")

