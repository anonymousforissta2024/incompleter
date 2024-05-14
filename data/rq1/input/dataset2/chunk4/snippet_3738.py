#Source: https://stackoverflow.com/questions/49259443/im-overlooking-something-typeerror-create-got-unexpected-keyword-argument
class SystemManager(models.Manager):
    """"""
    def create(self, project, system_name):
        system = super().create(project=project, system_name=system_name)
        system.save()

        Circuit.objects.create(system=system, circuit_name="Primary circuit")
        return system

class System(models.Model):
    objects = SystemManager()

    project     = models.ForeignKey('solgeo.Project', related_name='systems', on_delete=models.CASCADE)
    system_name = models.CharField(max_length=200)

    @classmethod
    def create(cls, project):
        system = cls(project=project)

    def __str__(self):
        return "system name: " + str(self.system_name)

class CircuitManager(models.Manager):
    """"""
    def create(self, project, system_name):
        circuit = super().create(system=system, circuit_name=circuit_name)
        circuit.save()
        return circuit


class Circuit(models.Model):
    """Models a hydraulic circuit"""
    objects = CircuitManager()

    system = models.ForeignKey(System, related_name='circuits', on_delete=models.CASCADE)
    circuit_name = models.CharField(max_length=200)