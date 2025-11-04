#Problema Terreno

#Declaração de variáveis
largura: float
comprimento: float
preco_por_m2: float

#Entrada de dados
largura = float(input("Digite a largura do terreno (em metros): "))

comprimento = float(input("Digite o comprimento do terreno (em metros): "))

preco_por_m2 = float(input("Digite o preço por metro quadrado do terreno: "))

area = largura * comprimento

valor_do_terreno = area * preco_por_m2

#Saída de dados
print(f"A área do terreno é: {area:.2f} metros quadrados")

print(f"O valor do terreno é: R$ {valor_do_terreno:.2f}")