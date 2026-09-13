import pennylane as qml
from pennylane import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

# 1. Carrega o Dataset Iris e filtra apenas 2 classes (Setosa e Versicolor)
iris = load_iris()
X = iris.data[iris.target < 2]
y = iris.target[iris.target < 2]

# Alinha os alvos para serem -1 (Setosa) e 1 (Versicolor) para a lógica quântica
y = np.where(y == 0, -1, 1)

# Normaliza as características (features) entre 0 e pi para caberem nas rotações quânticas
scaler = MinMaxScaler(feature_range=(0, np.pi))
X_scaled = scaler.fit_transform(X)

# 2. Configura o dispositivo quântico (vamos usar 2 qubits para processar as features)
dev = qml.device("default.qubit", wires=2)

# 3. Desenha o Circuito Quântico (Variational Quantum Circuit)
@qml.qnode(dev)
def quantum_circuit(weights, x):
    # Codifica os dados clássicos das flores em estados quânticos (Ângulos de Rotação)
    qml.RY(x[0], wires=0)
    qml.RY(x[1], wires=1)
    
    # Aplica os pesos que o modelo vai treinar (Camada Parametrizada)
    qml.RX(weights[0], wires=0)
    qml.RX(weights[1], wires=1)
    qml.CNOT(wires=[0, 1]) # Emaranhamento para misturar as informações
    
    # Retorna a medição
    return qml.expval(qml.PauliZ(0))

# 4. Função de Custo e Precisão (Accuracy)
def cost_function(weights, X_data, y_target):
    loss = 0
    for x, y_true in zip(X_data, y_target):
        prediction = quantum_circuit(weights, x)
        loss += (prediction - y_true) ** 2
    return loss / len(X_data)

# 5. Inicializa os pesos da IA Quântica aleatoriamente
np.random.seed(42)
weights = np.random.randn(2, requires_grad=True)

# Otimizador clássico
opt = qml.GradientDescentOptimizer(stepsize=0.5)

print("\n--- [ TREINANDO O CLASSIFICADOR QUANTICO DE FLORES ] ---")
# Treina por 5 épocas usando uma amostra para ir rápido
for epoch in range(5):
    weights, cost = opt.step_and_cost(lambda w: cost_function(w, X_scaled[:20], y[:20]), weights)
    print(f"Época {epoch+1:02d} | Perda (Loss): {cost:.6f} | Pesos: {weights.numpy()}")

# 6. Testando a acurácia do modelo quântico treinado
correct = 0
for x, y_true in zip(X_scaled, y):
    pred = np.sign(quantum_circuit(weights, x))
    if pred == y_true:
        correct += 1

print(f"\n[ RESULTADO FINAL ] Acurácia nas Flores: {(correct / len(y)) * 100:.2f}%")
