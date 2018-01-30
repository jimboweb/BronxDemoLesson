import math

siblingData = [2, 0, 3, 0, 1, 4, 3, 2, 1, 1, 2, 1, 3, 2, 1, 1, 2, 5, 2, 3, 4, 2, 4]

total = 0
for number in siblingData:
    total = total + number

print("our total number of siblings are " + str(total))

numberCount = len(siblingData)

average = total/numberCount
average = round(average,2)

print("on average we have " + str(average) + " siblings")

sortedNumbers = sorted(siblingData)

minSiblings = sortedNumbers[0]
print("the smallest number of siblings is " + str(minSiblings))
maxSiblings = sortedNumbers[numberCount-1]
print("the largest number of siblings is " + str(maxSiblings))


#find mode
siblingCount = []

for i in range(0,maxSiblings+1):
    siblingCount.append(0)

for number in siblingData:
    siblingCount[number]+=1

largestCount = max(siblingCount)

modes = []

for i, number in enumerate(siblingCount):
    if number==largestCount:
        modes.append(i)

print("the modes of our number of siblings is " + str(modes))


#find median
median = 0
if numberCount%2==0:
    firstMiddle = int(numberCount/2)
    secondMiddle = firstMiddle+1
    median = int((sortedNumbers[firstMiddle] + sortedNumbers[secondMiddle])/2)
else:
    middleNumber = math.ceil(numberCount/2) + 1
    median = sortedNumbers[middleNumber]

print("our median number of siblings is " + str(median))
