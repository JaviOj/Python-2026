# LISTAS

# Primera forma de declarar listas (lista mixta)
lista1 = ["a", 6, True]
ramos = [] # Lista vacia

# Segunda forma de declarar listas (lista numerica)
n = list([5,4,3,2,1])

print(type(n))
print(type(lista1))

# Metodo listas
# 01-Count() - contar la cantidad de concurrencias de un elemento
print(lista1.count(6))
print(ramos)

#Agregar elementos al final de una lista
ramos.append("Química")
print(ramos)

ramos.append("Habilidades comunicativas")
print(ramos)

ramos.append("Programación")
print(ramos)

# Otra forma de insertar un elemento a la lista
ramos.insert(0, "Introducción a la matemática")
print(ramos)

# Modificar un elemento en especifico de una lista
ramos[2] = "Habilidades comunicativas para ingenieros e ingenieras"
print(ramos)

# Eliminar el ultimo elemento de una lista
ramos.pop ()
print(ramos)

# Ordenar los elementos de una lista de forma descendente a ascendente
ramos.sort()
print(ramos)

n.sort()
print(n)

# Ordenar elementos de una lista segun cantidad de caracteres de cada elemento
ramos.sort(key=len)
print(ramos)

# Método Extend, extender una lista a partir de otra
ramos_segundo_semestre = ["Ciudadania","Algebra","Introducción a la física"]
print(ramos_segundo_semestre)

ramos.extend(ramos_segundo_semestre)
print(ramos)

# Aplicando metodo index
print(ramos_segundo_semestre.index("Algebra"))