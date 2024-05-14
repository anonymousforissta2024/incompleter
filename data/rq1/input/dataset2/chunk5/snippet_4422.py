#Source: https://stackoverflow.com/questions/53861239/getting-no-attribute-error-attribute-seems-to-be-there
from random import choice

class RandomWalk():
    """A class to generate random walks."""

    def _init_(self, num_points=5000):
        """ Initialize attributes of a walk."""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction
            x_direction = choice([1,-1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the pointsself.

rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()