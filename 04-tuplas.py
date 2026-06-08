# TUPLAS
print(f"-----------------TUPLAS-----------------")
# Creando tupla tipo string
estudiantes = ("d","b", "a","c")
print(type(estudiantes))
print(f"TUPLA: {estudiantes}")

# Creando tupla compleja con datos estructurados
datos = ([1,2,3,4,5], ("Queilen","Castro"), ("Universidad de Los Lagos", "AIEP"))

# Se puede consultar la posicion de un elemento 
print(datos[0])
print(datos)

# Con listas se pueden eliminar elementos
lista_asignaturas = ["Programacion", "Quimica", "Intro a la Mate"]
print(f"LISTA: {lista_asignaturas}")

lista_asignaturas.pop()
print(f"LISTA CON ELEMENTO ELIMINADO: {lista_asignaturas}")

# ¿Que pasa si quiero eliminar el ultimo elemento de una tupla?
"""estudiantes.pop()
print(f"TUPLA CON ULTIMO ELEMENTO ELIMINADO: {estudiantes}")

Al ser inmutable no se pueden agregar o eliminar elementos"""
# Vamos a consultar posición con metodo index
print(estudiantes.index("a"))

# Metodo sorted
print(sorted(estudiantes)) # Se transformó a lista

