import datetime
import pandas as pd
import numpy as np
import csv

def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_minimo(datos_pandas, file_name)
    funcion_mediana(datos_pandas, file_name) 
    funcion_promedio(datos_pandas, file_name)
    funcion_desviacion(datos_pandas, file_name)   
    """
    Inserte aqui las otras funciones.
    funcion_Minimo()
    funcion_Mediana()
    funcion_Promedio()
    funcion_Desviacion()
    funcion_Varianza()
    """
    datos_graficar = leer_datos(file_name)
    return datos_graficar

def funcion_maximo(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    dat_max=max(valores_temperatura)
    dato_guardar = [1, date_string, "Maximo", dat_max]
    guardar(dato_guardar, file_name)

def funcion_minimo(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    temp_min=min(valores_temperatura)
    dato_guardar = [1, date_string, "Minimo", temp_min]
    guardar(dato_guardar, file_name)

def funcion_mediana(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    temp_media=np.median(valores_temperatura)
    dato_guardar = [1, date_string, "Mediana", temp_media]
    guardar(dato_guardar, file_name)


def funcion_promedio(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    temp_promedio=np.mean(valores_temperatura)
    dato_guardar = [1, date_string, "Promedio", temp_promedio]
    guardar(dato_guardar, file_name)


def funcion_desviacion(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    temp_desviacion=np.std(valores_temperatura)
    dato_guardar = [1, date_string, "Desviacion",temp_desviacion]
    guardar(dato_guardar, file_name)


def funcion_varianza(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    varianza_temp=np.var(valores_temperatura)
    dato_guardar = [1, date_string, "Varianza", varianza_temp]
    guardar(dato_guardar, file_name)


def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas


def guardar(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)
