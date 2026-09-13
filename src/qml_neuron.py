import pennylane as qml
from pennylane import numpy as np

# 1. Configura um dispositivo quântico simulado de 1 qubit
dev = qml.device("default.qubit", wires=1)

# 2. Cria o "Neurônio Quântico" (Circuito Parametrizado)
@qml.qnode(dev)
def quantum_neuron(weights):
    # Aplica uma rotação no eixo Y baseada no "peso" do neurônio
    qml.RY(weights, wires=0)
    # Mede o valor esperado no eixo Z (retorna um valor entre -1 e 1)
    return qml.expval(qml.PauliZ(0))

# 3. Define a função de custo (o quão longe estamos do nosso objetivo)
# Queremos que o neurônio aprenda a retornar o valor EXATO -1
def cost_function(weights):
    return (quantum_neuron(weights) - (-1)) ** 2

# 4. Inicializa o peso do neurônio com um valor aleatório qualquer
weights = np.array(0.123, requires_grad=True)

# 5. Escolhe o otimizador clássico de IA (Gradient Descent)
opt = qml.GradientDescentOptimizer(stepsize=0.4)

print("\n--- [ TREINANDO O NEURÔNIO QUÂNTICO ] ---")
# Loop de treinamento por 10 épocas
for epoch in range(10):
    weights, cost = opt.step_and_cost(cost_function, weights)
    print(f"Época {epoch+1:02d} | Custo: {cost:.6f} | Peso Atual: {weights:.4f}")

print("\n[ SUCESSO ] O neurônio quântico aprendeu a rotacionar o qubit!")
print(f"Resultado final do circuito: {quantum_neuron(weights):.4f}\n")
