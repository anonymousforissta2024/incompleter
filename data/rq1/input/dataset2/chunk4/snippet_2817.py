#Source: https://stackoverflow.com/questions/56846939/why-am-i-getting-typeerror-for-device-function-in-pennylane
from pennylane import numpy as np
import pennylane as qml

dev1 = qml.Device('default.qubit', wires=1)