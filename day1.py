from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram, plot_bloch_multivector, plot_state_city
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# Build a Bell state
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Draw the circuit
print(qc.draw())

# Run simulation
sim = AerSimulator()
counts = sim.run(qc, shots=1024).result().get_counts()

# Histogram
plot_histogram(counts)
# plt.show()

# Bloch sphere (no measurement)
qc2 = QuantumCircuit(2)
qc2.h(0)
qc2.cx(0, 1)
sv = Statevector.from_instruction(qc2)
plot_bloch_multivector(sv)
# plt.show()

# State city
plot_state_city(sv)
plt.show()