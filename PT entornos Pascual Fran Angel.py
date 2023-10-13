# 1 ¿Qué hace este código?
"""
Este codigo se encarga de hacer medias, primero solicita la cantidad de numeros(entre 1-5) con las que vas a hacer las medias. 
Luego tienes que escribir los numeros y el codigo se encarga de hacer la media
"""
#2 ¿Cómo lo has refactorizado? Explica los cambios que le has realizado y el motivo.
"""
Hemos creado una función llamada medias que te divide la suma de los valores introducidos entre la cantidad de valores, a parte hemos hecho que la cantidad de números
introducidos te determine cuántas veces te pide un valor en un while y por último se imprime el resultado. 
"""
#3 Inventa un enunciado para el código resultante relacionado con Halloween.
"""
La temática fue de CastleVania. El ejercicio finalizado esta al final del codigo, mientras bajas revisando el codigo podrás ver el proceso de mejora del ejercicio.
"""

"""
Versión original del código:
#Funciones
def abcde(a,b,c,d,e):
    s = a+b+c+d+e
    t = s/5
    return t
def abcd(a,b,c,d):
    s = a+b+c+d
    t = s/4
    return t
def abc(a,b,c):
    s = a+b+c
    t = s/3
    return t
def ab(a,b):
    s = a+b
    t = s/2
    return t   
  #Código principal  
x = int(input())
if x==1:
    a = int(input())
    print(1)
elif x==2:
    a = int(input())
    b = int(input())
    print(ab(a,b))
elif x==3:
    a = int(input())
    b = int(input())
    c = int(input())
    print(abc(a,b,c))
elif x==4:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(abcd(a,b,c,d))
elif x==5:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(abcde(a,b,c,d,e))
else:
    print("no")
"""


"""
Versión 1 del código (Refactorizada)
# Funciones 
def medias():
    resultado = suma/divisorMedia
    return resultado
#Primary Code
suma = 0
cantidadNum = int(input("De cuantos numeros quieres hacer la media: "))
divisorMedia = cantidadNum
#print(divisorMedia)
while cantidadNum > 0:
    solicitaNum = int(input("Introduce un numero --> "))
    suma = suma + solicitaNum
    cantidadNum -= 1

print(f"La media de los números introducidos es {medias()}")
"""


#3 Inventa un enunciado para el código resultante relacionado con Halloween.
#Versión 2 del código (refactorizada y ambientada en halloween)
# Funciones 
def medias():
    resultado = suma/divisorMedia
    return resultado
#Primary Code
suma = 0
cantidadNum = int(input("Eres un Belmont, y te toca enfrentarte a Dracula a tí en esta generación. Introduce la cantidad de plantas que hay entre Dracula y tú: "))
divisorMedia = cantidadNum
#print(divisorMedia)
while cantidadNum > 0:
    solicitaNum = int(input("Introduce la cantidad de monstruos que hay en esta planta: "))
    suma = suma + solicitaNum
    cantidadNum -= 1
print(f"La media de los monstruos que has vencido en todo el castillo por planta es {medias()}")