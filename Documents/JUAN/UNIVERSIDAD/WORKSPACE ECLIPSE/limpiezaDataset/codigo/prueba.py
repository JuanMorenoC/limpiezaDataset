'''
Created on 8 oct. 2020

@author: JUAN MORENO
@author: TATIANA MORA
@author: JORGE GIRALDO
@author: LORENZO FLEREZ
@author: DAVID OROZCO
@author: SEBASTIAN ANTTURY
@author: JUAN GARCIA
@author: DIEGO GUTIERREZ
@author: BRYAN HENAO
'''

# Importar librerias 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import colors
import seaborn as sns
from builtins import len

from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
#from sklearn.externals.six import StringIO  
#from IPython.display import Image  
import pydotplus
from sklearn import tree
from sklearn.tree import export_graphviz
import graphviz

from sklearn import preprocessing 
from sklearn.cluster import KMeans

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest


import csv

# Metodo main el menu principal, llamados de todos los metodos, lectura de los archivos 
# llamado de los metodos para graficar y de las impiezas
def main():
    data = pd.read_csv('Dataset_finalSonia.csv')
    datos1 = np.array(data) 
    tamFila = datos1.shape[0] 
    
    # LIMPIEZA DE CADA DATO CON GRAFICA INCLUIDA
    #Realiza la limpieza de cada dato, grafica la cajas y bigotes ates de la limpieza
    # y luego despues de la limpieza vuelve a graficar.
    #A cada metodo se le envia data para alguna grafica,  datos1 que es 
    # con el que se va hacer la limpieza y en algunas graficas se va a tratar
    # y tamFila porque es para poder recorrelo 
    
    # ATRY TO LECTURE
    print("ATRY TO LECTURE")
    limpiezaAtrytoLecture(data, datos1, tamFila)
    
    # ONLY LECTURE
    print("ONLY LECTURE")
    limpiezaOnlyLecture(data, datos1, tamFila)
    
    # EXPLORE
    print("EXPLORE")
    limpiezaExplore(data, datos1, tamFila)
    
    # AGE
    print("AGE")
    limpiezaAge(data, datos1, tamFila)
    
    # TaskStrategies
    print("TaskStrategies")
    limpiezaTaskStrategies(data, datos1, tamFila)
    
    # ISFEMALE
    print("ISFEMALE")
    limpiezaIsFemale(data, datos1, tamFila)
    
    # INT_TOPIC
    print("int_topic")
    limpiezaInt_Topic(data, datos1, tamFila)
    
    # INT_ASSESS
    print("int_assess")
    limpiezaInt_Assess(data, datos1, tamFila)
    
    # COMPLETER
    print("COMPLETER")
    limpiezaCompleter(data, datos1, tamFila)
    
    #OTRAS GRAFICAS DE OTROS DATOS
    print("OTRAS GRAFICAS")
    graficaDispersionSRLvsDAY_ACT(datos1)
    graficaBarraVertical(data, "Gano", "num_events")
    graficaBarraHorizontal(data, "Gano", "days_act")
    graficaScatter(data, "Lcomplete to Atry", "explore" )
    graficaScatter(data, "StrategicPlanning", "TaskStrategies" )

    
    #Metodo para crear el archivo CSV despues de ya limpia el dataset
    crearDataLimpiaCSV(datos1)
    
    #Llamado del dataset para graficar el arbol, mandamos como parametro
    #un data set pero ya limpio y con los datos ya listos para raficar 
    arboles()
    
    # LLamado de los metodos para Clustering
    graficaCluster(data)
    graficaScatter(data, "Lcomplete to Atry", "explore" )
    
    # LLamado del metodo para Bayes
    bayes()

    print("FIN DE LA OPERACION")

#METODOS DE LIMPIEZAS DE LOS DATOS DIVIDIDOS CADA UNO

#Metodo Aty to lecture 
def limpiezaAtrytoLecture(data, datos1, tamFila):
    # Grafica de cajas y bigotes para Atry To Lecture
    graficaCajasYBigotesUno(data, "Atry to lecture")
    
    print(isinstance(datos1[0][9], int))  # Es para saber el tipo de dato
  
    # Sacar Promedio de Atry to Lecture
    i = 0
    media9, cont9, suma9 = 0, 0, 0
    while i < tamFila:
        if datos1[i][9] <= 5 and datos1[i][9] >= 0 :
                suma9 = suma9 + datos1[i][9]
                cont9 += 1
        i += 1
             
    media9 = suma9 / cont9
    print("media ", media9, "  cuenta ", cont9)
    
    # Reemplazar valores atipicos de Atry to Lecture
    numeroRemplazo9 = round(media9)
    i = 0
    while i < tamFila:
        if datos1[i][9] > 5 :
                datos1[i][9] = numeroRemplazo9
        i += 1
    
    # Imprimir columna de Atry to Lecture
    i = 0
    while i < tamFila:
        print(datos1[i][9])
        i += 1
    
    # Diagrama de cajas y bigotes de atry to lecture    
    listaSILimpia = np.empty((274))
    listaNOLimpia = np.empty((220))
    
    # Reemplazamos los atos uno del si y otro del no
    k, j = 0, 0
    for i in range(tamFila):
        if datos1[i][31] == "NO":
            listaNOLimpia[j] = datos1[i][9]
            j += 1
        if datos1[i][31] == "SI":
            listaSILimpia[k] = datos1[i][9]
            k += 1
    
    # GRAFICA CON DATOS LIMPIOS CAJAS Y BIGOTES
    datos_graf = [listaSILimpia, listaNOLimpia]
    c = "red"
    plt.boxplot(datos_graf, labels=["SI", "NO"],
            capprops=dict(color=c),
            whiskerprops=dict(color=c),
            flierprops=dict(color=c, markeredgecolor=c),
            medianprops=dict(color=c))
    plt.title('Grafica Atry to lecture')
    plt.ylabel('Atry To Lecture')
    plt.xlabel('Gano')
    plt.show()
    
    # GRafica de frecuencia histograma para Atry to lecture ya con datos limpios
    graficaHistograma(datos_graf, "Atry to lecture")

#Metodo only lecture  
def limpiezaOnlyLecture(data, datos1, tamFila):
    # Grafica de cajas y bigotes para only lecture
    graficaCajasYBigotesUno(data, "only lecture")
    
    print(isinstance(datos1[0][8], int))  # Es para saber el tipo de dato
  
    # Sacar Promedio de only lecture
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
    
    # Reemplazar valores atipicos de only lecture
    numeroRemplazoNO8 = round(mediaNO8)
    numeroRemplazoSI8 = round(mediaSI8)
    i = 0
    while i < tamFila:
        if datos1[i][8] > 5 and datos1[i][31] == "NO":
                datos1[i][8] = numeroRemplazoNO8
        if datos1[i][8] > 50 and datos1[i][31] == "SI":
                datos1[i][8] = numeroRemplazoSI8
        i += 1
    
    # Imprimir columna de only lecture
    i = 0
    while i < tamFila:
        print(datos1[i][8])
        i += 1
    
   # Diagrama de cajas y bigotes de Only Lecture    
    listaSILimpiaO = np.empty((274))
    listaNOLimpiaO = np.empty((220))
    
    # Reemplazamos los datos uno del si y otro del no
    k, j = 0, 0
    for i in range(tamFila):
        if datos1[i][31] == "NO":
            listaNOLimpiaO[j] = datos1[i][8]
            j += 1
        if datos1[i][31] == "SI":
            listaSILimpiaO[k] = datos1[i][8]
            k += 1
    c = "blue"
    # GRAFICA CON DATOS LIMPIOS CAJAS Y BIGOTES
    datos_graf = [listaSILimpiaO, listaNOLimpiaO]
    plt.boxplot(datos_graf, labels=["SI", "NO"],
            capprops=dict(color=c),
            whiskerprops=dict(color=c),
            flierprops=dict(color=c, markeredgecolor=c),
            medianprops=dict(color=c))
    plt.title('Grafica Only Lecture')
    plt.ylabel('Only Lecture')
    plt.xlabel('Gano')
    plt.show()
    
    # GRafica de frecuencia histograma para only lecture ya con datos limpios
    graficaHistograma(datos_graf, "only lecture")

#Metodo explore
def limpiezaExplore(data, datos1, tamFila):
    # Grafica de cajas y bigotes para explore
    graficaCajasYBigotesUno(data, "explore")
    
    print(isinstance(datos1[0][10], int))  # Es para saber el tipo de dato
  
    # Sacar Promedio de explore
    i = 0
    mediaSI10, contSI10, sumaSI10 = 0, 0, 0
    while i < tamFila:
        if datos1[i][10] <= 39 and datos1[i][10] >= 0 and datos1[i][31] == "SI":
                sumaSI10 = sumaSI10 + datos1[i][10]
                contSI10 += 1
        i += 1
             
    mediaSI10 = sumaSI10 / contSI10
    print("SI->   media ", mediaSI10, "  cuenta ", contSI10)
    
    # Reemplazar valores atipicos de explore
    numeroRemplazoSI10 = round(mediaSI10)
    i = 0
    while i < tamFila:
        if datos1[i][10] > 35 and datos1[i][31] == "SI":
                datos1[i][10] = numeroRemplazoSI10
        i += 1
    
    # Imprimir columna de explore
    i = 0
    while i < tamFila:
        print(datos1[i][10])
        i += 1
    
    # Diagrama de cajas y bigotes de explore    
    listaSILimpiaE = np.empty((274))
    listaNOLimpiaE = np.empty((220))
    
    # Reemplazamos los datos uno del si y otro del no
    k, j = 0, 0
    for i in range(tamFila):
        if datos1[i][31] == "NO":
            listaNOLimpiaE[j] = datos1[i][10]
            j += 1
        if datos1[i][31] == "SI":
            listaSILimpiaE[k] = datos1[i][10]
            k += 1
    c = "purple"
    
    # GRAFICA CON DATOS LIMPIOS CAJAS Y BIGOTES
    datos_graf = [listaSILimpiaE, listaNOLimpiaE]
    plt.boxplot(datos_graf, labels=["SI", "NO"],
            capprops=dict(color=c),
            whiskerprops=dict(color=c),
            flierprops=dict(color=c, markeredgecolor=c),
            medianprops=dict(color=c))
    plt.title('Grafica Explore')
    plt.ylabel('Explore')
    plt.xlabel('Gano')
    plt.show()
    
    # GRafica de frecuencia histograma para explore ya con datos limpios
    graficaHistograma(datos_graf, "explore")

def limpiezaAge(data, datos1, tamFila):
    # Grafica de cajas y bigotes para age
    graficaCajasYBigotesUno(data, "age")
    
    print(isinstance(datos1[0][21], int))  # Es para saber el tipo de dato
  
    # Sacar Promedio de age
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
    
    # Reemplazar valores atipicos de age
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
    # Imprimir columna de age
    i = 0
    while i < tamFila:
        print(datos1[i][21])
        i += 1
    
    # Armar la lista de AGE
    listaSILimpia = np.empty((274))
    listaNOLimpia = np.empty((220))
    
    # asignamos o preparamos las lista para poder graficar lo dividimos entre 
    # 2 lisas, uno la list Si y otra lista NO, ambas ya limpias
    
    k, j = 0, 0
    for i in range(tamFila):
        if datos1[i][31] == "NO":
            listaNOLimpia[j] = datos1[i][21]
            j += 1
        if datos1[i][31] == "SI":
            listaSILimpia[k] = datos1[i][21]
            k += 1
    
    # grafica los datos de AGE por medio de dos listas, una del SI y la otra del NO
    # donde graficamos en cajas y bigotes pero con los datos ya limpios
    datos_graf = [listaSILimpia, listaNOLimpia]
    graficaCajasYBigotesDos(datos_graf, "age")
    
    # GRafica de frecuencia histograma para AGE ya con datos limpios
    graficaHistograma(datos_graf, "age")

def limpiezaTaskStrategies(data, datos1, tamFila):
    # Grafica de cajas y bigotes para TaskStrategies
    graficaCajasYBigotesUno(data, "TaskStrategies")
    
    print(isinstance(datos1[0][4], float))  # Es para saber el tipo de dato
  
    # Sacar Promedio de TaskStrategies
    i = 0
    media4, cont4, suma4 = 0, 0, 0
    while i < tamFila:
        if datos1[i][4] < 3.33 and datos1[i][4] >= 1.33 and datos1[i][31] == "NO":
                suma4 = suma4 + datos1[i][4]
                cont4 += 1
        i += 1
             
    media4 = suma4 / cont4
    print("media ", media4, "  cuenta ", cont4)
    
   # Reemplazar valores atipicos de TaskStrategies
    numeroRemplazo4 = media4
    i = 0
    while i < tamFila:
        if datos1[i][4] >= 3.33 and datos1[i][4] < 1.33 and datos1[i][31] == "NO" :
                datos1[i][4] = numeroRemplazo4
        i += 1
    
    # Imprimir columna de TaskStrategies
    i = 0
    while i < tamFila:
        print(datos1[i][4])
        i += 1

def limpiezaIsFemale(data, datos1, tamFila):
    # Grafica de cajas y bigotes para isfemale
    graficaCajasYBigotesUno(data, "isfemale")
    
    print(isinstance(datos1[0][9], int))  # Es para saber el tipo de dato
  
    # Sacar moda de isfemale
    moda = 0
    moda2 = ""
    i, j, cont, mayor = 0, 0, 0, 0
    while i < tamFila:
        cont = 0
        while j < tamFila:
            if datos1[i][22] == datos1[j][22]:
                cont = cont + 1 
            j += 1
        if cont > mayor:
            mayor = cont
            moda2 = datos1[i][22]
        i += 1
    
    print("Moda:  ", moda2, "  Cuenta: ", mayor)
    
    # Reemplazar valores atipicos de isfemale
    numeroRemplazo22 = moda2
    i = 0
    while i < tamFila:
        if datos1[i][22] == 1 and datos1[i][31] == "SI" :
                datos1[i][22] = numeroRemplazo22
        i += 1
    
    # Imprimir columna de isfemale
    i = 0
    while i < tamFila:
        print(datos1[i][22])
        i += 1
    
    graficaBarras1(datos1)

def limpiezaInt_Topic(data, datos1, tamFila):
    # Grafica de cajas y bigotes para int_topic
    graficaCajasYBigotesUno(data, "int_topic")
    
    print(isinstance(datos1[0][18], int))  # Es para saber el tipo de dato
  
    # Sacar moda de int_topic
    moda = 0
    moda18 = ""
    i, j, cont, mayor = 0, 0, 0, 0
    while i < tamFila:
        cont = 0
        while j < tamFila:
            if datos1[i][18] == datos1[j][18]:
                cont = cont + 1 
            j += 1
        if cont > mayor:
            mayor = cont
            moda2 = datos1[i][18]
        i += 1
    
    print("Moda:  ", moda, "  Cuenta: ", mayor)
    
    # Reemplazar valores atipicos de int_topic
    numeroRemplazo18 = moda
    i = 0
    while i < tamFila:
        if datos1[i][18] == 0 and datos1[i][31] == "SI" :
                datos1[i][18] = numeroRemplazo18
        if datos1[i][18] == 0 and datos1[i][31] == "NO" :
                datos1[i][18] = numeroRemplazo18
        i += 1
    
    # Imprimir columna de int_topic
    i = 0
    while i < tamFila:
        print(datos1[i][18])
        i += 1

def limpiezaInt_Assess(data, datos1, tamFila):
    # Grafica de cajas y bigotes para isfemale
    graficaCajasYBigotesUno(data, "int_assess")
    
    print(isinstance(datos1[0][19], int))  # Es para saber el tipo de dato
  
    # Sacar moda de int_assess
    moda = 0
    moda18 = ""
    i, j, cont, mayor = 0, 0, 0, 0
    while i < tamFila:
        cont = 0
        while j < tamFila:
            if datos1[i][19] == datos1[j][19]:
                cont = cont + 1 
            j += 1
        if cont > mayor:
            mayor = cont
            moda2 = datos1[i][19]
        i += 1
    
    print("Moda:  ", moda, "  Cuenta: ", mayor)
    
    # Reemplazar valores atipicos de int_assess
    numeroRemplazo19 = moda
    i = 0
    while i < tamFila:
        if datos1[i][19] == 0 and datos1[i][31] == "SI" :
                datos1[i][19] = numeroRemplazo19
        if datos1[i][19] == 0 and datos1[i][31] == "NO" :
                datos1[i][19] = numeroRemplazo19
        i += 1
    
    # Imprimir columna de int_assess
    i = 0
    while i < tamFila:
        print(datos1[i][19])
        i += 1
    

def limpiezaCompleter(data, datos1, tamFila):
    # Contando la lista para SI y luego para NO
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
    
    # Reemplazamos los datos vacios o que no correspodan a VERDADERO o FALSO
    # por un valor alto, en este caso 4, ahora para VERDADERO lo colocamos 1
    # Para el valor FALSO lo colocamos 0
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
 
    # grafica los datos de completer por medio de dos listas, una del SI y la otra del NO
    # donde graficamos en cajas y bigotes pero con los datos sin limpiar
    datos_graf = [listaSI, listaNO]
    graficaCajasYBigotesDos(datos_graf, "completer")

    # Sacar moda de completer
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
    
    # Reemplazar valores atipicos de completer
    numeroRemplazo25 = moda25
    i = 0
    while i < tamFila:
        if datos1[i][25] == "VERDAD" and datos1[i][31] == "SI" :
                datos1[i][25] = numeroRemplazo25
        if (datos1[i][25] != "VERDADERO" and datos1[i][25] != "FALSO" and datos1[i][25] != "VERDAD") and datos1[i][31] == "SI" :
                datos1[i][25] = numeroRemplazo25
        i += 1
    
    # Imprimir columna de completer
    i = 0
    while i < tamFila:
        print(datos1[i][25])
        i += 1
    
    # Armo dos listas para prepar la istas de los datos limpios
    listaSILimpia = np.empty((contSI))
    listaNOLimpia = np.empty((contNO))
    
    # volvemos asignar datos de 1 a los datosVERDADERO y 0 para los datos  FALSO
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
    
    # grafica los datos de completer por medio de dos listas, una del SI 
    #y la otra del NO
    # donde graficamos en cajas y bigotes pero con los datos ya limpios
    datos_graf = [listaSILimpia, listaNOLimpia]
    graficaCajasYBigotesDos(datos_graf, "completer")
    
    # GRafica de frecuencia histograma para COMPLETER ya con datos limpios
    graficaHistograma(datos_graf, "completer")

def crearDataLimpiaCSV(datos1):
    #Reemplazamos los datos completer y Gano en numeros 1 y 0 para reprsentarlos
    #ya que en arboles no tiene en cuenta los Strings cuando se van a 
    #convertir en float.
    
    dataLimpia = reemplazoDatosCompleterYGano(datos1)
    
    #Crear un archivo csv ya con los datos limpios de la matriz ataLimpia
    with open('dataLimpia.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(dataLimpia)


def graficaCajasYBigotesUno(data, datoColumna1):
    titulo = 'Grafica {}'.format(datoColumna1)
    data[[datoColumna1, 'Gano']].boxplot(by='Gano')
    plt.title(titulo)
    plt.show()


def graficaCajasYBigotesDos(datos_graf, datoColumna1):
    titulo = 'Grafica {}'.format(datoColumna1)
    plt.boxplot(datos_graf, labels=["SI", "NO"])
    plt.title(titulo)
    plt.show()
    
    
def graficaHistograma(datos_graf, datoColumna):
    titulo = 'Grafica {}'.format(datoColumna)
    plt.hist(datos_graf, bins=2, edgecolor='black')
    plt.title(titulo)
    plt.xlabel(datoColumna)
    plt.ylabel("Frecuencia")
    plt.show()

def graficaBarras1(datos1):
    # grafica de barras para ver la cantidad de female vs otro
    print("isFemale contra age")
    isfemale = [fila[22] for fila in datos1]
    female = list(isfemale).count(1)
    other = list(isfemale).count(0)
    datox = ["femenino", "otro"]
    datoy = [female, other]
    colores = ["blue", "yellow"]
    plt.title("isFemale ")
    plt.bar(datox, height= datoy,color= colores,width= 0.5, align= 'center' )
    plt.show()


def graficaDispersionSRLvsDAY_ACT(datos1):
    
    xDay = [fila[26] for fila in datos1]
    ySrl = [fila[7] for fila in datos1]
    fig, ax = plt.subplots()
    ax.scatter(xDay, ySrl, color="green", s=25, alpha=0.5,linewidths=1) 
    # editar las etiquetas

    ax.set_xlabel('DAY_ACT')
    ax.set_ylabel('SRL')  
    plt.title('SRL vs DAY_ACT')         
    plt.show()

def graficaBarraVertical(data, datoColumna1, datoColumna2):
    titulo = 'Grafica de barras {}'.format(datoColumna1) + ' vs {}'.format(datoColumna2)
    x = data[datoColumna1].values
    y = data[datoColumna2].values
    plt.bar(x, y, data = data, color="purple", align="center")
    plt.title(titulo)
    plt.xlabel(datoColumna1)
    plt.ylabel(datoColumna2)
    plt.show()
    
    
def graficaBarraHorizontal(data, datoColumna1, datoColumna2):
    titulo = 'Grafica de barras {}'.format(datoColumna1) + ' vs {}'.format(datoColumna2)
    x = data[datoColumna1].values
    y = data[datoColumna2].values
    plt.barh(x, y, data = data, color="brown", align="center")
    plt.title(titulo)
    plt.xlabel(datoColumna2)
    plt.ylabel(datoColumna1)
    plt.show() 
    
       
def graficaScatter(data, datoColumna1, datoColumna2):
    titulo = 'Grafica Scatter {}'.format(datoColumna1) + ' vs {}'.format(datoColumna2) 
    plt.scatter(data[[datoColumna1]], data[[datoColumna2]], color='blue', edgecolors='black')
    plt.title(titulo)
    plt.xlabel(datoColumna1)
    plt.ylabel(datoColumna2)
    plt.show()


def clusteringCodo(data):
    
    data = data.dropna()
    data = data.reset_index(drop=True)
    
    data.drop('userId',axis=1, inplace=True)
    data.drop('completer',axis=1, inplace=True)
    data.drop('Gano',axis=1, inplace=True)
    
    
    min_max_scaler = preprocessing.MinMaxScaler() 
    data_escalado = min_max_scaler.fit_transform(data)
    data_escalado = pd.DataFrame(data_escalado) # Hay que convertir a DF el resultado.
    data_escalado = data_escalado.rename(columns = {11: 'only asessment', 8: 'only lecture'})
    
    
    x = data_escalado['only asessment'].values
    y = data_escalado['only lecture'].values
    plt.xlabel('only asessment')
    plt.ylabel('only lecture')
    plt.title('Clustering only asessment vs. only lecture')
    plt.plot(x,y,'o',markersize=1)
    

    nc = range(1, 20)
    kmeans = [KMeans(n_clusters=i) for i in nc]
    kmeans
    score = [kmeans[i].fit(data_escalado).score(data_escalado) for i in range(len(kmeans))]
    score
    plt.xlabel('Numero de clusteres')
    plt.ylabel('Suma de los errores cuadraticos')
    plt.plot(nc,score)
   
    
def graficaCluster(data):
    
    data = data.dropna()
    
    data = data.reset_index(drop=True)
    
    data.drop('userId',axis=1, inplace=True)
    data.drop('completer',axis=1, inplace=True)
    data.drop('Gano',axis=1, inplace=True)
    
    
    min_max_scaler = preprocessing.MinMaxScaler() 
    data_escalado = min_max_scaler.fit_transform(data)
    data_escalado = pd.DataFrame(data_escalado) # Hay que convertir a DF el resultado.
    data_escalado = data_escalado.rename(columns = {11: 'only asessment', 8: 'only lecture'})
    
    kmeans = KMeans(n_clusters=3).fit(data_escalado)
    centroids = kmeans.cluster_centers_
    print(centroids)
    
    labels = kmeans.predict(data_escalado)
    
    colores=['red','green','orange']
    asignar=[]
    for row in labels:
        asignar.append(colores[row])
    
        
    x = data_escalado['only asessment'].values
    y = data_escalado['only lecture'].values
    plt.scatter(x, y, c=asignar, s=40)
    plt.scatter(centroids[:, 1], centroids[:, 2], marker='*', c=colores, s=60, alpha=0.5) # Marco centroides.
    plt.xlabel('only asessment')
    plt.ylabel('only lecture')
    plt.title('k-means clustering')
    plt.show()    

    
#Metod para reemplazar los datos de completer y Gano por 1 y 0,
# para poder graficar el arbol ya que n0 admite Strings cuando se va pasar a Float 
def reemplazoDatosCompleterYGano(datos1):
    
    dataLimpiaAux = np.ones(datos1.shape)
    #datos a reemplazar de completer y gano por los valores 1 y 0 
    # para completer cuando es VERDADERO se reemplaza con 1
    # para completer cuando es FALSO se reemplaza con 0
    # para Gano cuando es SI se reemplaza con 1
    # para Gano cuando es NO se reemplaza con 0
    
    for i in range(datos1.shape[0]):
        for j in range(datos1.shape[1]):
            if datos1[i][25] == "VERDADERO":
                dataLimpiaAux[i][25] = 1
            if datos1[i][25] == "FALSO":
                dataLimpiaAux[i][25] = 0
            if datos1[i][31] == "SI":
                dataLimpiaAux[i][31] = 1
            if datos1[i][31] == "NO":
                dataLimpiaAux[i][31] = 0
            if j != 25 and j!= 31 and j != 0:
                dataLimpiaAux[i][j] = datos1[i][j]
            if j == 0:
                dataLimpiaAux[i][0] = i+1
            
    
    return dataLimpiaAux 

#Metodo para creear el arbol de decisiones, este arbol arma el arbol dependiendo
# de las hojas, el nodo raiz, y de las caracteristicas que se le impone.
def arboles():
    col_names = ['userId', 'GoalSetting', 'StrategicPlanning', 'SelfEvaluation', 
                 'TaskStrategies', 'Elaboration', 'HelpSeeking', 'SRL', 
                 'only_lecture', 'Atry_to_lecture', 'explore', 
                 'only_asessment', 'Lcomplete_to_Atry', 'lecture_to_Acomplete', 
                 'hrs', 'prior_exp', 'crs_str', 
                 'crs_fin', 'int_topic', 'int_assess', 
                 'edu', 'age', 'isfemale', 
                 'emp_student', 'emp_job', 'completer', 
                 'days_act', 'num_events', 'num_ses', 
                 'grade', 'cluster', 'Gano']
    # cargar el dataset
    pima = pd.read_csv("dataLimpiaPrueba.csv", header=None, names=col_names)

    print(pima.head())
    #split dataset in features and target variable
    feature_cols = ['Atry_to_lecture', 'only_lecture', 'explore', 'age','TaskStrategies','isfemale','int_topic','int_assess','completer','Gano']
    X = pima[feature_cols] # caracteristicas
    y = pima.Atry_to_lecture # variable objetivo
    # Dividir el conjunto de datos en conjunto de entrenamiento y de prueba
    # generador de numeros aleatorios (semilla)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1) # 70% training and 30% test
    # crear objeto clasificador para el arbol de decision
    # se pasa max_depth como la profundidad, min_samples_leaf como las hojas
    # se pasa min_features como el minimo de caracteristicas
    # y se pasa el min_samples_split como el minimo de conjuntos de datos divididas
    clf = DecisionTreeClassifier(criterion = "entropy", max_depth = 3, min_samples_split = 3,min_samples_leaf = 3, max_features = 3).fit(X,y)

    # clasificador de arbol de decision
    clf = clf.fit(X_train,y_train)

    # predecir la respuesta para el conjunto de datos de prueba
    y_pred = clf.predict(X_test)


    # precision del modelo
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    # aqui se pasa llos nombres de las caracteristicas y de las columas
    # guarda el arbol en un archivo de PDF
    dot_data = export_graphviz(clf, out_file=None, rounded=True,special_characters=True, filled=True, feature_names = feature_cols)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf('tree2.pdf')

    # se obtiene la importancia de cada atributo
    for name, importance in zip(feature_cols, clf.feature_importances_):
        print(name + ': ' + str(importance))


    y2_pred = clf.predict([[64,11, 7, 31,2.71, 1,1,1,1,1]])

    print("La prediccion "+str(y2_pred))
    print("SALIO ARBOLES")

#Metodo para Bayes
def bayes():
    #se carga el dataset    
    dataset = pd.read_csv("Dataset_Bayes.csv")

    #Se imprime la cantidad de usuarios que ganaron y perdieron
    print(dataset.groupby('Gano').size())

    #Imprime grafica de barras  Gano vs Variables
    dataset.drop(['Gano'], axis=1).hist()
    plt.show()

    #se elimina userId, completer son irrelevantes para aplicar el metodo
    dataset_limpio = dataset.drop(['userId','completer'], axis=1)
    dataset_limpio.describe()

    # se limpia el dataset de valores NaN, Inf
    dataset_limpio = limpiar_dataset_Para_Bayes(dataset_limpio)

    #se elimna y obtiene la variable Gano con el fin de poder buscar las 5 mejores variables que pueden determinar si Gano o perdio 
    a=dataset_limpio.drop(['Gano'], axis=1)
    b=dataset_limpio['Gano']
    best=SelectKBest(k=5)
    a_new = best.fit_transform(a, b)
    a_new.shape
    selected = best.get_support(indices=True)
    print("Mejores 5 variables")
    print(a.columns[selected])

    #Imprime grafica de correlación de pearson con respecto a las 5 mejores variables
    used_features = a.columns[selected]
    colormap = plt.viridis()
    plt.figure(figsize=(12,12))
    plt.title('Coeficiente de correlación de Pearson', y=1.05, size=15)
    sns.heatmap(dataset_limpio[used_features].astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
    plt.show()

    #se dividen los datos de entrada en 'entrenamiento' y 'pruebas'
    a_entrenamiento, a_pruebas = train_test_split(dataset_limpio, test_size=0.2, random_state=6) 
    b_entrenamiento =a_entrenamiento["Gano"]
    b_pruebas = a_pruebas["Gano"]

    gnb = GaussianNB()
    gnb.fit(
        a_entrenamiento[used_features].values,
        b_entrenamiento
    )
    y_pred = gnb.predict(a_pruebas[used_features])
    
    print('Precisión en el set de Entrenamiento: {:.2f}'
        .format(gnb.score(a_entrenamiento[used_features], b_entrenamiento)))
    print('Precisión en el set de Pruebas: {:.2f}'
        .format(gnb.score(a_pruebas[used_features], b_pruebas)))

    #cinco mejores variables
    #'SRL', 'Atry to lecture', 'num_events', 'grade', 'cluster'
    #tomamos datos del dataset donde un usuario perdio y gano (0,1) con relacion a las 5 mejores variables
    print(gnb.predict( [[1.666666667,0,2,5.999999866,0],[2.041666667,150,151,62.00000048,1]]))

def limpiar_dataset_Para_Bayes(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

    
if __name__ == '__main__':
    main()
    
