#Un método es una función que permite crear nueva utilidades y/p darle un nuevo comportamiento al string.
""" Para aplicar un método se tiene que primero llamar a la cadena, luego . y el método a utilizar.
Cada método tiene su parentesis."""
#TRANSFORMAR ALL UN STRING A LETRAS MINUSCULAS.
cadena = "STAN eres Muy HERmoso PreCIoso"
print("Cadena normal, sin metodos:", cadena)
print ("---------------------------")
print("Lower:", cadena.lower()) #.Lower() transforma toda la cadena a minusculas.
print ("---------------------------")
print("Uper:", cadena.upper()) #.uper() transforma toda la cadena a mayusculas.
print ("---------------------------")

#MOSTRAR LA PRIMERA LETRA DEL STRING EN MAYUSCULAS Y EL RESTO DEL STRING EN MINUSCULAS.
print(cadena.capitalize())
print ("---------------------------")

#MOSTRAR LA PRIMERA LETRA DE CADA PALABRA EN MAYUSCULAS Y EL RESTO EN MINUSCULAS.
print(cadena.title())
print ("---------------------------")

#INVERITIR MAYUSCULAS A MINUSCULAS Y VICEVERSA.
print(cadena.swapcase())
print ("---------------------------")