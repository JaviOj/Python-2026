# DATOS NUMERICOS
print("-------DATOS NUMERICOS-------- \n")
# Números enteros
edad = 32

# Números flotantes (reales)
estatura = 1.75  # el decimal utiliza punto y no coma 

# Números complejos
num_complejo = 4 + 2j #primera forma
otro_complejo = complex (4,2) #segunda forma

print(num_complejo) 
print(otro_complejo)

# Operación aritmetica básica (Área de un triangulo)
PI = 3.14159
base = 8
altura = 12.5

area = (base * altura) / 2
print(f"el area del triangulo es de {area} cm") 

# Formatos de salida de Números
print(f"El valor de PI es aproximadamente {PI:.2f}")

# Metodo de redondeo
print(round(PI, 3))
print(f"El area del triangulo es de {round(area)} cm")

# Transformaciones de números
print(float(edad))

print("-------CADENAS DE TEXTO-------- \n")

# Cadenas de texto (STRINGS)
carrera = "Ingenieria Civil en Informática" 
institucion = "Universidad de Los Lagos"

# Imprimir la posición del caracter
print(carrera[0]) 
""" Cada cadena se trata como lista,
imprimiendo la letra en la posición
del n° ingresado"""

print("Hola" * 4) # Multiplicacion de un string por entero
# print( "Hola" / 2 ) # No se puede hacer

print(carrera[0:10]) # Obtener subcadena (cortando strings), SUBSTRINGS

# Método Len() permite contar caracteres
print(len(institucion)) # Cuenta los espacios

#Arreglos (Listas)
print("-------Arreglos (Listas)-------- \n")
colores = ["Azul", "Rojo", "Verde", "Amarillo"] # Arreglo de strings
numeros = [1,2,3,4,5,6]                         # Arreglo numerico
lista_mixta = ["Gato", 2, 23.2, True]           # Arreglo mixto 

print(colores[0]) # Se imprime el primer elemento de la lista colores
print(numeros[-1]) # Se imprime el ultimo elemento de la lista números
print(lista_mixta)