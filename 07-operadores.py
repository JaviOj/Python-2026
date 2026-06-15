# Operadores en python
a = 10
b = 5
c = 4
d = 10
print("===OPERADORES ARITMETICOS===")
print(f"La suma entre la variable a y b es: {a+b}")
print(f"La resta entre la variable a y b es: {a-b}")
print(f"La multiplicacion entre la variable a y b es: {a*b}")
print(f"La división entre la variable a y b es: {a/b}")
print(f"El módulo entre la variable a y b es: {a%b}")
print(f"El coeficiente entre la variable b y c es: {b//c}")
print(f"El resultado entre la variable b elevado a c es: {b ** c}")

# Se puede hacer esta operacion?
print("Hola" * ((int(10*2)/5)),"\n")

print("\n===OPERADORES DE COMPARACIÓN===") # Booleano

print(a == b) # op igualdad
print(a != b) # op Desigualdad
print(a > b) # op mayor que
print(a < b) # op mayor que
print(c >= d) # op mayor o igual que
print(c <= d) # op menor o igual que

print("\n===OPERADORES LÓGICOS===") 
"""Trabajaremos con el siguiente ejemplo:
Tenemos un vehículo que tiene bencina (variable bencina) y una opción que dice 
si esta encendido o no el vehiculo (variable encendido).
Dependiendo del estado de cada variable, se irá cambiando por False o True."""

# Variables Booleanas
bencina = True
encendido = True
# if = si 
# else = sino

# Utilizando operador AND
if bencina and encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")

# Utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")