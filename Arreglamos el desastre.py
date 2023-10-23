""" 
El color de la camiseta establece el tipo de trabajo que desempeñas dentro de la nave:
Liderazgo -> Dorada
Ciencia -> Azul
Ingeniería -> Roja
"""

""" 
Para hacer una estimación del porcentaje de tripulantes de cada tipo se estudia el color 
del traje de 10 de ellos.
Refactoriza: 
    - Cambiándole el nombre contadorTrajeAzul las variables.
    - Creando funciones para solicitar el color del traje y hacer el recuento.
    - Con un bucle para no repetir código.
    - Imprime el resultado del recuento, en porcentajes (como indica el enunciado).
    - Mejora la función de recuento.
"""

def calcularPorcentaje(contador, numElementos):
    return (contador/numElementos)*100

def solicitarColorTraje():
    return input("¿De qué color es tu traje? ")

contadorTrajeDorado = 0
contadorTrajeAzul = 0
contadorTrajeRojo = 0

numTripulantes = 10

for tripulante in range(numTripulantes):
    color = solicitarColorTraje()
    if color == "dorado":
        contadorTrajeDorado += 1
    elif color == "azul":
        contadorTrajeAzul += 1
    elif color == "rojo":
        contadorTrajeRojo += 1

porcentajeDorado = calcularPorcentaje(contadorTrajeDorado, numTripulantes)
porcentajeAzul = calcularPorcentaje(contadorTrajeAzul, numTripulantes)
porcentajeRojo = calcularPorcentaje(contadorTrajeRojo, numTripulantes)

print(f'Hay {porcentajeDorado}% de trajes dorados,{porcentajeAzul}% de trajes azules,{porcentajeRojo}% de trajes rojos')