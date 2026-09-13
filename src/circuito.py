# Seu primeiro circuito quântico: Gerando Superposição Líquida!
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Cria um circuito quântico com 1 qubit e 1 bit clássico (para ler o resultado)
qc = QuantumCircuit(1, 1)

# 2. Aplica a Porta Hadamard (H) no qubit 0
# Isso coloca o qubit em SUPERPOSIÇÃO (50% de chance de ser 0, 50% de ser 1)
qc.h(0)

# 3. Mede o qubit 0 e guarda o resultado no bit clássico 0
qc.measure(0, 0)

# 4. Inicializa o simulador quântico local (Aer)
simulator = AerSimulator()

# 5. Executa o circuito no simulador 1000 vezes para coletar estatísticas (shots)
job = simulator.run(qc, shots=1000)
result = job.result()

# 6. Pega as contagens finais de quantas vezes caiu 0 ou 1
counts = result.get_counts(qc)

print("\n--- [ RESULTADOS DO SEU CIRCUITO QUANTICO ] ---")
print(f"Frequência de medições (0 ou 1): {counts}")
print("------------------------------------------------\n")

