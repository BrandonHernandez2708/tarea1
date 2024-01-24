entrada=input("ingrse un numero: ")
if entrada.isdigit(): #isdigit: comprueba si el dato ingresa es texto
    print("Has ingresado un número:")
elif len(entrada) == 1: #len: cuenta el numero de caracteres ingresado 
    print("Has ingresado un caracter,ingrsalo como un char")
elif entrada.lower() == "true" or entrada.lower() == "false": #lower: compara que el dato ingresado sea el mismo que pide la condicion 
    print("Has ingresado un booleano, ingrésalo como un bool")
else:  print("Has ingresado un texto, ingrésalo como un string.")
     