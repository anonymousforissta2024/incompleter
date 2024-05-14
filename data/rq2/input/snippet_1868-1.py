import random
randomList = random.choices(sampleList, weights=(10, 20, 30, 40, 50), k=5)
print(randomList)