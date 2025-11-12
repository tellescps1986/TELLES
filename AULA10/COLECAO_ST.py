#Lista

lista = ["SENAI", True, 22, 3.5]

print(lista)

print(type(lista))

print(lista[2])

print(len(lista))

lista.insert(1, "Campeão")
print(lista)


lista.append("Feriado")
print(lista)


del lista[3]
print(lista)


lista.append("Senai")
print(lista)

for i in range(len(lista)):
    print(list[i])

#Tupla
tupla =  ("Senai", True, 56, 74.6)
print(tupla)
print(type(tupla))

print(tupla[3])

#Dicionário
dicionario = {"nome":"SENAI", "logica":False, "num1":2, "num2": 1.5}

print(dicionario)

print(type(dicionario))
print(dicionario["logica"])

for chave in dicionario.keys():
    print(chave, "->", dicionario[chave])

dicionario.update({"nome":"Senai"})
dicionario.update({"nome":"Terça"})
print(dicionario)

del dicionario["logica"]
print(dicionario)

#Conjunto
conjunto = {"SENAI", False, 10, 2.69}
print(conjunto)
print(type(conjunto))
conjunto.add(23)
print(conjunto)
conjunto.discard("SENAI")
print(conjunto)
conjunto.clear
print(conjunto)

