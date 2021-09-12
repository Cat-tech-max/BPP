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
    
class operacionesEstadisticasCsv:
    """
    Operaciones estadisticas. Esta clase resuelve una serie de operaciones estadisticas sobre datos leidos en un csv de tipo entero.
    Atributos:
    csv:
        este es el fichero csv que se va a utilizar en los metodos de operaciones estadísticas
        En el caso de que el fichero tenga errores se comprueban los datos
  
    Metodos:
    
    pasar_dic_array:
        Convierte un diccionario con el parametro dic en array
        
    mes_mas_gastado:
        Calcula del diccionario gastos pasado por parametro, el mes que mas se ha gastado, retornando el mes y la cantidad

    mes_mas_ahorrado:
        Calcula del diccionario ingresos pasado por parametro, el mes que mas se ha ingresado, retornando el mes y la cantidad 

    media_gastos_anual:
        Calcula del diccionario gastos pasado por parametro, el valor de la media de gastos anual
     
    total_gastos_anual:
        Calcula del diccionario gastos pasado por parametro, el valor de la suma de gastos anual

    total_ingresos_anual:
        Calcula del diccionario ingresos pasado por parametro, el total de ingresos anual
    
    pintar_grafica:
        Pinta la grafica por barras dados unos parametros meses y datosingresos
        
    leer_csv:
        Lee el fichero csv pasado por el parametro fichero y lo convierte en un dataframe
        Si no encuentra el fichero nos muestra un mensaje de error y devuelve un valor vacio
    
    Ejemplos:
    >>> from utils import Actividad3CatiGalindo as ac
    >>> ac.operar_csv('finanzas2020.csv')    
    """
    def __init__(self, csv):
        self.csv = csv
        self.operar_csv(csv)
            
    def pasar_dic_array(self, dic):
        """
        Método pasar_dic_array.  Convierte un diccionario con el parametro dic
        Inputs:
            dic: tipo diccionario
        Outputs:
            array convertido  
        """
        data = list(dic.values())
        return (np.array(data)) 
        
    def mes_mas_gastado(self, gastos):
        """
        Método mes_mas_gastado. Calcula de un diccionario el mes y la cantidad que mas se ha gastado
        Inputs:
           gastos: tipo diccionario
        Outputs:
           mes
           valor de este mes mas gastado
        """
        maxgasto = 0
        Mesgastadomas = ''
        gastosnp = self.pasar_dic_array(gastos)
        for mesg, gasto in gastos.items():     
            if (maxgasto > gasto):
                Mesgastadomas = mesg 
                maxgasto = gasto
        return (Mesgastadomas, np.amin(gastosnp))

    def mes_mas_ahorrado(self, ingresos):
        """
        Método mes_mas_ahorrado. Calcula de un diccionario el mes y la cantidad que mas se ha ahorrado
        Inputs:
           ingreos: tipo diccionario
        Outputs:
           mes
           valor de este mes mas ahorrado
        """
        maxingreso = 0    
        Mesahorradomas = ''
        ingresosnp = self.pasar_dic_array(ingresos)
        for mes, ingreso in ingresos.items():  
            if (maxingreso < ingreso):
                maxingreso = ingreso
                Mesahorradomas = mes 
        return (Mesahorradomas, np.amax(ingresosnp))  

    def media_gastos_anual(self, gastos):
        """
        Método media_gastos_anual. Calcula de un diccionario la media de gastos anual
        Inputs:
           gastos: tipo diccionario
        Outputs:
           media de gastos anual
        """
        gastosnp = self.pasar_dic_array(gastos)
        return np.mean(gastosnp)    
        
    def total_gastos_anual(self, gastos):
        """
        Método total_gastos_anual. Calcula de un diccionario el total de gastos anual
        Inputs:
           gastos: tipo diccionario
        Outputs:
          total de gastos anual
        """
        return sum(gastos.values())

    def total_ingresos_anual(self, ingresos):
        """
        Método total_ingresos_anual. Calcula de un diccionario el total de ingresos anual
        Inputs:
            ingresos: tipo diccionario
        Outputs:
            total de ingresos anual
        """
        return sum(ingresos.values())    
    
    def pintar_grafica(self, meses, datosingresos):
        """
        Método pintar_grafica. Pinta la grafica de barras dados unos valores pasados por parametro
        Inputs:
            meses: lista de encabezados del dataframe
            ingresos: datos de los totales de ingresos
        Outputs:
            ventana con grafica
        """
        plt.bar(meses,datosingresos, color={'b','g','r','m','c','y','orange','purple','brown','blue','pink'})  
        plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
        plt.xlabel("Meses del año")  
        plt.ylabel("Ingresos")  
        plt.title("Evolución de ingresos de todo el año")
        plt.show()
        plt.savefig('vertical_barras.png')
        
    def leer_csv(self, fichero):
        """
        Método leer_csv. Lee un fichero csv y lo convierte en dataframe conprobando si existe
        Inputs:
            fichero: fichero csv
        Outputs:
            dataframe
        """
        try:
            df = pd.read_csv(fichero, skipinitialspace=True, sep='\t', decimal=',', index_col=False)
            return df
        except IOError:
            print ("No encuentro el fichero o no puedo leerlo")
            return np.empty
            
    def operar_csv(self, csv): 
        """
        Método operar_csv. Llama a los anteriores métodos realizando los calculos necesarios 
        Inputs:
            fichero: fichero csv
        Outputs:
            todos los calculos de esta aplicacion
        """ 
        try:
            ingresos = {}
            gastos = {}
            df = self.leer_csv(csv)
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
        mes, maxmesgasto =  self.mes_mas_gastado(gastos)
        print(f'El mes que se ha gastado más {mes} {maxmesgasto}')
        mesahorro, maxmes = self.mes_mas_ahorrado(ingresos)
        print(f'El mes que se ha ahorrado más {mesahorro} {maxmes}')   
        print(f'La media de gastos anual  es  {self.media_gastos_anual(gastos)}')
        print(f'El gasto total anual es {self.total_gastos_anual(gastos)}')  
        print(f'Los ingresos totales a lo largo del año son {self.total_ingresos_anual(ingresos)}')
        
        #Pintamos la grafica con los datos del dataframe
        dataingresos = list(ingresos.values())
        self.pintar_grafica(df.columns,dataingresos)
    

