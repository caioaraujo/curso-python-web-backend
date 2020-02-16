produtos = []

while True:
    produto = input("Digite o nome do primeiro produto (tecle 0 para sair): ")

    if produto == "0":
        break

    quantidade = int(input("Digite a quantidade de itens do produto: "))

    valor = float(input("Digite o valor total do produto: "))

    item = {
        "produto": produto,
        "quantidade": quantidade,
        "valor": valor
    }

    produtos.append(item)

print("Total de produtos:", len(produtos))

if len(produtos) == 0:
    print("Você não cadastrou nenhum produto")
    exit(0)

lista_de_nomes = []
lista_de_quantidades = []
lista_de_valores = []

for produto in produtos:
    lista_de_nomes.append(produto["produto"])
    lista_de_quantidades.append(produto["quantidade"])
    lista_de_valores.append(produto["valor"])

print("Produtos cadastrados em ordem alfabética: ", sorted(lista_de_nomes))
print("Produtos cadastrados, sem valores repetidos:", set(lista_de_nomes))
print("Quantidade total de itens:", sum(lista_de_quantidades))
print("Valor total dos itens:", sum(lista_de_valores))
print("Produto mais caro:", max(lista_de_valores))
print("Produto mais barato:", min(lista_de_valores))
