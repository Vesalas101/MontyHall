import random

def generateRandom(minValue, maxValue):
    return random.randint(minValue, maxValue)

unchangedCounter = 0
changedCounter = 0
trials = 100000
for i in range(trials):
    answer = generateRandom(1, 3)
    choice = generateRandom(1, 3)
    if answer == choice:
        unchangedCounter += 1


for i in range(trials):
    choices = [1, 2, 3]
    answer = generateRandom(1, 3)
    pick = generateRandom(1, 3)
    for j in range(3):
        if choices[j] != answer and choices[j] != pick:
            del choices[j]
            break
    if choices[0] == pick:
        pick = choices[1]
    else:
        pick = choices[0]
    if answer == pick:
        changedCounter += 1

print("Here's the answer if we choose the first door")
print(unchangedCounter / trials)
print("Here's the answer if we choose the other door")
print(changedCounter / trials)

