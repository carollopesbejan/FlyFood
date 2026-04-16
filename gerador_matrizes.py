def gerar_matriz(linhas, colunas):
    for _ in range(linhas):
        for _ in range(colunas):
            print(0, end="")
        print(0)

def main():
    gerar_matriz(4, 5)

if __name__ == "__main__":
    main()