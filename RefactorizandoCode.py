"""
Tenemos un recuento de los cocodrilos que viven en el rio Nilo :D
contamos:
- Contamos el num de dientes que tienen. 
- La longitud del cocodrilo.
- El peso del cocodrilo.

Solicitamos por consola las caracteristicas de cada cocodrilo.
'''
introduce datos: 250
5
75
....
....
....
'''
El resultado es u escrito en el que ponga para cada coccodrilo:
El cocodrilo num 1 pesa 250kg, mide 5m y tiene 75 dientes.
"""

# Funciones

def rellenarDatosCocodrilos(num):
    resultado = ""
    for numCocodrilo in range(num):
        peso = int(input("introduce el peso: "))
        longitud = int(input("introduce la longitud: "))
        numdientes = int(input("introduce el numero de dientes: "))
        resultado += f"\nEl cocodrilo numero {numCocodrilo} pesa {peso}kg, mide {longitud}m y tiene {numdientes} dientes :O"
    return resultado



# Code

listaNumDientes = []
listaLongCocodrilo = []
listaPesoCocodrilo = []

numCocodrilos = int(input("Cuantos cocodrilos vas a introducir? "))
print(rellenarDatosCocodrilos(numCocodrilos))