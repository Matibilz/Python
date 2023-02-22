"""Una cadena es una secuencia de caracteres.
Monty Python: es una cadena de caracteres; cada caracter ocupa un espacio en memoria inclusive los espacios en blanco.
Normalmente, la posición de una cadena comienza desde 0 hasta n, donde n es la dimension de la cadena.

Debanado/Slice de cadenas: Consiste en mostrar contenido de una cadena de manera segmentada, es decir, mostrar por medio de instrucciones un segmento de posiciones especificas.
Monty Python
01234567891011

[0:5] -> "Monty"  == Desde espacio 0 hasta espacio 5.
[ :3] -> "Mon" == Primeras tres letras.
[3: ] -> "hon" == Ultimas tres letras.
"""
numero = 10
cadena_nombre_persona = "Constanza Montoya Pantoja"
cadena_otro_nombre_persona = 'Conzanza "Montoya" Pantoja'
print (cadena_nombre_persona, " | ",  cadena_otro_nombre_persona)

#Escapar caracteres, string itera.
mi_nombre =  " Matias \"Bilz\" Gonzalez" #La barra invertida permite colocar dentro del string comillas dobles en un string que esta contenido por comillas dobles, cosa que en otro caso no es posible.
print (mi_nombre)
nombre_azar = 'Constanza\' Montoya\' Pantoja' #Otro tipo de string itera.
otro_string = "Esto es un ejemplo\tde cadena de texto" #\t es una tabulación. (4 espacios)
print (otro_string) 

#CONCATENAR CADENAS DE CARACTERES.
cadena_saludo = "Hola, como estas"
cadena_nombre = "Matias Gonzalez"
print(cadena_saludo+" "+cadena_nombre) #concatenación de dos cadenas.

#IMPRIMIR N VECES UN STRING.
print((cadena_saludo+"\n")*5) #La suma y a la multiplicación son los unicos operadores aritmeticos que permiten esto.

#CONCATENAR UN STRING A UN MENSAJE.
print("Hola: " + cadena_nombre) #es posible tambien print("Hola: ", cadena_nombre)

#CONCATENAR UN NUMERO A UN STRING.
print("Hola: ", cadena_nombre, " | Dorsal: ", numero )

#CONVERITR UNA VARIABLE NUMERICA A STRING. Función str.
print (type(numero)) #ok, pero es un dato tipo entero, se necesita como string, para esto.
print ("Numero es: ", numero, "y es un tipo de dato:", type(str(numero)))
