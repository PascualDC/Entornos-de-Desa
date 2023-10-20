# FUnciones
"""
def solicitarDia():
	return int(input("Introduce un día del mes: "))
def solicitarMes():
	return int(input("Introduce un mes: "))
def solicitarAnio():
	return int(input("Introduce un año: "))
"""

def solicitarNum(texto):
	return int(input(f"introduce un {texto}: "))

def mesNumericoATexto(numMes):
	listaMeses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
	return listaMeses[numMes-1]

# Codigo principal

dia = solicitarNum("dia del mes")
mesNum = solicitarNum("mes del anio")
mes = mesNumericoATexto(mesNum)

anio = solicitarNum("año")

esValido = False
mes28DiasNoValido = mes == "febrero" and dia > 28
mes30DiasNoValido = (mes == "septiembre" or mes == "noviembre" or mes == "abril" or mes == "junio")and dia > 30
mes31DiasNoValido = dia > 31
"""
if anio > 2025:
	esValido = False
else:
    if mes == "febrero" and dia > 28:
        esValido = False
    elif (mes == "septiembre" or mes == "noviembre" or mes == "abril" or mes == "junio")and dia > 30:
        esValido = False
    elif dia > 31:
        esValido = False
"""
if anio < 2025:
	if (anio < 2025) or not (mes28DiasNoValido or mes30DiasNoValido or mes31DiasNoValido):
		esValido = True
else:
    esValido = False
	
print(f"El mes {mes} es {mesNumericoATexto(mesNum)}")

""" 

d2 = int(input("Introduce un día del mes: "))
m2 = int(input("Introduce un mes: "))
a2 = int(input("Introduce un año: "))

if m2 == "febrero" and d2 > 28:
	print("No es valido")
elif (m2 == "septiembre" or m2 == "noviembre" or m2 == "abril" or m2 == "junio")and d2 > 30:
	print("No es valido")
elif d2 > 31:
	print("No es valido")
	
if a2 > 2025:
	print("No es valido")
	
d3 = int(input("Introduce un día del mes: "))
m3 = int(input("Introduce un mes: "))
a3 = int(input("Introduce un año: "))

if m3 == "febrero" and d3 > 28:
	print("No es valido")
elif (m3 == "septiembre" or m3 == "noviembre" or m3 == "abril" or m3 == "junio")and d3 > 30:
	print("No es valido")
elif d3 > 31:
	print("No es valido")
	
if a3 > 2025:
	print("No es valido")
	
d4 = int(input("Introduce un día del mes: "))
m4 = int(input("Introduce un mes: "))
a4 = int(input("Introduce un año: "))

if m4 == "febrero" and d4 > 28:
	print("No es valido")
elif (m4 == "septiembre" or m4 == "noviembre" or m4 == "abril" or m4 == "junio")and d4 > 30:
	print("No es valido")
elif d4 > 31:
	print("No es valido")
	
if a4 > 2025:
	print("No es valido")

	""" 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# funciones

def restricionesDia(dia,mes):
    resultado = "No es correcto"
    if dia > 31:
        resultado
    elif mes and dia > 30:
        resultado 
    else:
        print("Es correcto")
    
#Primary code

# listaMeses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
# listaMeses30 = ["septiembre", "noviembre", "abril", "junio"]

# dia1 = int(input("Introduce un día: "))

# mes1 = int(input(("Escribe un mes: ")))
# posicionMes = listaMeses.index(mes1)

# restricionesDia(dia1,posicionMes)
# anio1 = int(input("Escribe un año: "))

# print(restricionesDia)

