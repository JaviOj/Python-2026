print("Para calcular su promedio de notas ingrese individualmente cada una")
nota1 = float(input("Ingrese su nota del laboratorio n° 1 para calcular el promedio: "))
nota2 = float(input("Ingrese su nota del laboratorio n° 2 para calcular el promedio: "))
nota3 = float(input("Ingrese su nota del laboratorio n° 3 para calcular el promedio: "))

notas = []
notas.append(nota1)
notas.append(nota2)
notas.append(nota3)

promedio = ((notas[0])*0.4)+((notas[1])*0.4)+((notas[2])*0.2)
print(f"Las notas ingresadas fueron: {notas}\nLa nota final es de: {promedio:.2f}")