from itertools import permutations
from pathlib import Path
import os
import time

def main():
    diretorios = os.listdir(f"{os.getcwd()}/matrizes")

    for diretorio in diretorios:
        nome_arquivos = list(Path(f"{os.getcwd()}/matrizes/{diretorio}").rglob("*.txt"))
        for nome_arquivo in nome_arquivos:
            arquivo = open(nome_arquivo, 'r')
            linhas_raw = arquivo.readlines()
            arquivo.close()
            print("Arquivo:", nome_arquivo)

            inicio = time.time()
            matriz = [linha.split() for linha in linhas_raw[1:]]

            pontos = []
            coords = {}

            for x, linha in enumerate(matriz):
                for y, valor in enumerate(linha):
                    if valor != '0':
                        coords[valor] = (x, y)
                        if valor != 'R':
                            pontos.append(valor)

            menor_distancia = float('inf')
            melhor_rota = []

            for p in permutations(pontos):
                rota_atual = ('R',) + p + ('R',)
                dist_atual = 0
                
                for atual, proximo in zip(rota_atual, rota_atual[1:]):
                    x1, y1 = coords[atual]
                    x2, y2 = coords[proximo]
                    dist_atual += abs(x1 - x2) + abs(y1 - y2)
                
                if dist_atual < menor_distancia:
                    menor_distancia = dist_atual
                    melhor_rota = rota_atual

            caminho_str = ' '.join(melhor_rota[1:-1])

            fim = time.time()
            print(f"Melhor rota: {caminho_str}")
            print(f"Menor distância: {menor_distancia}")
            print("Tempo de processamento:", f"{fim - inicio} segundos")
            print()

if __name__ == "__main__":
    main()