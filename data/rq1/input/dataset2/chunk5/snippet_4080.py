#Source: https://stackoverflow.com/questions/61262052/receiving-following-error-when-trying-to-write-python3-program-nameerror-name
import itertools
import random
import busters
import game

from util import manhattanDistance, raiseNotDefined

def getBeliefDistribution(self):
        """
        Return the agent's current belief state, a distribution over ghost
        locations conditioned on all evidence and time passage. This method
        essentially converts a list of particles into a belief distribution.

        This function should return a normalized distribution.
        """
        "*** YOUR CODE HERE ***"
        beliefDistribution = util.Counter()

        for particle in self.particles: #in particle list
            beliefDistribution[particle] += 1 #weighing all the particles
        beliefDistribution.normalize() #normalizing

        return beliefDistribution #returns distribution

        #util.raiseNotDefined()