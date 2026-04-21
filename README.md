# 🚁Fly Food - Otimização de Rotas com Força Bruta

Este projeto simula o problema de otimização de rotas de entrega utilizando drones, inspirado na empresa fictícia FlyFood.

O objetivo é encontrar a melhor sequência de entregas, minimizando a distância total percorrida, considerando a limitação de bateria dos drones.

A solução utiliza o algoritmo de **força bruta**, testando todas as possíveis rotas e selecionando a de menor custo.

### 🧠 Conceitos Utilizados

- Algoritmo de força bruta
- Permutações (`itertools.permutations`)
- Distância de Manhattan
- Estruturas de dados (listas e dicionários)
- Leitura de arquivos

## 🚀 O Problema

O cenário foi modelado como uma variação do **Problema do Caixeiro Viajante (TSP - Travelling Salesman Problem)**. 

### Desafios Principais:
* **Malha Bidimensional:** Coordenadas (x, y) representando os pontos de entrega.
* **Custo de Deslocamento:** Calculado através da **Distância de Manhattan**, simulando o movimento em eixos horizontais e verticais.
* **Restrição de Retorno:** O drone deve obrigatoriamente iniciar e finalizar o trajeto na base.
