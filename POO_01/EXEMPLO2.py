import PRODUTO_POO as p #Importar o módulo

p1 = p.Produto() #Instanciar o objeto 

#Entrada de Dados
print("Digite os dados do Produto")
p1.nome = input("\tNome: ")
p1.preco = float(input("\tPreco: R$"))
p1.saldo = int(input("\tQuantidade: "))

#Saída de Dados 1a
print("Dados do Produto")
print(f"\tNome do Produto: {p1.nome}")
print(f"\tValor da Compra: {p1.preco:.2f}")
print(f"\tQuantidade em Estoque: {p1.saldo:.2f}")
print(f"\tValor Total em Estoque: {p1.valorTotalEmEstoque():.2f}")


