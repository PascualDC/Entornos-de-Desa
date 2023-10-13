def generarMonstruos(numMonstruosAGenerar):
    for monstruo in range(numMonstruosAGenerar):
        nomMonstruo = input("Dale nombre --> ")
        fuerzaMonstruo = int(input("Dale poder --> "))
        print(f"Toma un monstruo llamado {nomMonstruo} con {fuerzaMonstruo} de fuerza.")

numMonstruos = int(input("¿Cuantos monstruos necesitas? "))
generarMonstruos(numMonstruos)

# if numMonstruos == 1:
#     nomMonstruo = input("Como vas a llamar a tu monstruo : ")
#     fuerzaMonstruo = int(input("Selecciona la fuerza de tu monstruo "))
# elif numMonstruos == 2:
#     nomMonstruo = input("Como vas a llamar a tu monstruo : ")
#     fuerzaMonstruo = int(input("Selecciona la fuerza de tu monstruo "))
#     nomMonstruo2 = input("Como vas a llamar a tu monstruo : ")
#     fuerzaMonstruo2 = int(input("Selecciona la fuerza de tu monstruo "))
# elif numMonstruos == 3:
#     for monstruo in range(3):
#         nomMonstruo = input("Como vas a llamar a tu monstruo : ")
#         fuerzaMonstruo = int(input("Selecciona la fuerza de tu monstruo "))
#         print(f"Toma un monstruo llamado {nomMonstruo} con {fuerzaMonstruo} de fuerza.")

# else:
#     print("Si quieres mas de 3 o menos de 1, ve a buscar monstruos a otro siteo")

