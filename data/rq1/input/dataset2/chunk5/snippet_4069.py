#Source: https://stackoverflow.com/questions/55003113/attributeerror-nonetype-object-has-no-attribute-magnitude
class Force:
    def __init__(self,magnitude,angle):
        self.magnitude = magnitude
        self.angle = angle

    def get_horizontal(self):
        return self.magnitude * cos(radians(self.angle))

    def get_vertical(self):
        return self.magnitude * sin(radians(self.angle))

    def get_angle(self,use_degrees = True):
        if use_degrees:
            return self.angle
        else:
            return radians(self.angle)

def find_net_force(forces):
        tot_hor = 0
        tot_ver = 0
        for i in forces:
            tot_hor += i.get_horizontal()
            tot_ver += i.get_vertical()

        magnitude = (tot_hor ** 2 + tot_ver ** 2) ** 0.5
        magnitude = round(magnitude,1)
        angle = degrees(atan2((tot_ver),(tot_hor)))
        angle = round(angle,1)

force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
print(net_force.magnitude)
print(nIt_force.get_angle())