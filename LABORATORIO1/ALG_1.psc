Algoritmo ALG_1
	Definir precioun, cantidad, valorbase, descuentoIt, descuentoUla, valorfinal Como Real
	definir promoit, ulagos Como Caracter
	Escribir "Ingrese los siguientes datos para determinar si se aplica algun descuento a su compra"
	Repetir
		Escribir "Ingrese el valor unitario de su compra"
		leer precioun
		Escribir "Ingrese la cantidad de completos que llevará"
		leer cantidad
	Hasta Que precioun>0 y cantidad>0
	
	valorbase <- precioun * cantidad
	
	Repetir
		Escribir "Su producto es un Completo Italiano? (escriba si / no )"
		leer promoit
		promoit = minusculas (promoit)
		Escribir "Usted pertenece a la Universidad de Los Lagos? (escriba si / no )"
		leer ulagos
		ulagos = minusculas (ulagos)
	Hasta Que promoit = "si" o promoit = "no" o ulagos = "si" o ulagos = "no" 
	
	Si promoit = "si" Entonces
		descuentoit <- valorbase * 0.9
	SiNo
		Si ulagos = "si" Entonces
			descuentoUla <- valorbase * 0.95
		Fin Si
	Fin Si
	
	Si promoit = "si" y ulagos = "si" Entonces
		valorfinal <- descuentoit * 0.95
		Escribir "Usted tiene una compra de monto $", valorbase, " pero pretenece a la Universidad de Los Lagos por lo que a su compra se le disminuye $", valorbase * 0.05, " pesos " 
		Escribir "y ademas compró una promo Italiano, por lo que disminuye en $", descuentoit * 0.1, " pesos, teniendo una compra de $",  valorfinal, " pesos en total"
	Fin Si
	
	Si  promoit = "si" y ulagos = "no" Entonces
		valorfinal <- descuentoit 
		Escribir "Usted tiene una compra de monto $", valorbase, " pero compró una promo italiano por lo que a su compra se le disminuyen $", valorbase * 0.1, " pesos" 
		Escribir " Finalmente usted debe cancelar $", valorfinal
	SiNo
		Si  promoit = "no" y ulagos = "si"  Entonces
			valorfinal <- descuentoUla
			Escribir "Usted tiene una compra de monto $", valorbase, " pero retenece a la Universidad de Los Lagos por lo que a su compra se le disminuye en $", valorbase * 0.05, " pesos "
			Escribir " Finalmente usted debe cancelar $", valorfinal
		SiNo
			Escribir "Su compra no aplica descuentos por lo que debe pagar $", valorbase
		Fin Si
	Fin Si
	
	
	
FinAlgoritmo
