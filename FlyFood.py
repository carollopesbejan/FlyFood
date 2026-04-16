from itertools import permutations

def main():
    arquivo = open('matrizes/matriz3.txt', 'r')
    linhas_raw = arquivo.readlines()
    arquivo.close()

    linhas, colunas = map(int, linhas_raw[0].split())
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
    print(caminho_str)

    tempo_total = round(time.time() - start_time, 3)
    print(f'Código finalizado em {tempo_total} segundos.')

if __name__ == "__main__":
    main()