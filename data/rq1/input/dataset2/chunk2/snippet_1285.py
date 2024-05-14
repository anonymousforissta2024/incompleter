#Source: https://stackoverflow.com/questions/47715289/typeerror-not-supported-between-instances-of-float-and-function
import infection

def isResistent(virus):
    if virus.find('AAA') > -1:
        return True
    else:
        return False

def simulate(viruses, mortalityProb, mutationProb, maxReproductionProb, maxPopulation, timesteps = 500):
    activation_cure = 400
    while timesteps > -1:
        survivors = infection.kill(viruses, mortalityProb)
        for virus in viruses:
            if timesteps < activation_cure and isResistent(virus):
                reproductionProb = infection.reproductionProbability
                infection.reproduce(viruses, mutationProb, reproductionProb)
        timesteps -= 1
    return len(viruses)

def experiment(numberOfPatients):
    cured = 0
    viruses = []
    for i in range(10):
        viruses.append(infection.generateVirus(16))
    for i in range(numberOfPatients):
        remaining_virus = simulate(viruses, 0.05, 0.1, 0.07, 1000)
        if remaining_virus[len(remaining_virus)-1] == 0:
            cured += 1
    return cured

print(experiment(5))