from qiskit import *
from qiskit_aer import AerSimulator

SHOTS = 1000

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')
qc = QuantumCircuit(q,c)

qc.h(q[0])
qc.cx(q[0],  q[1])

print(qc)

qc.measure(q[0],c[0])
qc.measure(q[1],c[1])

print(qc)

backend = AerSimulator()
job = backend.run(qc, shots=SHOTS)

result = job.result()
counts = result.get_counts()

print("counts:", counts)