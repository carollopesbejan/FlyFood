import random

def dois_menores(populacao, aptidao):
    menor_val = segundo_menor_val = float('inf')
    menor_perm = segundo_menor_perm = None

    for perm, val in zip(populacao, aptidao):
        if val < menor_val:
            segundo_menor_val = menor_val
            segundo_menor_perm = menor_perm
            menor_val = val
            menor_perm = perm
        elif val < segundo_menor_val:
            segundo_menor_val = val
            segundo_menor_perm = perm

    return ((menor_val, menor_perm), (segundo_menor_val, segundo_menor_perm))

def selecao_torneio(populacao, aptidao, k=3):
    """
    Seleciona 'k' indivíduos aleatórios da população e
    retorna o que tiver a melhor aptidão (menor custo).
    """
    competidores_idx = random.sample(range(len(populacao)), k)
    melhor_idx = min(competidores_idx, key=lambda idx: aptidao[idx])
    return populacao[melhor_idx]

def mutacao(permutacao, taxa_mutacao=0.05):
    """
    Mutação por Troca (Swap Mutation): Escolhe duas cidades
    aleatórias e inverte a posição delas com base na taxa de mutação.
    """
    if random.random() < taxa_mutacao:
        idx1, idx2 = random.sample(range(len(permutacao)), 2)
        permutacao[idx1], permutacao[idx2] = permutacao[idx2], permutacao[idx1]
    return permutacao

def cruzamento(pai1, pai2):
    n = len(pai1)

    def criar_filho(p1, p2):
        corte1, corte2 = sorted(random.sample(range(n), 2))
        filho = [None] * n
        filho[corte1:corte2] = p1[corte1:corte2]

        elementos_copiados = set(filho[corte1:corte2])
        posicoes_vazias = list(range(corte2, n)) + list(range(0, corte1))
        cidades_p2 = p2[corte2:] + p2[:corte2]

        idx_vazio = 0
        for cidade in cidades_p2:
            if cidade not in elementos_copiados:
                filho[posicoes_vazias[idx_vazio]] = cidade
                idx_vazio += 1
                if idx_vazio == len(posicoes_vazias):
                    break
        return filho

    filho1 = criar_filho(pai1, pai2)
    filho2 = criar_filho(pai2, pai1)

    # CORRIGIDO AQUI: Mudado de 'return filho1, ...' para:
    return filho1, filho2

def criar_nova_geracao(populacao, aptidao, taxa_mutacao=0.05):
    """
    Gera uma população completamente nova combinando elitismo,
    seleção, cruzamento e mutação.
    """
    tamanho_pop = len(populacao)
    nova_populacao = []

    # 1. ELITISMO: Salva os 2 melhores da geração atual direto para a próxima
    menores = dois_menores(populacao, aptidao)
    nova_populacao.append(menores[0][1]) # Melhor absoluto
    nova_populacao.append(menores[1][1]) # Segundo melhor

    # 2. REPRODUÇÃO: Preenche o resto da população com novos filhos
    while len(nova_populacao) < tamanho_pop:
        # Seleciona dois pais de forma independente por torneio
        pai1 = selecao_torneio(populacao, aptidao)
        pai2 = selecao_torneio(populacao, aptidao)

        # Realiza o cruzamento Order-1
        filho1, filho2 = cruzamento(pai1, pai2)

        # Aplica a mutação nos filhos gerados
        filho1 = mutacao(filho1, taxa_mutacao)
        filho2 = mutacao(filho2, taxa_mutacao)

        # Adiciona os filhos respeitando o limite da população original
        nova_populacao.append(filho1)
        if len(nova_populacao) < tamanho_pop:
            nova_populacao.append(filho2)

    return nova_populacao

def main():
    dicDistancias = ler_arquivo()
    populacao = inicializaPopulacao(100, 58)

    # Configuração do Algoritmo Genético
    num_geracoes = 4_000
    taxa_mutacao = 0.05  # 5% de chance de mutação por indivíduo

    print("Iniciando a evolução...")
    print("-" * 50)

    for g in range(1, num_geracoes + 1):
        # Calcula a aptidão da população atual
        aptidao = calculaAptidao(populacao, dicDistancias)

        # Encontra os melhores para exibir no log
        menores = dois_menores(populacao, aptidao)
        melhor_custo = menores[0][0]

        if g == 1 or g % 10 == 0 or g == num_geracoes:
            print(f"Geração {g:03d} | Melhor Custo Atual: {melhor_custo}")

        # Gera a nova população substituindo a antiga
        populacao = criar_nova_geracao(populacao, aptidao, taxa_mutacao)

    # Resultado Final após todas as gerações
    aptidao_final = calculaAptidao(populacao, dicDistancias)
    resultado = dois_menores(populacao, aptidao_final)
    print("-" * 50)
    print(f"Evolução concluída!")
    print(f"Melhor Rota Encontrada (Custo {resultado[0][0]}): {resultado[0][1]}")

def ler_arquivo():
    # SEU CÓDIGO ORIGINAL RESTAURADO:
    objArq = open("edgesbrasil58.tsp")
    distancias = {}

    for i in range(1, 58):
        linha = objArq.readline()
        lista = i_lista = linha.split()

        for j in range(i + 1, 59):
            if len(lista) > 0:
                peso = int(lista.pop(0))
            else:
                print(f"Erro! linha {i} do arquivo não possui elementos suficientes")
                exit()
            distancias[(i, j)] = peso
            distancias[(j, i)] = peso
    objArq.close()
    return distancias

def custoCaminho(permutacao, dicDistancias):
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