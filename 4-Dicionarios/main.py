produto = input("Digite o nome do produto: ")
print("O produto possui", len(produto), "caracteres")
print("O primeiro caracter é", produto[0], "e o último caractere é", produto[-1])

quantidade = int(input("Digite a quantidade de itens: "))

valor = float(input("Digite o valor total: "))

item = {
    "produto": produto,
    "quantidade": quantidade,
    "valor": valor
}

print("Chaves:", item.keys())
print("Valores:", item.values())
print("Produto:", item["produto"])
print("Quantidade:", item["quantidade"])
print("Valor:", item["valor"])
