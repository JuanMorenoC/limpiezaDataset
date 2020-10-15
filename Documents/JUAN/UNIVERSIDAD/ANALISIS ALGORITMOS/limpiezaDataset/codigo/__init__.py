import csv
import pandas as pd
# Import libraries 
import pandas as pd 
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt 
import seaborn as sns
from builtins import len
from collections import Counter

import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from pandas.core.algorithms import mode


def main():
    dataF = pd.read_csv('Dataset_finalSonia.csv')
    dataF.head()
    datos1 = np.array(dataF)
    tamFila = datos1.shape[0]
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
    
    #Reemplazamos los atos vacios o que no correspodan a VERDADERO o FALSO
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
             
         
         
         
         
         
     
    #datosSI = pd.DataFrame(listaSI)
    #datosNO = pd.DataFrame(listaNO)
     
    datos_graf = [listaSI, listaNO]
    plt.boxplot(datos_graf, labels=["SI", "NO"])
    plt.show()
    
#     n = len(listaSI) + len(listaNO)
#     listaCompleterAtipicos = np.empty(n)
#     i, k, j = 0, 0, 0
#     while i < n:
#         if datos1[i][31] == "SI":
#             listaCompleterAtipicos[i] = listaSI[k]
#             k += 1
#         if datos1[i][31] == "NO":
#             listaCompleterAtipicos[i] = listaNO[j]
#             j += 1
#         
#         i += 1
        
         
    
    
    #Sacar Promedio de int_assess
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
    
    #Reemplazar valores atipicos de int_assess
    numeroRemplazo25 = moda25
    i = 0
    while i < tamFila:
        if datos1[i][25] == "VERDAD" and datos1[i][31] == "SI" :
                datos1[i][25] = numeroRemplazo25
        if (datos1[i][25] != "VERDADERO" and datos1[i][25] != "FALSO" and datos1[i][25] != "VERDAD") and datos1[i][31] == "SI" :
                datos1[i][25] = numeroRemplazo25
        i += 1
    
    #Imprimir columna de int_assess
    i = 0
    while i < tamFila:
        print(datos1[i][25])
        i += 1
    
    listaSILimpia = np.empty((contSI))
    listaNOLimpia = np.empty((contNO))
    
    #Reemplazamos los atos vacios o que no correspodan a VERDADERO o FALSO
    # por un valor alto, en este caso 10, ahora para VERDADERO lo colocamos 1
    #Para el valor FALSO lo colocamos 0
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
    
    datos_graf = [listaSILimpia, listaNOLimpia]
    plt.boxplot(datos_graf, labels=["SI", "NO"])
    plt.show()
    
    print("SALIO")
    
#     print("completer")
#     datosL[['completer', 'Gano']].boxplot(by='Gano')
#     plt.title('Grafica completer')
#     plt.show()
    # print(data)
    
    # print(data.describe())
    
    # print(data.isnull().sum())
    # filavacia = data.isnull()['age']
    # filasvacias = data[filavacia]
    # print(filasvacias)
    
    # hist = data['age'].hist()
    # datos1 = pd.DataFrame(data)
    
    # dato = pd.DataFrame(data[1], columns=['GoalSetting'])
    # dato.plot.box(grid='True')
    
    # data.boxplot(by ='Gano', column =['Atry to lecture'], grid = False) 
    
    # valor = data[['Gano','Atry to lecture']]  
    
    # ax = valor.plot.bar(x='Gano', y='Atry to lecture', rot=0)
    # plt.show()
    # print(valor)
    
    # parametros esteticos de seaborn
    # sns.set_palette("deep", desat=.6)
    # sns.set_context(rc={"figure.figsize": (8, 4)})
    # sns.boxplot(list(data['Atry to lecture']))
    # plt.title('importe')
    # plt.show()
    
    # tamCol = datos1.shape[1]
    
    # ESTE SI ES LA GRAFICA
    
    # data[['Atry to lecture', 'Gano']].boxplot(by='Gano')
    # plt.title('Grafica 1')
    # plt.show()
    
#     sns.boxplot(datos_graf, names=["grupo1", "grupo2", "grupo3", "grupo 4"],
#             color="PaleGreen");
    
#     print(data.shape[1])
#     
#     print("termino")
#     datos1 = np.array(data)
#     tamFila = datos1.shape[0]
#    
#     
#     moda = 0
#     moda2 = ""
#     i, j, cont, mayor = 0, 0, 0, 0
#     while i < tamFila:
#         cont = 0
#         while j <tamFila:
#             if datos1[i][31] == datos1[j][31]:
#                 cont = cont + 1 
#             j += 1
#         if cont > mayor:
#             mayor = cont
#             moda2 = datos1[i][31]
#         i += 1
#     
#     
#     print("Moda:  ", moda2, "  Cuenta: ", mayor)
    
    # ISFEMALE
    
    # Grafica de cajas y bigotes para isfemale
    
    
#     ray1=[0.217766,0.691315,0.289239,0.239135,0.161341,0.364297,0.373284,0.323216]
#     df = pd.DataFrame(ray1, dtype = float)
#     
#     data.boxplot()
#     plt.plot(np.arange(len(data)),data[25])
#     plt.show()

#     sns.boxplot(x="Gano",y="completer",data=dataF,linewidth=1,fliersize=2 )
#     
#     plt.figure(figsize=(20,10))
#     ax = sns.boxplot(x="Gano",y="completer",data=dataF,linewidth=1,fliersize=2)
#     _ = ax.set_xticklabels(ax.get_xticklabels(), rotation=-80)
#     plt.show()
#     datos_graf = [listaSI, listaNO]
 
#     plt.boxplot(datos_graf)
#     plt.show()
    

if __name__ == '__main__':
    main()
