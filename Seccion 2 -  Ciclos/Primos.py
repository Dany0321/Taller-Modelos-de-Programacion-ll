import math
n = float(input ("Ingrese un numero : "))
aux = 0
i = 2
if (n - int(n)) != 0 or n <= 1:
	print("El numero debe ser un natural positivo")

else:
	
	while aux == 0 and i < n:
		if (((n/i) - int(n/i)) == 0) :
			aux = aux + 1
		i = i + 1
		
	if aux == 0:
		print("El numero es primo")
	else:
		print("El numero es compuesto")
