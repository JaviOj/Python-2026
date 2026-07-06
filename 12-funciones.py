
# Ejemplo de función simple
def multiplicacion(x):# parametro puede tomar cualquier valor
    return x * 10 

y = multiplicacion(20) # Utilizandolo en variable
print(f"El resultado de la función es {y}")

# Segundo ejemplo
def saludo(nombre):
    print(f"Hola mi nombre es {nombre}")

saludo("Tomas")

# Se puede utilizar más de 1 parametro
def suma(a,b):
    return a + b
# Llamada a la funcion con argumentos posicionales
resultado = suma(2,3) # El orden si importa
print(resultado)

# Definicion de la funcion "resta" con parametros por defecto
def resta(a,b=5):
    return a - b

resultado1 = resta(6)
print("Resultado 1 (b por defecto): ", {resultado1})

resultado2 = resta(4,4) # a = 4, b = 4
print("Resultado 2 (b personalizado): ", {resultado2})

# Argumentos por nombre
def calcular_potencia(base,exponente):
    return base ** exponente

# Llamada con argumentos por nombre (orden no importa)
resultado3 = calcular_potencia(exponente = 2, base = 3)
print("Resultado potencia:",resultado3)

# RECURSIVIDAD

# Ejercicio factorial 
def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r *=i
        i +=1
    return r

print(factorial_normal(5))

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

print(factorial_recursivo(5))

def fibonacci_recursivo(n):
    # Casos base (0 y 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Ejemplo: 5to número de Fibonacci (Se empieza del cero)
print(f"5to Número de Fibonacci: {fibonacci_recursivo(5)}")

def fibonacci_iterativo(n):
    # Casos base (0 y 1)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b  # Se actualizan los valores
    return a

# Ejemplo: 5to número de Fibonacci (Se empieza del cero)
print(f"5to Número de Fibonacci: {fibonacci_iterativo(5)}")
