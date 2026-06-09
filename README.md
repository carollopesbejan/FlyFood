# 🚁Fly Food - Otimização de Rotas com Força Bruta e Algoritmo Genético

Este projeto simula o problema de otimização de rotas de entrega utilizando drones, inspirado na empresa fictícia FlyFood.

O objetivo é encontrar a melhor sequência de entregas, minimizando a distância total percorrida, considerando a limitação de bateria dos drones.

A solução foi desenvolvida com duas abordagens: **força bruta** para instâncias pequenas, e **Algoritmo Genético**, para instâncias de maior escala.

### 🧠 Conceitos Utilizados

- Algoritmo de força bruta
- Permutações (`itertools.permutations`)
- Distância de Manhattan
- Estruturas de dados (listas e dicionários)
- Leitura de arquivos
- Algoritmo Genético (DEAP)
- Mutação por inversão
- Seleção por torneio
- Elitismo (HallOfFame)

## 🚀 O Problema

O cenário foi modelado como uma variação do **Problema do Caixeiro Viajante (TSP - Travelling Salesman Problem)**. 

### Desafios Principais:
* **Malha Bidimensional:** Coordenadas (x, y) representando os pontos de entrega.
* **Custo de Deslocamento:** Calculado através da **Distância de Manhattan**, simulando o movimento em eixos horizontais e verticais.
* **Restrição de Retorno:** O drone deve obrigatoriamente iniciar e finalizar o trajeto na base.
* **Benchmark Real:** Instância brazil58 da TSPLIB, composta por 58 cidades com solução ótima conhecida de 25.395.
