# SETS
print(f"-----------------SETS-----------------")

# Creando los primeros conjuntos
colores_primarios = {"azul","rojo","amarillo"}
colores_secundarios = set({"naranja", "verde", "violeta"})

print(f"CONJUNTO 1: {colores_primarios}")
print(f"CONJUNTO 2 : {colores_secundarios}")

# Creando un conjunto nuevo con duplicados
# En los sets no se consideran duplicados
colores_nuevos = {"azul","rojo","celeste"}
print(f"CONJUNTO 3: {colores_nuevos}")

# Agregando elementos a set
colores_nuevos.add("cafe")
print(f"CONJUNTO 3 ACTUALIZADO: {colores_nuevos}")

# Eliminando un elemento del set
colores_nuevos.discard("cafe")
print(f"CONJUNTO 3 ACTUALIZADO SIN EL COLOR CAFE: {colores_nuevos}")

# Aplicando el metodo intersection()
interseccion = colores_primarios.intersection(colores_nuevos)
print(f"CONJUNTO INTERSECTADO: {interseccion}")