# Problema triangulo sem POO

# Entrada

# Trinagulo X
print('Inserir as medidas do triangulo X')
ax=int(input('Digite a medida a:'))
bx=int(input('Digite a medida b:'))
cx=int(input('Digite a medida c:'))

# Trinagulo Y
print('Inserir as medidas do triangulo Y')
ay=int(input('Digite a medida a:'))
by=int(input('Digite a medida b:'))
cy=int(input('Digite a medida c:'))

# Processamento de dados
p=(ax+bx+cx)/2
areax=(p*(p-ax)(p-bx)(p-cx))**0,5
p=(ay+by+cy)/2
areay=(p*(p-ay)(p-by)(p-cy))**0,5

if areax>areay:
    saida='A área do triângulo X é maior que a área do Y.'
elif areay>areax:
    saida='A área do triângulo Y é maior que a área do X.'
else:
    saida='As áreas dos triângulos são iguais!'

print(f"A área do triangulo X={areax}")
print(f"A área do triangulo Y={areay}")
print(saida)