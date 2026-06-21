nombre_estudiante = input("Ingrese su nombre y apellido, separandolos por 1 espacio: ")
nombre_estudiante = nombre_estudiante.strip()
nombre_estudiante = nombre_estudiante.lower()
nombre_estudiante = nombre_estudiante.replace(" ",".")

print(nombre_estudiante + "@alumnos.ulagos.cl")
