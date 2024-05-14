#Source: https://stackoverflow.com/questions/47715289/typeerror-not-supported-between-instances-of-float-and-function
import random

def generateVirus(length):
    return ''.join([random.choice(['A', 'G', 'T', 'C']) for i in range(length)])

def mutate(virus):
    rand = random.randint(0, len(virus)-1)
    return virus[:rand] + random.choice([i for i in 'AGTC' if i != virus[rand]]) + virus[rand+1:]

def kill(viruses, mortalityProb):
    return [survivors for survivors in viruses if random.random() > mortalityProb]

def reproduce(viruses, mutationProb, reproductionProb):
    nextgen = []
    for i in viruses:
        nextgen.append(i)
        if random.random() < reproductionProb:
            if random.random() < mutationProb:
                nextgen.append(mutate(i))
            else:
                nextgen.append(i)
    return nextgen

def reproductionProbability(viruses, maxReproductionProb, maxPopulation):
    return (1 - (len(viruses) / maxPopulation)) * maxReproductionProb

def simulate(viruses, mortalityProb, mutationProb, maxReproductionProb, 
    maxPopulation, timesteps = 500):
    pop_size = []
    while timesteps > -1:
        survivors = kill(viruses, mortalityProb)
        reproductionProb = reproductionProbability(survivors, maxReproductionProb, maxPopulation)
        viruses = reproduce(survivors, mutationProb, reproductionProb)
        pop_size.append(len(viruses))
        timesteps -= 1
    return pop_size

print(simulate(['GCTCC', 'CCGG', 'AACCGG', 'CCCTATAGG'], 0.05, 0.1, 0.07, 1000))