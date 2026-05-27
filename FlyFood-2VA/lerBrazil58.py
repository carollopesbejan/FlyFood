from deap import base, creator, tools
import random

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)


class Populacao:
    def __init__(self, tamanho, qtde_cidades):
        self.tamanho = tamanho
        self.qtde_cidades = qtde_cidades
        self.individuos = [] #lista de rotas
        self.aptidoes = [] #lista de custos/aptidões
        self.inicializar()

    def inicializar(self):
        """Cria as permutações aleatórias iniciais."""
        self.individuos = []
        for _ in range(self.tamanho):
            individuo = creator.Individual(range(1, self.qtde_cidades + 1))
            random.shuffle(individuo)
            self.individuos.append(individuo)

    def avaliar(self, dicDistancias):
        """Calcula e armazena a aptidão de todos os indivíduos."""
        self.aptidoes = []
        for individuo in self.individuos:
            custo = custoCaminho(individuo, dicDistancias)
            individuo.fitness.values = (custo,)
            self.aptidoes.append(custo)
        return self.aptidoes

    def selecionar_pais(self):
        """Seleciona dois pais usando torneio binário."""
        return tools.selTournament(self.individuos, k=2, tournsize=2)

    def obter_dois_melhores(self):
        """Retorna as duas melhores tuplas (aptidao, individuo)."""
        menor_val = segundo_menor_val = float('inf')
        menor_perm = segundo_menor_perm = None

        # Percorre a população e a aptidão internamente em paralelo
        for perm, val in zip(self.individuos, self.aptidoes):
            if val < menor_val:
                segundo_menor_val = menor_val
                segundo_menor_perm = menor_perm

                menor_val = val
                menor_perm = perm
            elif val < segundo_menor_val:
                segundo_menor_val = val
                segundo_menor_perm = perm

        return ((menor_val, menor_perm), (segundo_menor_val, segundo_menor_perm))


def main():
    dicDistancias = ler_arquivo()

    # Instanciando a população como um objeto
    populacao = Populacao(tamanho=100, qtde_cidades=58)

    # Avaliando a população
    aptidao = populacao.avaliar(dicDistancias)
    print("Aptidões:", aptidao)

    # Seleciona os dois pais usando torneio binário
    pai1, pai2 = populacao.selecionar_pais()

    print("Pai 1 gerado:\t", pai1)
    print("Pai 2 gerado:\t", pai2)

    # Realiza o cruzamento Order-1
    filho1, filho2 = cruzamento(pai1, pai2)

    # Realiza a mutação
    filho1 = mutacao(filho1, taxa_mutacao=0.05)
    filho2 = mutacao(filho2, taxa_mutacao=0.05)
    print("Filho 1 gerado:\t", filho1)
    print("Filho 2 gerado:\t", filho2)


def mutacao(permutacao, taxa_mutacao):
    """
    Mutação por Inversão (Inverse Mutation):
    Escolhe dois pontos e inverte o segmento entre eles.
    """
    if random.random() < taxa_mutacao:
        n = len(permutacao)
        idx1, idx2 = sorted(random.sample(range(n), 2))
        permutacao[idx1:idx2] = reversed(permutacao[idx1:idx2])
    return permutacao


def cruzamento(pai1, pai2):
    filho1 = [cidade - 1 for cidade in pai1]
    filho2 = [cidade - 1 for cidade in pai2]

    # Aplica o cruzamento ordenado da DEAP
    tools.cxOrdered(filho1, filho2)

    # Somamos 1 de volta para retornar à base original (1 a 58)
    filho1 = [cidade + 1 for cidade in filho1]
    filho2 = [cidade + 1 for cidade in filho2]

    return filho1, filho2


def ler_arquivo():

    with open("edgesbrasil58.tsp", "r") as objArq:
        distancias = {}

        for i in range(1, 58):
            linha = objArq.readline()
            lista = linha.split()

            for j in range(i + 1, 59):
                if len(lista) > 0:
                    peso = int(lista.pop(0))
                else:
                    print(f"Erro! linha {i} do arquivo não possui elementos suficientes")
                    exit()
                distancias[(i, j)] = peso
                distancias[(j, i)] = peso

    return distancias


def custoCaminho(permutacao, dicDistancias):
    """Função que retorna o custo total do caminho."""
    soma = 0
    for i in range(len(permutacao) - 1):
        a = permutacao[i]
        b = permutacao[i + 1]
        if (a, b) in dicDistancias:
            soma += dicDistancias[(a, b)]
        else:
            print(f"Erro! ({a},{b}) não existe no dicionario!")
            exit()

    # Fechando o ciclo (última cidade voltando para a primeira)
    soma += dicDistancias[(permutacao[-1], permutacao[0])]
    return soma


if __name__ == "__main__":
    main()
