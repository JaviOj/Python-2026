toma1 = float(input("Administrador ingrese el tiempo de respuesta numero 1: "))
toma2 = float(input("Administrador ingrese el tiempo de respuesta numero 2: "))
toma3 = float(input("Administrador ingrese el tiempo de respuesta numero 3: "))
tiempo_respuesta = []
tiempo_respuesta.append(toma1)
tiempo_respuesta.append(toma2)
tiempo_respuesta.append(toma3)
promedio = (tiempo_respuesta[0] + tiempo_respuesta[1] + tiempo_respuesta[2]) / len(tiempo_respuesta)
min_t = min(tiempo_respuesta)
max_t = max(tiempo_respuesta)
brecha = max_t - min_t
print(f"La lista de datos tiene los siguientes datos: {tiempo_respuesta}\npromedio: {promedio}\nla brecha es de {brecha}")

