temperaturas = [12.5,14.2,11.8]
promedio = (sum(temperaturas))/len(temperaturas)
print(f"El promedio de las 3 temperaturas es de {promedio:.2f}°")
diferencia = (temperaturas[1])-(temperaturas[2]) #se puede usar max()min() 
print(f"La diferencia es de {diferencia:.2f}°")
