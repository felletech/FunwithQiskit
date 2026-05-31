from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram, plot_state_city, plot_bloch_multivector
import matplotlib.pyplot as plt

# Build Bell state
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Noiseless circuit (no measurement) for statevector
qc_sv = QuantumCircuit(2)
qc_sv.h(0)
qc_sv.cx(0, 1)

# Noise model
noise_model = NoiseModel()
dep_error_1q = depolarizing_error(0.01, 1)
dep_error_2q = depolarizing_error(0.05, 2)
noise_model.add_all_qubit_quantum_error(dep_error_1q, ['h', 'x', 'z'])
noise_model.add_all_qubit_quantum_error(dep_error_2q, ['cx'])

# Run simulations
ideal_sim = AerSimulator()
noisy_sim = AerSimulator(noise_model=noise_model)

ideal_counts = ideal_sim.run(qc, shots=1024).result().get_counts()
noisy_counts = noisy_sim.run(qc, shots=1024).result().get_counts()

# Statevector (ideal, no noise)
sv = Statevector.from_instruction(qc_sv)

# --- Plot 1: histogram comparison ---
plot_histogram([ideal_counts, noisy_counts], legend=['ideal', 'noisy'])
# plt.savefig("histogram.png")
# plt.close()

# --- Plot 2: state city ---
plot_state_city(sv, title="State city — Bell state")
# plt.savefig("city.png")
# plt.close()

# --- Plot 3: Bloch spheres ---
plot_bloch_multivector(sv, title="Bloch spheres — Bell state")
# plt.savefig("bloch.png")
# plt.close()
plt.show()
# print("Saved: histogram.png, city.png, bloch.png")