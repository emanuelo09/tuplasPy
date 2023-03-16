

"""Variable = "hola", 1, 1.25, True
print(Variable)"""


"""tupla = 2,
print(type(tupla))
#variable1 = 2

Lista = [] #Mutable
tupla = () #Inmutable"""


"""
Variable = ("hola", 1, 1.25, True)
print(Variable[1])
#Indexacion: index()
indice = Variable.index(1.25)
print(indice)
#Longitud: len()
longitud = len(Variable)
print(longitud)

numeros = (1, 2, 3, 4, 5, 6, 5, 2, 8, 1, 6, 7, 4, 4, 9, 2)
#Repeticion: count()
print(numeros.count(4))
#De tupla a lista: list()
listaNumeros = list(numeros)
print(listaNumeros)
#De lista a tupla: tuple()
tuplaNumeros = tuple(listaNumeros)
print(tuplaNumeros)

#Elemento mayor y menor: max(), min()
mayor = max(numeros)
menor = min(numeros)
print(f"El numero mayor de la tupla es {mayor}")
print(f"El numero menor de la tupla es {menor}")
print("El numero mayor es {0} y el menor es {1}".format(mayor, menor))

#%d Enteros
#%f Decimales
#%s Texto
print("El mayor es %d y el menor es %d"%(mayor, menor))

#Eliminar la tupla: No se puede, se tiene que convertir en lista y luego eliminarla

#Recorrer la tupla
for elemento in numeros:
    print(elemento)


for indic in range(len(numeros)):
    print(indic, numeros[indic])

#Recorrer de forma inversa    
for indi in range (len(numeros)-1,-1,-1):
    print(indi,"es la posicion del elemento", numeros[indi])

"""


Diccionario = { "Nombre": "Laura",
               "Edad": 5,
               "Sexo": "F"
               }

Diccionario_1 = dict(Nombre = "Laura",
                     Edad = 23,
                     Sexo = "F")

Diccionario_2 = {"Nombre": "Sandra",
                 "Telefono": 58963200,
                 "Apellido": "Gonzalez"
                 }

print(Diccionario)
print(Diccionario_1)

#Acceder -> get(clave) 
print(Diccionario.get("Edad"))
#Modificar
Diccionario["Edad"] = 89
print(Diccionario)

Diccionario["Apellido"] = "Suarez"
print(Diccionario)

#popitem()
#Diccionario.popitem()
#print(Diccionario)

#update()
Diccionario.update(Diccionario_1)
print(Diccionario)

Diccionario_2.update(Ocupacion = "Programadora")
print(Diccionario_2)

diccionario = { "Nombre": "Laura",
               "Edad": 5,
               "Sexo": "F"
               }

#Recorrer diccionario
for x in diccionario:
    print(x) #Imprime solo claves

for valores in diccionario:
    print(diccionario[valores]) #Imprime solo valores

for claves in diccionario:
    print(claves, diccionario[claves])

#keys(): obtener solo las claves
#values(): obtener solo los valores
#items(): obtener claves y valores

for claves in diccionario.keys():
    print(claves)

for clave in diccionario.values():
    print(clave)

for key in diccionario.items():
    print(key)
#O tambien funciona asi
for key, value in diccionario.items():
    print(key, value)




