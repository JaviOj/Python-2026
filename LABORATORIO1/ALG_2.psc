Algoritmo ALG_2
	Definir cat1, cat2, hipo como real
	Repetir
		Escribir "Ingrese las medidas de los catetos de su triangulo para determinar la Hipotenusa y clasificarlo según sus medidas"
		Escribir "Ingrese la medida del cateto 1"
		leer cat1
		Escribir "Ingrese la medida del cateto 2"
		leer cat2
	Hasta Que cat1 > 0 y cat2 > 0
	
	hipo <- raiz (cat1^2 + cat2^2)
	
	Si cat1 = cat2 Entonces
		Escribir "El triangulo tiene una hipotenusa de ", hipo, " y se clasifica como Isósceles ya que sus dos catetos son iguales"
	SiNo
		Si (cat1 <> cat2) y (cat1 <> hipo) y (cat2 <> hipo) Entonces
			Escribir "El triangulo tiene una hipotenusa de ", hipo, " y se clasifica como Escaleno ya que todos sus lados son distintos"
		SiNo
			Escribir "No está en ninguna categoria considerada"
		Fin Si
	Fin Si
FinAlgoritmo
