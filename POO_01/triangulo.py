#Problema Triângulo sem POO

#Entrada de Dados
#Triângulo X
print("Inserir as Medidas do Triângulo X")
ax = int(input("Digite a medida a: "))
bx = int(input("Digite a medida b: "))
cx = int(input("Digite a medida c: "))

#Triângulo Y
print("Inserir as Medidas do Triângulo Y")
ay = int(input("Digite a medida a: "))
by = int(input("Digite a medida b: "))
cy = int(input("Digite a medida c: "))

#Processamento de Dados
p = (ax+bx+cx) / 2
areax = (p * (p-ax) * (p-bx) * (p-cx)) **0.5

p = (ay+by+cy) / 2


if areax > areay:
    saida = "A área do triângulo X é maior que a área do triângulo Y."
elif areay > areax:
    saida = "A área do triângulo Y é maior que a área do triângulo X."
else:
    saida = "As áreas dos triângulos são iguais." 

#Saída de Dados
print(f"A área do triângulo X = {areax:.1f}")
print(f"A área do triângulo Y = {areay:.1f}")
print(saida)