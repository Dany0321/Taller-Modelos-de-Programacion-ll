d =  input("Ingrese un muero entre 1 y 7: ")
d = int(d)

if d == 2:
	d = "Lunes"
elif d == 3:
	d = "Martes"
elif d == 4:
	d = "Miercoles"
elif d == 5:
	d = "Jueves"
elif d == 6:
	d = "Viernes"
elif d == 7:
	d = "Sabado"
elif d == 1:
	d = "Domingo"
else: 
	d = 0
	print ("El numero no esta entre 1 y 7")

if d == 0:
	exit()
else:
	print ("El dia es: " + d)
