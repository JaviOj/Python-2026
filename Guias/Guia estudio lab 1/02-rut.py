"""Al desarrollar sistemas informaticos, los usuarios suelen ingresar datos con espacios
accidentales o formatos incorrectos. El sistema de la biblioteca de la ULagos recibio el
RUT de un estudiante, pero viene “sucio” con espacios al inicio, al final y con puntos
intermedios: “ 19.543.872-K ”...
Escribe un programa que:
a) Guarde el RUT original en una variable de tipo string.
b) Utilice el metodo propio de Python para eliminar los espacios en blanco de los
extremos.
c) Utilice un metodo propio de Python para eliminar los puntos (.).
d) Calcule el largo total del RUT ya limpio (sin espacios ni puntos) y muestre el
resultado por pantalla junto al RUT con su nuevo formato."""

# a) Guarde el RUT original en una variable de tipo string.
rut = " 19.543.872-K "
# b) Utilice el metodo propio de Python para eliminar los espacios en blanco de los extremos
rut_sin_espacios = rut.strip()
# c) Utilice un m´etodo propio de Python para eliminar los puntos (.).
rut_fin = rut_sin_espacios.replace(".","")
print(f"El largo del rut es de {len(rut_fin)} caracteres y el rut final es {rut_fin}")
