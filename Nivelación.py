BM_1 = 0.0
BM_2 = 0.0 
TotalVistas = 0
i = 0
SumaPractica = 0.0
Teorica = 0.0
Error = 0.0
Ajuste = 0.0 

BM_1 = float (input("Ingresar la cota de partida (BM_1): "))
BM_2 = float (input("Ingresar la cota final (BM_2): "))
TotalVistas = int(input("Ingrese el total de vistas (V+ y V-): "))

VistasAtras = [0,0] * TotalVistas
VistasAdelante = [0,0] * TotalVistas

i = 0
while i < TotalVistas:
    if i % 2 == 0:
        print("Vista hacia adelante", i)
        VistasAdelante[i] = float(input())

        opcion = input("¿Desea ingresar una vista intermedia? (1/0): ")

        while opcion.lower() == "1" or opcion.lower() == "si":
            print("Vista intermedia", i)
            VistaIntermedia = float(input())    #Guarda la vista intermedia 

            opcion = input("¿Desea ingresar otra vista intermedia?  (Si/No): ")
    else:
        print("Vista hacia atrás", (i + 1))
        VistasAtras[(i + 1)]
    
    i += 1

#Sumatoria práctica 

SumaVistasAtras = 0.0
SumaVistasAdelante = 0.0

i = 0
while i < TotalVistas:
    if i % 2 == 0:
        SumaVistasAdelante += VistasAdelante[i]
    else:
        SumaVistasAtras += VistasAtras [(i +1)]
    
    i += 1

SumaPractica = SumaVistasAdelante - SumaVistasAtras

Teorica = BM_1 - BM_2
Error = Teorica - SumaPractica
Ajuste = Error / TotalVistas

i = 0
while i < TotalVistas:
    if i % 2 == 0:
        VistasAdelante [i] += Ajuste
    else: 
        VistasAtras [(i + 1)]
    
    i += 1
    

print ("Resultados: ")
print ("Sumatoria práctica: ", SumaPractica)
print ("Sumatoria teórica: ", Teorica)
print ("Error: ", Error)
print ("Error de ajuste: ", Ajuste)

print ("Datos corregidos: ")
i = 0
j = 0 
while i < TotalVistas:
    if i % 2 == 0:
        print("Vistas hacia atrás: ", (i + 1))
        print("Vistas hacia adelante: ", (i + 1))
        j += 1

    i += 1
    

