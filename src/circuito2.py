from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Cria um circuito com 2 qubits e 2 bits clássicos
qc = QuantumCircuit(2, 2)

# 1. Coloca o primeiro qubit (0) em superposição
qc.h(0)

# 2. Aplica a porta CNOT (Controlled-NOT)
# O qubit 0 é o controle e o qubit 1 é o alvo.
# Isso EMARANHA os dois qubits!
qc.cx(0, 1)

# 3. Mede ambos os qubits
qc.measure([0, 1], [0, 1])

# 4. Executa no simulador local
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
counts = job.result().get_counts(qc)

print("\n--- [ RESULTADOS DO EMARANHAMENTO ] ---")
print(f"Resultados obtidos (Qubit1 Qubit0): {counts}")
print("----------------------------------------\n")
