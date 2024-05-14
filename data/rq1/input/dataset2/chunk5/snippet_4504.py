#Source: https://stackoverflow.com/questions/24091859/name-error-in-random-generator-function
import random

class DNA_mutant_generator:
    def __init__ (self, dna):
        self.dna = dna
        self.bases = bases

    def mutate(mutation_rate=0.0066):
        result = []
        mutations = []
        for base in self.dna:
            if random.random() < mutation_rate:
                new_base = bases[bases.index(base) - random.randint(1, 3)] # negatives are OK
                result.append(new_base)
                mutations.append((base, new_base))#appends the original base, as well as the new mutated base to a list of tuples
            else:
                result.append(base)
        return "".join(result), mutations

        for result_string, mutations in results:
            if mutations: # skip writing out unmutated strings
                print(result_string, mutations)    
bases = "ACTG"
dna = "GGCTCTCCAACAGgtaagcactgaagggtagaaggcatcgtctgtctcagacatgtctggcaccatccgctaagacattaccacgtgggtctcgagtatagctaacacccttctgtttggcagCTTACAGGAGCGAACGTTGG"
dna_mutants = DNA_mutant_generator(dna)
dna_mutants.mutate()
results = [DNA_mutants.mutate() for _ in range(100)]