import random

def dois_menores(populacao, aptidao):
    # Inicializa os dois menores valores com infinito positivo e suas permutações como None
    menor_val = segundo_menor_val = float('inf')
    menor_perm = segundo_menor_perm = None

    # Percorre a população e a aptidão em paralelo
    for perm, val in zip(populacao, aptidao):
        if val < menor_val:
            # O antigo menor passa a ser o segundo menor
            segundo_menor_val = menor_val
            segundo_menor_perm = menor_perm

            # Atualiza o novo menor
            menor_val = val
            menor_perm = perm
        elif val < segundo_menor_val:
            # O número é maior que o menor, mas menor que o segundo_menor
            segundo_menor_val = val
            segundo_menor_perm = perm

    # Retorna uma tupla contendo as duas tuplas estruturadas (valor, permutação)
    return ((menor_val, menor_perm), (segundo_menor_val, segundo_menor_perm))

def main():
    dicDistancias = ler_arquivo()
    populacao = inicializaPopulacao(100, 58)

    aptidao = calculaAptidao(populacao, dicDistancias)
    # print(aptidao)

    menores = dois_menores(populacao, aptidao)
    print(menores)

    # Separa os dois melhores indivíduos para serem os pais
    pai1 = menores[0][1]
    pai2 = menores[1][1]
    print("Pai 1 gerado:\t", pai1)
    print("Pai 2 gerado:\t", pai2)

    # Realiza o cruzamento Order-1
    filho1, filho2 = cruzamento(pai1, pai2)
    print("Filho 1 gerado:\t", filho1)
    print("Filho 2 gerado:\t", filho2)

def mutacao(permutacao):
    pass

def cruzamento(pai1, pai2):
    n = len(pai1)

    def criar_filho(p1, p2):
        # Escolhe dois pontos de corte aleatórios e distintos
        corte1, corte2 = sorted(random.sample(range(n), 2))

        # Inicializa o filho preenchido com None
        filho = [None] * n

        # Copia o segmento do primeiro pai para o filho
        filho[corte1:corte2] = p1[corte1:corte2]

        # Conjunto para busca rápida O(1) de elementos já copiados
        elementos_copiados = set(filho[corte1:corte2])

        # Posições a serem preenchidas no filho (daqui até o fim, e depois do início até o corte)
        posicoes_vazias = list(range(corte2, n)) + list(range(0, corte1))

        # Sequência circular de cidades tiradas do segundo pai
        cidades_p2 = p2[corte2:] + p2[:corte2]

        idx_vazio = 0
        for cidade in cidades_p2:
            if cidade not in elementos_copiados:
                filho[posicoes_vazias[idx_vazio]] = cidade
                idx_vazio += 1
                if idx_vazio == len(posicoes_vazias):
                    break
        return filho

    # Gera os dois filhos cruzando as referências dos pais
    filho1 = criar_filho(pai1, pai2)
    filho2 = criar_filho(pai2, pai1)

    return filho1, filho2

def ler_arquivo():
    objArq = open("edgesbrasil58.tsp")
    # se você quiser uma lista onde cada objeto será uma string
    # grande representando uma linha do arquivo:
    # listaLinhas = objArq.readlines() #obs: cada linha terah um enter junto com o ultimo elemento

    distancias = {}

    for i in range(1, 58):  # linhas 1 a 57 pois a 58 nao terá aresta
        linha = objArq.readline()  # le só uma linha do arquivo
        # transformando a linha em lista de strings:
        lista = linha.split()  # obs: lista de strings (não int)

        for j in range(i + 1, 59):  # colunas i+1 a 58
            if len(lista) > 0:
                peso = int(
                    lista.pop(0)
                )  # obs: peso int, poderia ser float em outro problema
            else:
                print(f"Erro! linha {i} do arquivo não possui elementos suficientes")
                exit()
            # gravando a aresta em (i, j) e (j, i):
            distancias[(i, j)] = peso
            distancias[(j, i)] = peso
    objArq.close()

    return distancias

# funcao que retorna o custo total do caminho:
def custoCaminho(permutacao, dicDistancias):
    # ex: permutacao = [5, 14, 2, 3, 7, ...]
    soma = 0
    for i in range(len(permutacao) - 1):
        a = permutacao[i]
        b = permutacao[i + 1]
        if (a, b) in dicDistancias:
            soma += dicDistancias[(a, b)]
        else:
            print(f"Erro! ({a},{b}) não existe no dicionario!")
            exit()
    soma += dicDistancias[(permutacao[-1], permutacao[0])]
    return soma


def inicializaPopulacao(tamanho, qtdeCidades):
    import random

    # criando uma lista com "tamanho" permutacoes aleatorias de cidades:
    lista = []
    for i in range(tamanho):
        individuo = list(range(1, qtdeCidades + 1))
        random.shuffle(individuo)
        lista.append(individuo)
    return lista

def calculaAptidao(populacao, dicDistancias):
    listaAptidao = []
    for elem in populacao:
        listaAptidao.append(custoCaminho(elem, dicDistancias))
    return listaAptidao

if __name__ == "__main__":
    main()