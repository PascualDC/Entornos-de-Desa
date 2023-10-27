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
def preguntasChill(nombre):
    return int(input(f"introduce el/la {nombre}: "))

def rellenarDatosCocodrilos(num):
    resultado = ""
    for numCocodrilo in range(num):
        peso = preguntasChill("peso")
        longitud = preguntasChill("longitud")
        numdientes = preguntasChill("numdientes")
        resultado += f"\nEl cocodrilo numero {numCocodrilo+1} pesa {peso}kg, mide {longitud}m y tiene {numdientes} dientes :O"
    return resultado



# Code

listaNumDientes = []
listaLongCocodrilo = []
listaPesoCocodrilo = []

numCocodrilos = int(input("Cuantos cocodrilos vas a introducir? "))
print(rellenarDatosCocodrilos(numCocodrilos))