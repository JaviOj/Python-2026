print("==== MENÚ ====")
print("1. Hamburguesa")
print("2. Pizza")
print("3. Completo Italiano")

opcion = input("Por favor ingrese una opcion (1-3): ")
match opcion:
    case "1":
        print("Has elegido Hamburguesa")
    case "2":
        print("Has elegido Pizza")
    case "3":
        print("Has elegido Completo Italiano")
    case _:
        print("Opcion no valida. Por favor, elige entre el 1 y 3 ")


mes = 4 #Abril
match mes:
    case 12 | 1 | 2:
        print("Verano")
    case 3 | 4 | 5:
        print("Otoño")
    case 6 | 7 | 8:
        print("Invierno")
    case 9 | 10 | 11:
        print("Primavera")
    case _: 
        print("Ingrese un mes valido del 1 al 12")

x = [1,2,3]
match x: 
    case [a, b, c]:
        print(f"Elementos de la lista: {a}, {b}, {c}")

datos = {
    "Nombre" : "",
    "Edad" : ""
}

match datos:
    case {"nombre": n, "edad" : e}
        print

# Guards
# Ejemplo: saber si un numero es par o impar 
valor = 6
match valor:
    case x if x % 2 == 0:
        print(f"{valor} es un número par")
    case x if x % 2 != 0:
        print(f"{valor} es un número impar")