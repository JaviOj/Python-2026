# 11-BUCLES

from colorama import init, Fore
init() 

print(Fore.MAGENTA + "====UTILIZANDO BUCLES====\n")

# Bucle while
edad = 15
num = 0

# BUCLE INFINITO
# while edad < 18:
#   print("Eres menor de edad, no puedes manejar")

# BUCLE INFINITO n° 2
#while True:
#    print(num)
#    num =num + 2

# Bucle while
# Impresion de numeros de 0 al 100 incrementando de 2 en 2
while num<= 100:
    print(num)
    num += 2
print(Fore.RED + "Primer bucle terminado!")
# Impresion de numeros de 100 al 200 + condicion ELSE
while num <= 200:
    print(num)
    num += 2
else:
    print("Mi condicion es igual o mayor a 200")
print(Fore.CYAN + "Segundo bucle terminado!")

# Combinar while con un if dentro
while num <= 300:
    print(num)
    num += 2
    if num == 250:
        print("Mi condicion es igual a 250")
print(Fore.GREEN + "Tercer bucle terminado!")

# Utilizando break
# La palabra break quiebra un bucle solo se puede usar en conjunto con while
while num <= 400:
    print(num)
    num += 2
    if num == 350:
        print(Fore.MAGENTA + "Se detiene el bucle")
        break
print(num)
print(Fore.MAGENTA + "Cuarto bucle terminado!")

# Utilizar el continue
num = 0
while num <= 50:
    num += 1
    if num == 40:
        continue
    print(num)
print(num)

# Bucle infinito + break 
"""while True:
    parametro = input("Ingrese la palabra: ")
    if parametro == "exit":
        break
    else:
        print(parametro)
"""
# Bucle FOR
# For n° 1
print(f"--------BUCLE FOR-----------")
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

# Iterando una lista
listita = [1,2,3,4,5,6,7,8,9,10]
for i in listita:
    print(i)
print(Fore.MAGENTA + "\n2° bucle for")
# Iterando de una tercera forma 
for i in range(1,101):
    print(i)