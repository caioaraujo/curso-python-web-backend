produto = input("Digite o nome do produto: ")
print("O produto possui", len(produto), "caracteres")
print("O primeiro caracter é", produto[0], "e o último caractere é", produto[-1])

quantidade = int(input("Digite a quantidade de itens: "))

valor = float(input("Digite o valor total: "))

saida = f"Produto: {produto}, Qtde.: {quantidade}, Valor: {valor}"
print(saida)
