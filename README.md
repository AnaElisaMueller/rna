# 🧠 Detecção de Fraudes em Faturamentos na Área da Saúde com Redes Neurais Artificiais

## 📌 Sobre o Projeto

Este projeto tem como objetivo analisar a viabilidade do uso de Redes Neurais Artificiais (RNA) para a detecção de fraudes em faturamentos da área da saúde.  

Utilizando um modelo de classificação binária baseado em Multilayer Perceptron (MLP), o sistema identifica padrões suspeitos em registros de faturamento, auxiliando na distinção entre casos fraudulentos e não fraudulentos.

---

## 🎯 Objetivo

Desenvolver e avaliar um modelo de rede neural capaz de:

- Identificar possíveis fraudes em registros médicos
- Reduzir falsos negativos (fraudes não detectadas)
- Apoiar processos de auditoria e tomada de decisão na área da saúde

---

## 🧠 Metodologia

O projeto segue as seguintes etapas:

### 1. Pré-processamento dos dados
- Remoção de valores nulos
- Tratamento de outliers
- Remoção de duplicatas
- Normalização dos dados
- One-Hot Encoding para variáveis categóricas
- Target Encoding para variáveis de alta cardinalidade

### 2. Base de dados
- Dataset: Healthcare Fraud Detection Dataset (Kaggle)
- Aproximadamente 10.000 registros
- 19 variáveis

---

## 🤖 Modelo de Machine Learning

Foi utilizado um modelo de Rede Neural Artificial do tipo:

### MLP (Multilayer Perceptron)

Características:

- Implementado com TensorFlow e Keras
- Arquitetura Sequential
- Camadas Dense (totalmente conectadas)
- Função de ativação ReLU nas camadas ocultas
- Saída com função Sigmoid (classificação binária)
- Dropout para redução de overfitting

---

## ⚙️ Treinamento

- Divisão dos dados:
  - 80% treino
  - 20% teste

- Otimizadores testados:
  - SGD
  - Adam
  - RMSprop

- Função de perda:
  - Binary Cross-Entropy

- Estratégias adicionais:
  - Ajuste de hiperparâmetros
  - Ponderação de classes (desbalanceamento)
  - Experimentos com diferentes arquiteturas

---

## 📊 Avaliação do Modelo

O desempenho foi analisado com:

- Acurácia
- Precisão
- Recall (ênfase principal)
- Matriz de confusão

🔎 Foco especial na redução de falsos negativos (fraudes não detectadas)

---

## 📈 Resultados

Os experimentos demonstraram que:

- Redes neurais são eficazes para detecção de padrões complexos
- A escolha de hiperparâmetros impacta diretamente o desempenho
- O modelo apresentou boa capacidade de generalização
- A abordagem é viável para apoio à detecção de fraudes em saúde

---

## 🧰 Tecnologias Utilizadas

- Python 🐍
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn

---

## 👨‍💻 Autores

- Ana Elisa Mueller  
- Eduardo da Costa Couto  
- Gabriel Dall'acqua Gomes  
- Thais Bastos Oliveira  
- Vitor Rezer Soares  

---

## 📚 Dataset

Healthcare Fraud Detection Dataset  
https://www.kaggle.com/datasets/nudratabbas/healthcare-fraud-detection-dataset

---

## 📌 Observação

Este projeto foi desenvolvido como parte de disciplina acadêmica da Universidade de Santa Cruz do Sul (UNISC), com foco em aplicação de Inteligência Artificial em problemas reais.

---

## 🚀 Possíveis melhorias futuras

- Testes com outros modelos (Random Forest, XGBoost)
- Uso de redes neurais mais profundas
- Balanceamento avançado de classes (SMOTE)
- Validação cruzada