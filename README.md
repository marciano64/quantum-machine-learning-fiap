# FIAP - Faculdade de Informática e Administração Paulista
<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br> 

# Quantum Machine Learning: Classificação Quântica Aplicada

## 👨‍🎓 Integrantes:
* Edmilson Marciano Santos - RM 565912

## 📜 Descrição
Este projeto aplica conceitos fundamentais de Computação Quântica e Variational Quantum Circuits (VQC) para resolver problemas de Inteligência Artificial (Quantum Machine Learning). O objetivo principal foi codificar o clássico Iris Dataset em estados quânticos (através de Angle Embedding) e treinar uma rede neural quântica utilizando o framework PennyLane para classificar espécies de flores com otimizadores clássicos.

## 📁 Estrutura de pastas
Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:
* **assets**: Imagens e gráficos gerados durante os experimentos.
* **src**: Todo o código fonte criado, contendo os geradores de superposição, circuitos de emaranhamento (Estado de Bell) e o classificador quântico.
* **README.md**: Guia geral do projeto.

## 🔧 Como executar o código
1. Certifique-se de estar em um ambiente Linux (Ubuntu).
2. Ative o ambiente virtual e instale as dependências:
   ```bash
   pip install qiskit qiskit-aer pennylane scikit-learn
   ```
3. Execute o classificador quântico:
   ```bash
   python src/classificador_flores.py
   ```

## 🗃 Histórico de lançamentos
* 0.1.0 - 13/09/2026 - Implementação do Classificador Quântico Híbrido (81% de acurácia).
