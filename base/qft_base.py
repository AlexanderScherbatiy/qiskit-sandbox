from qiskit import *
from qiskit.circuit.library import QFT
from qiskit_aer import AerSimulator

NUM_QUBITS = 3
SHOTS = 1000

q = QuantumRegister(NUM_QUBITS,'q')
c = ClassicalRegister(NUM_QUBITS,'c')
qc = QuantumCircuit(q,c)

qft = QFT(num_qubits=NUM_QUBITS, approximation_degree=0, do_swaps=True, inverse=False, insert_barriers=False)
qc.append(qft, qargs=range(NUM_QUBITS))

print(qc)

for i in range(NUM_QUBITS):
    qc.measure(q[i],c[i])

print(qc)

simulator = AerSimulator()
qct = transpile(qc, simulator)

job = simulator.run(qct, shots=SHOTS)

result = job.result()
counts = result.get_counts()

print("counts:", counts)