import produtoOOP as p

#Entrada de Dados
print("Entre com os dados do produto:")

nome = input("Nome:")
preco = float(input("Preço R$:"))
saldo = int(input("Quantidade:"))

#Instanciar Objeto
#ps = p.Produto(nome, preco, saldo)
ps = p.Produto(nome, preco)

#Saída de Dados
print(ps.dadosDoProduto())