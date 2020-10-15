'''
Created on 8 oct. 2020

@author: JUAN MORENO
'''

# Import libraries 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from builtins import len


def main():
    data = pd.read_csv('Dataset_finalSonia.csv')
    datos1 = np.array(data)
    tamFila = datos1.shape[0]
    
    
    #LIMPIEZA DE CADA DATO
    
    
    #ATRY TO LECTURE
    print("ATRY TO LECTURE")
    #Grafica de cajas y bigotes para Atry To Lecture
    data[['Atry to lecture', 'Gano']].boxplot(by='Gano')
    plt.title('Grafica Atry to lecture')
    plt.show()
    
    print(isinstance(datos1[0][9], int))  # Es para saber el tipo de dato
  
    #Sacar Promedio de Atry to Lecture
    i = 0
    media9, cont9, suma9 = 0, 0, 0
    while i < tamFila:
        if datos1[i][9] <= 5 and datos1[i][9] >= 0 :
                suma9 = suma9 + datos1[i][9]
                cont9 += 1
        i += 1
             
    media9 = suma9 / cont9
    print("media ", media9, "  cuenta ", cont9)
    
    #Reemplazar valores atipicos de Atry to Lecture
    numeroRemplazo9 = round(media9)
    i = 0
    while i < tamFila:
        if datos1[i][9] > 5 :
                datos1[i][9] = numeroRemplazo9
        i += 1
    
    #Imprimir columna de Atry to Lecture
    i = 0
    while i < tamFila:
        print(datos1[i][9])
        i += 1
    
    
    
   
    
    #ONLY LECTURE
    print("ONLY LECTURE")
    #Grafica de cajas y bigotes para only lecture
    data[['only lecture', 'Gano']].boxplot(by='Gano')
    plt.title('Grafica only lecture')
    plt.show()
    
    print(isinstance(datos1[0][8], int))  # Es para saber el tipo de dato
  
    #Sacar Promedio de only lecture
    i = 0
    mediaNO8, mediaSI8, contNO8, contSI8, sumaNO8, sumaSI8 = 0, 0, 0, 0, 0, 0
    while i < tamFila:
        if datos1[i][8] <= 5 and datos1[i][8] >= 0 and datos1[i][31] == "NO":
                sumaNO8 = sumaNO8 + datos1[i][8]
                contNO8 += 1
        if datos1[i][8] <= 52 and datos1[i][8] >= 0 and datos1[i][31] == "SI":
                sumaSI8 = sumaSI8 + datos1[i][8]
                contSI8 += 1
        i += 1
             
    mediaNO8 = sumaNO8 / contNO8
    print("NO->   media ", mediaNO8, "  cuenta ", contNO8)
    mediaSI8 = sumaSI8 / contSI8
    print("SI->   media ", mediaSI8, "  cuenta ", contSI8)
    
    #Reemplazar valores atipicos de only lecture
    numeroRemplazoNO8 = round(mediaNO8)
    numeroRemplazoSI8 = round(mediaSI8)
    i = 0
    while i < tamFila:
        if datos1[i][8] > 5 and datos1[i][31] == "NO":
                datos1[i][8] = numeroRemplazoNO8
        if datos1[i][8] > 52 and datos1[i][31] == "SI":
                datos1[i][8] = numeroRemplazoSI8
        i += 1
    
    #Imprimir columna de only lecture
    i = 0
    while i < tamFila:
        print(datos1[i][8])
        i += 1
    
    
    #EXPLORE
    print("EXPLORE")
    #Grafica de cajas y bigotes para explore
    data[['explore', 'Gano']].boxplot(by='Gano')
    plt.title('Grafica explore')
    plt.show()
    
    print(isinstance(datos1[0][10], int))  # Es para saber el tipo de dato
  
    #Sacar Promedio de explore
    i = 0
    mediaSI10, contSI10, sumaSI10 = 0, 0, 0
    while i < tamFila:
        if datos1[i][10] <= 39 and datos1[i][10] >= 0 and datos1[i][31] == "SI":
                sumaSI10 = sumaSI10 + datos1[i][10]
                contSI10 += 1
        i += 1
             
    mediaSI10 = sumaSI10 / contSI10
    print("SI->   media ", mediaSI10, "  cuenta ", contSI10)
    
    #Reemplazar valores atipicos de explore
    numeroRemplazoSI10 = round(mediaSI10)
    i = 0
    while i < tamFila:
        if datos1[i][10] > 39 and datos1[i][31] == "SI":
                datos1[i][10] = numeroRemplazoSI10
        i += 1
    
    #Imprimir columna de explore
    i = 0
    while i < tamFila:
        print(datos1[i][10])
        i += 1
        
    
    #AGE
    print("AGE")
    #Grafica de cajas y bigotes para age
    data[['age', 'Gano']].boxplot(by='Gano')
    plt.title('Grafica age')
    plt.show()
    
    print(isinstance(datos1[0][21], int))  # Es para saber el tipo de dato
  
    #Sacar Promedio de age
    i = 0
    mediaNO21, mediaSI21, contNO21, contSI21, sumaNO21, sumaSI21 = 0, 0, 0, 0, 0, 0
    while i < tamFila:
        if datos1[i][21] <= 53 and datos1[i][21] >= 15 and datos1[i][31] == "NO":
                sumaNO21 = sumaNO21 + datos1[i][21]
                contNO21 += 1
        if datos1[i][21] <= 68 and datos1[i][21] >= 16 and datos1[i][31] == "SI":
                sumaSI21 = sumaSI21 + datos1[i][21]
                contSI21 += 1
        i += 1
             
    mediaNO21 = sumaNO21 / contNO21
    print("NO->   media ", mediaNO21, "  cuenta ", contNO21)
    mediaSI21 = sumaSI21 / contSI21
    print("SI->   media ", mediaSI21, "  cuenta ", contSI21)
    
    #Reemplazar valores atipicos de age
    numeroRemplazoNO21 = round(mediaNO21)
    numeroRemplazoSI21 = round(mediaSI21)
    i = 0
    while i < tamFila:
        if datos1[i][21] > 53 and datos1[i][31] == "NO":
                datos1[i][21] = numeroRemplazoNO21
        if datos1[i][21] > 68 and datos1[i][31] == "SI":
                datos1[i][21] = numeroRemplazoSI21
        if datos1[i][31] == "NO"  and np.isnan(datos1[i][21]):
                datos1[i][21] = numeroRemplazoNO21
        if datos1[i][31] == "SI" and  np.isnan(datos1[i][21]):
                datos1[i][21] = numeroRemplazoSI21
        i += 1
    #Imprimir columna de age
    i = 0
    while i < tamFila:
        print(datos1[i][21])
        i += 1
    
    
    
    #TaskStrategies
    print("TaskStrategies")
    #Grafica de cajas y bigotes para TaskStrategies
    data[['TaskStrategies', 'Gano']].boxplot(by='Gano')
    plt.title('Grafica TaskStrategies')
    plt.show()
    
    print(isinstance(datos1[0][4], float))  # Es para saber el tipo de dato
  
    #Sacar Promedio de TaskStrategies
    i = 0
    media4, cont4, suma4 = 0, 0, 0
    while i < tamFila:
        if datos1[i][4] < 3.33 and datos1[i][4] >= 1.33 and datos1[i][31] == "NO":
                suma4 = suma4 + datos1[i][4]
                cont4 += 1
        i += 1
             
    media4 = suma4 / cont4
    print("media ", media4, "  cuenta ", cont4)
    
   #Reemplazar valores atipicos de TaskStrategies
    numeroRemplazo4 = media4
    i = 0
    while i < tamFila:
        if datos1[i][4] >= 3.33 and datos1[i][4] < 1.33 and datos1[i][31] == "NO" :
                datos1[i][4] = numeroRemplazo4
        i += 1
    
    #Imprimir columna de TaskStrategies
    i = 0
    while i < tamFila:
        print(datos1[i][4])
        i += 1
        
    
    
    #ISFEMALE
    print("ISFEMALE")
    #Grafica de cajas y bigotes para isfemale
    data[['isfemale', 'Gano']].boxplot(by='Gano')
    plt.title('Grafica isfemale')
    plt.show()
    
    print(isinstance(datos1[0][9], int))  # Es para saber el tipo de dato
  
    #Sacar Promedio de isfemale
    moda = 0
    moda2 = ""
    i, j, cont, mayor = 0, 0, 0, 0
    while i < tamFila:
        cont = 0
        while j <tamFila:
            if datos1[i][22] == datos1[j][22]:
                cont = cont + 1 
            j += 1
        if cont > mayor:
            mayor = cont
            moda2 = datos1[i][22]
        i += 1
    
    
    print("Moda:  ", moda2, "  Cuenta: ", mayor)
    
    #Reemplazar valores atipicos de isfemale
    numeroRemplazo22 = moda2
    i = 0
    while i < tamFila:
        if datos1[i][22] == 1 and datos1[i][31] == "SI" :
                datos1[i][22] = numeroRemplazo22
        i += 1
    
    #Imprimir columna de isfemale
    i = 0
    while i < tamFila:
        print(datos1[i][22])
        i += 1
        
        
    
    #INT_TOPIC
    print("int_topic")
    #Grafica de cajas y bigotes para int_topic
    data[['int_topic', 'Gano']].boxplot(by='Gano')
    plt.title('Grafica int_topic')
    plt.show()
    
    print(isinstance(datos1[0][18], int))  # Es para saber el tipo de dato
  
    #Sacar Promedio de int_topic
    moda = 0
    moda18 = ""
    i, j, cont, mayor = 0, 0, 0, 0
    while i < tamFila:
        cont = 0
        while j <tamFila:
            if datos1[i][18] == datos1[j][18]:
                cont = cont + 1 
            j += 1
        if cont > mayor:
            mayor = cont
            moda2 = datos1[i][18]
        i += 1
    
    
    print("Moda:  ", moda, "  Cuenta: ", mayor)
    
    #Reemplazar valores atipicos de int_topic
    numeroRemplazo18 = moda
    i = 0
    while i < tamFila:
        if datos1[i][18] == 0 and datos1[i][31] == "SI" :
                datos1[i][18] = numeroRemplazo18
        if datos1[i][18] == 0 and datos1[i][31] == "NO" :
                datos1[i][18] = numeroRemplazo18
        i += 1
    
    #Imprimir columna de int_topic
    i = 0
    while i < tamFila:
        print(datos1[i][18])
        i += 1
    
    
    #INT_ASSESS
    print("int_assess")
    #Grafica de cajas y bigotes para isfemale
    data[['int_assess', 'Gano']].boxplot(by='Gano')
    plt.title('Grafica int_assess')
    plt.show()
    
    print(isinstance(datos1[0][19], int))  # Es para saber el tipo de dato
  
    #Sacar Promedio de int_assess
    moda = 0
    moda18 = ""
    i, j, cont, mayor = 0, 0, 0, 0
    while i < tamFila:
        cont = 0
        while j <tamFila:
            if datos1[i][19] == datos1[j][19]:
                cont = cont + 1 
            j += 1
        if cont > mayor:
            mayor = cont
            moda2 = datos1[i][19]
        i += 1
    
    
    print("Moda:  ", moda, "  Cuenta: ", mayor)
    
    #Reemplazar valores atipicos de int_assess
    numeroRemplazo19 = moda
    i = 0
    while i < tamFila:
        if datos1[i][19] == 0 and datos1[i][31] == "SI" :
                datos1[i][19] = numeroRemplazo19
        if datos1[i][19] == 0 and datos1[i][31] == "NO" :
                datos1[i][19] = numeroRemplazo19
        i += 1
    
    #Imprimir columna de int_assess
    i = 0
    while i < tamFila:
        print(datos1[i][19])
        i += 1
    
    
    #COMPLETER
    print("COMPLETER")
    #Contando la lista para SI y luego para NO
    i, contSI, contNO = 0, 0, 0
    while i < tamFila:
        if datos1[i][31] == "SI":
            contSI += 1
        if datos1[i][31] == "NO":
            contNO += 1
        i += 1
     
     
    listaSI = np.empty((contSI))
    listaNO = np.empty((contNO))
    print("aqui llego")
    
    #Reemplazamos los datos vacios o que no correspodan a VERDADERO o FALSO
    # por un valor alto, en este caso 10, ahora para VERDADERO lo colocamos 1
    #Para el valor FALSO lo colocamos 0
    k, j = 0, 0
    for i in range(tamFila):
        if datos1[i][25] == "VERDADERO" and datos1[i][31] == "NO":
            listaNO[j] = 1
            j += 1
        if datos1[i][25] == "FALSO" and datos1[i][31] == "NO":
            listaNO[j] = 0
            j += 1
        if (datos1[i][25] != "VERDADERO" and datos1[i][25] != "FALSO") and datos1[i][31] == "NO":
            listaNO[j] = 4
            j += 1    
        if datos1[i][25] == "VERDADERO" and datos1[i][31] == "SI":
            listaSI[k] = 1
            k += 1
        if datos1[i][25] == "FALSO" and datos1[i][31] == "SI":
            listaSI[k] = 0
            k += 1
        if (datos1[i][25] != "VERDADERO" and datos1[i][25] != "FALSO") and datos1[i][31] == "SI":
            listaSI[k] = 4
            k += 1
 
    #grafica los datos de completer por medio de dos listas, una del SI y la otra del NO
    # donde graficamos en cajas y bigotes pero con los datos sin limpiar
    datos_graf = [listaSI, listaNO]
    plt.boxplot(datos_graf, labels=["SI", "NO"])
    plt.show()

    #Sacar moda de completer
    moda = 0
    moda25 = ""
    i, j, cont, mayor = 0, 0, 0, 0
    while i < tamFila:
        cont = 0
        while j < tamFila:
            if datos1[i][25] == datos1[j][25]:
                cont = cont + 1 
            j += 1
        if cont > mayor:
            mayor = cont
            moda25 = datos1[i][25]
        i += 1
    
    
    print("Moda:  ", moda25, "  Cuenta: ", mayor)
    
    #Reemplazar valores atipicos de completer
    numeroRemplazo25 = moda25
    i = 0
    while i < tamFila:
        if datos1[i][25] == "VERDAD" and datos1[i][31] == "SI" :
                datos1[i][25] = numeroRemplazo25
        if (datos1[i][25] != "VERDADERO" and datos1[i][25] != "FALSO" and datos1[i][25] != "VERDAD") and datos1[i][31] == "SI" :
                datos1[i][25] = numeroRemplazo25
        i += 1
    
    #Imprimir columna de completer
    i = 0
    while i < tamFila:
        print(datos1[i][25])
        i += 1
    
    #Armo dos listas para prepar la istas de los datos limpios
    listaSILimpia = np.empty((contSI))
    listaNOLimpia = np.empty((contNO))
    
    #volvemos asignar datos de 1 a los datosVERDADERO y 0 para los datos  FALSO
    # esta dos listas estan con los datos ya limpios
    k, j = 0, 0
    for i in range(tamFila):
        if datos1[i][25] == "VERDADERO" and datos1[i][31] == "NO":
            listaNOLimpia[j] = 1
            j += 1
        if datos1[i][25] == "FALSO" and datos1[i][31] == "NO":
            listaNOLimpia[j] = 0
            j += 1    
        if datos1[i][25] == "VERDADERO" and datos1[i][31] == "SI":
            listaSILimpia[k] = 1
            k += 1
        if datos1[i][25] == "FALSO" and datos1[i][31] == "SI":
            listaSILimpia[k] = 0
            k += 1
    
    #grafica los datos de completer por medio de dos listas, una del SI y la otra del NO
    # donde graficamos en cajas y bigotes pero con los datos ya limpios
    datos_graf = [listaSILimpia, listaNOLimpia]
    plt.boxplot(datos_graf, labels=["SI", "NO"])
    plt.show()
    
if __name__ == '__main__':
    main()
    
    
