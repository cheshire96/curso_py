'''
COSAS QUE HACER

que anio/mes fue el mas caro y cual el mas barato
promedio anual del precio
ingresar nuevo mes y año mientras no sea superior al actual
modificar algun precio o dato
eliminar
un grafico de como varia el precio
verificar que los datos ingresados son validos

OPCIONAL
guardar en una base:
	se tiene 3 entidades(????)
	el pais(pais_id,pais)
	producto(año,mes,ccpa[es como un codigo],producto,precio_promedio_kg)
	moneda(moneda_id)

'''

from flask import Flask
from flask import request
from flask import render_template

import pandas as pd
import numpy as np
app = Flask(__name__)

'''
@app.route('/hello/')
@app.route('/hello/<nombre>')
def hello(nombre=None):
	 return render_template('hola.html', nombre=nombre)
@app.route('/persona', methods=['GET', 'POST'])
def persona():
	if request.method == 'POST':
		return 'POST'
	else:
		return 'GET'
'''
@app.route('/prueba')
def obtener_datos():
	#obtiene los valores del archivo csv
	df_txt = pd.read_csv("precio-promedio-por-litro-de-leche.csv",encoding = "ISO-8859-1",sep=';', header=None)
	return 'hola(???????)'#ver como retornar los datos

def comparar(lista, comparador):
	#compara cual mes/anio es el menor o mayor
	if(comparador=='mayor'):
		#recorre la lista y busca cual es el mayor
		pass
	elif(comparador=='menor'):
		#recorre la lista y busca cual es el menor
		pass
	else:
		#error el comparador no es valido
		pass

def promedio_anual(meses):
	#calcula el promedio anual
	pass
	#primero se fija si hay 12 elementos en la lista, si no hay devuelve un error
	#suma los meses y despues los divide por 12

def verificar_datos():
	#verifica que los datos ingresados sean validos
	pass

def graficar(lista):
	#grafica como varia el precio. Puede ser tanto anual como periodicamente(?????????)
	pass