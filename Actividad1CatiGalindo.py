from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.formats import style

class Error(Exception):
    pass

class MesVacio(Error):
    pass

class FicheroVacio(Error):
    pass

class Errornumcolumnas(Error):
    pass

def pasar_dic_array(dic):
    data = list(dic.values())
    return (np.array(data)) 
    
def mes_mas_gastado(gastos):
    maxgasto = 0
    Mesgastadomas = ''
    gastosnp = pasar_dic_array(gastos)
    for mesg, gasto in gastos.items():     
        if (maxgasto > gasto):
            Mesgastadomas = mesg 
            maxgasto = gasto
    return (Mesgastadomas, np.amin(gastosnp))

def mes_mas_ahorrado(ingresos):
    maxingreso = 0    
    Mesahorradomas = ''
    ingresosnp = pasar_dic_array(ingresos)
    for mes, ingreso in ingresos.items():  
        if (maxingreso < ingreso):
            maxingreso = ingreso
            Mesahorradomas = mes 
    return (Mesahorradomas, np.amax(ingresosnp))  

def media_gastos_anual(gastos):
    gastosnp = pasar_dic_array(gastos)
    return np.mean(gastosnp)    
    
def total_gastos_anual(gastos):
    return sum(gastos.values())

def total_ingresos_anual(ingresos):
    return sum(ingresos.values())    
 
def pintar_grafica(meses, datosingresos):
    plt.bar(meses,datosingresos, color={'b','g','r','m','c','y','orange','purple','brown','blue','pink'})  
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.xlabel("Meses del año")  
    plt.ylabel("Ingresos")  
    plt.title("Evolución de ingresos de todo el año")
    plt.show()
    plt.savefig('vertical_barras.png')
    
def leer_csv(fichero):
    try:
        df = pd.read_csv(fichero, skipinitialspace=True, sep='\t', decimal=',', index_col=False)
        return df
    except IOError:
        print ("No encuentro el fichero o no puedo leerlo")
        return np.empty
         
def operar_csv(fichero):  
    try:
        ingresos = {}
        gastos = {}
        df = leer_csv(fichero)
        if (df.empty):
            raise(FicheroVacio, "El fichero está vacío")
        if (len(df.columns) != 12):
            raise(Errornumcolumnas,"Número de columnas diferentes a 12")     
                        
    except ValueError:
        print ("El valor tiene que ser numerico")

    except TypeError:
        print ("Tipo incorrecto de dato")

   
    for x in df.columns: 
            if (df[x].empty):
                raise(MesVacio, "Datos del mes vacío")
             
            df[x] = pd.to_numeric(df[x], errors='coerce', downcast='signed') # df = df.replace(np.nan, 0, regex=True) 
            df[x] = np.nan_to_num(df[x])
            sumaIngresos = sum(np.clip(df[x], a_min = 0, a_max = None))
            ingresos.update({x:sumaIngresos})
            sumaGastos = sum(np.clip(df[x],  a_min = None, a_max = 0))
            gastos.update({x:sumaGastos})
    print("Valor del dataframe de entrada ----------------")
    print(df)
    mes, maxmesgasto =  mes_mas_gastado(gastos)
    print(f'El mes que se ha gastado más {mes} {maxmesgasto}')
    mesahorro, maxmes = mes_mas_ahorrado(ingresos)
    print(f'El mes que se ha ahorrado más {mesahorro} {maxmes}')   
    print(f'La media de gastos anual  es  {media_gastos_anual(gastos)}')
    print(f'El gasto total anual es {total_gastos_anual(gastos)}')  
    print(f'Los ingresos totales a lo largo del año son {total_ingresos_anual(ingresos)}')
    
    #Pintamos la grafica con los datos del dataframe
    dataingresos = list(ingresos.values())
    pintar_grafica(df.columns,dataingresos)

operar_csv('finanzas2020.csv')    

