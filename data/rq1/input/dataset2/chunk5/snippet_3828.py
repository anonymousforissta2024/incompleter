#Source: https://stackoverflow.com/questions/46018123/attributeerror-float-object-has-no-attribute-get-coords
import math, random, pylab, copy

class Location(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def move(self, xc, yc):
        return Location(self.x+float(xc), self.y+float(yc))
    def get_coords(self):
        return self.x, self.y
    def get_dist(self, other):
        ox, oy = other.get_coords()
        x_dist = self.x - ox
        y_dist = self.y - oy
        return math.sqrt(x_dist**2 + y_dist**2)

class Compass_Pt(object):
    possibles = ('N', 'S', 'E', 'W')
    def __init__(self, pt):
        if pt in self.possibles: self.pt = pt
        else: raise ValueError('in Compass_Pt.__init__')

    def move(self, dist):
        if self.pt == 'N': return (0, dist)
        elif self.pt == 'S': return (0, -dist)
        elif self.pt == 'E': return (dist, 0)
        elif self.pt == 'W': return (-dist, 0)
        else: raise ValueError('in Compass_Pt.move')

class Field(object):
    ''' Cartesian plane where object will be located '''
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc
    def move(self, cp, dist):
        old_loc = self.loc
        xc, yc = cp.move(dist)
        self.loc = old_loc.move(xc, yc)
    def get_loc(self):
        return self.loc
    def get_drunk(self):
        return self.drunk

class Drunk(object):
    ''' Point itself '''
    def __init__(self, name):
        self.name = name
    def move(self, field, cp, dist = 1):
        if field.get_drunk().name != self.name:
            raise ValueError('Drunk.move called with drunk not in the field')
        for i in range(dist):
            field.move(cp, 1)

class Usual_Drunk(Drunk):
    def move(self, field, dist = 1):
        ''' Drunk.move superclass method override. Sends additional cp attribute.'''
        cp = random.choice(Compass_Pt.possibles)
        Drunk.move(self, field, Compass_Pt(cp), dist)


class Cold_Drunk(Drunk):
    def move(self, field, dist = 1):
        cp = random.choice(Compass_Pt.possibles)
        if cp == 'S':
            Drunk.move(self, field, Compass_Pt(cp), 2*dist)
        else:
            Drunk.move(self, field, Compass_Pt(cp), dist)

class EW_Drunk(Drunk):
    def move(self, field, time = 1):
        cp = random.choice(Compass_Pt.possibles)
        while cp != 'E' and  cp != 'W':
            cp = random.choice(Compass_Pt.possibles)
        Drunk.move(self, field, Compass_Pt(cp), time)

def perform_trial(time, f):
    start = f.get_loc()
    distances = [0,0]
    for t in range(1, time + 1):
        f.get_drunk().move(f)
        new_loc = f.get_loc()
        distance = new_loc.get_dist(start)
        distances.append(distance)
    return distances

def perform_sim(time, num_trials, drunk_type):
    dist_lists = []
    loc_lists = []
    for trial in range(num_trials):
        d = drunk_type('Drunk' + str(trial))
        f = Field(d, Location(0, 0))
        distances = perform_trial(time, f)
        locs = copy.deepcopy(distances)
        dist_lists.append(distances)
        loc_lists.append(locs)
    return dist_lists, loc_lists


def ans_quest(max_time, num_trials, drunk_type, title):
    dist_lists, loc_lists = perform_sim(max_time, num_trials, drunk_type)
    means = []
    for t in range(max_time + 1):
        tot = 0.0
        for dist_l in dist_lists:
            tot += dist_l[t]
        means.append(tot/len(dist_lists))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title('{} Ave. Distance'.format(title))
    lastX = []
    lastY = []
    for loc_list in loc_lists:
        x, y = loc_list[-1].get_coords()
        lastX.append(x)
        lastY.append(y)
    pylab.figure()
    pylab.scatter(lastX, lastY)
    pylab.ylabel('NW Distance')
    pylab.title('{} Final location'.format(title))
    pylab.figure()
    pylab.hist(lastX)
    pylab.xlabel('EW Value')
    pylab.ylabel('Number of Trials')
    pylab.title('{} Distribution of Final EW Values'.format(title))


num_steps = 50
num_trials = 10


ans_quest(num_steps, num_trials, Usual_Drunk, 'Usual Drunk ' + str(num_trials) + ' Trials')
ans_quest(num_steps, num_trials, Cold_Drunk, 'Cold Drunk ' + str(num_trials) + ' Trials')
ans_quest(num_steps, num_trials, EW_Drunk, 'EW Drunk ' + str(num_trials) + ' Trials')

pylab.show()