#Substring se le suele llamar al debanado de cadenas.
cadena_string = "Este es un ejemplo de Substring (Debanado de cadenas)."

#TAMAÑO DE UNA CADENA.
print (len(cadena_string)) #Len permite conocer el tamaño de una cadena.

#MOSTRAR UN CARACTER DE UN STRING.
""" El debanado de caracteres utiliza dos parametros, una posición inicial y una posición final.
Los parametros pueden ser un numero o una variable."""
print(cadena_string[0]) #Imprimir el caracter de la posición 0.
print(cadena_string[0:50]) #Imprimir los caracteres que van desde la posición 0 hasta la posición 49.
print(cadena_string[ :10]) #Imprimir los caracteres hasta la posición 9.
print (cadena_string[10: ]) #Imprimir los caracteres desde la posición 10 hasta la posición final de la cadena.
print(cadena_string[-1]) #Imprime el ultimo caracter.
#Cuando mi parametro es un numero negativo, la cuenta se realiza desde el final de la cadena.