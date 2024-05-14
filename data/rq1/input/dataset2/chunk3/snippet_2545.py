#Source: https://stackoverflow.com/questions/52701261/qiskit-nameerror-name-q0-is-not-defined
from qiskit import*
from qiskit.tools.visualization import*

list = [q0,q1,q2]
def ccz(qci,q0,q1,q2):
    qci.h(q2)
    qci.ccx(q0,q1,q2)
    qci.h(q2)
def grover(qci,q0,q1,q2):
    ccz(qci,q0,q1,q2)
    for i in range(list):
        qci.h(i)
        qci.x(i)
    ccz(qci,q0,q1,q2)
    for i in range(list):
        qci.x(i)
        qci.h(i)

bn = 3
q = QuantumRegister(bn)
c = ClassicalRegister(bn)
qc = QuantumCircuit(q,c)
for i in range(bn):
    qc.h(q[i])
grover(qc,q[0],q[1],q[2])
for i in range(bn):
    qc.measure(q[bn-i-1],c[i])
r = execute(qc,"local_qasm_simulator").result()
rc = r.get_counts()
print(rc)
plot_histogram(rc) 