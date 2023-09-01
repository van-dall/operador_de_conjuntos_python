def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            resultados = []

            i = 0
            while i < len(linhas):
                conjunto1 = set(map(int, linhas[i].split()))
                conjunto2 = set(map(int, linhas[i + 1].split()))
                operacao = linhas[i + 2].strip()

                if operacao == 'U':
                    resultado = conjunto1.union(conjunto2)
                elif operacao == 'I':
                    resultado = conjunto1.intersection(conjunto2)
                elif operacao == 'D':
                    resultado = conjunto1.difference(conjunto2)
                elif operacao == 'C':
                    resultado = {(x, y) for x in conjunto1 for y in conjunto2}
                else:
                    resultado = None

                resultados.append(resultado)
                i += 3

            return resultados
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

def main():
    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    resultados = ler_arquivo(nome_arquivo)

    if resultados is not None:
        for i, resultado in enumerate(resultados, start=1):
            print(f"Resultado da operação {i}:", resultado)

if __name__ == "__main__":
    main()
