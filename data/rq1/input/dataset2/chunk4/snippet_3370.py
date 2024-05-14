#Source: https://stackoverflow.com/questions/76399931/attributeerror-cant-pickle-local-object-flask-init-locals-lambda
from multiprocessing import Process
import random
import string
import dill

import ServiceLogger as sl


class DillProcess(Process):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._target = dill.dumps(self._target)  # Save the target function as bytes, using dill

    def run(self):
        if self._target:
            self._target = dill.loads(self._target)  # Unpickle the target function before executing
            self._target(*self._args, **self._kwargs)  # Execute the target function


class ProcessBuilder:

    def __init__(self):
        self.processes = []
        self.logger = sl.ServiceLogger()

    def create_process(self, method, args=[]):
        process = DillProcess(name=self.__generate_instance_name(), target=method, args=tuple(args))
        self.processes.append(process)
        return process

    def get_process_instance(self, process_name):
        for process in self.processes:
            if str(process.name) == process_name:
                return process
        return None

    def run_process(self, process):
        process.start()

    def kill_process(self, process):
        process.kill()

    def __generate_instance_name(self):
        # printing lowercase
        letters = string.ascii_lowercase
        randomString = ''.join(random.choice(letters) for i in range(3))

        # printing letters
        letters = string.digits
        randomDigits = ''.join(random.choice(letters) for i in range(5))

        return randomString + "" + randomDigits