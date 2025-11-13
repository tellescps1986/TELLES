import triangulo_POO as tl

#Instanciar Classe
trianguloX = tl.triangulo()
trianguloY = tl.triangulo()

#Entrada de Dados
#Triângulo X
print("Inserir as Medidas do Triângulo X")
trianguloX.a = int(input("Digite a medida a: "))
trianguloX.b = int(input("Digite a medida b: "))
trianguloX.c = int(input("Digite a medida c: "))

#Triângulo Y
print("Inserir as Medidas do Triângulo Y")
trianguloY.a = int(input("Digite a medida a: "))
trianguloY.b = int(input("Digite a medida b: "))
trianguloY.c = int(input("Digite a medida c: "))

#Processamento de Dados
p = ((trianguloX.a + trianguloX.b + trianguloX.c) / 2)
areax = (p * (p-trianguloX.a) * (p-trianguloX.b) * (p-trianguloX.c)) **0.5

p = ((trianguloY.a + trianguloY.b + trianguloY.c) / 2)
areay = (p * (p-trianguloY.a) * (p-trianguloY.b) * (p-trianguloY.c)) **0.5

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

