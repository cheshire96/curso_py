'''

COSAS QUE HACER

-- obtener datos del dataset
que anio/mes fue el mas caro y cual el mas barato
promedio anual del precio
un grafico de como varia el precio
verificar que los datos ingresados son validos
CRUD:
--	mostrar todos los datos
	ingresar nuevo mes y año mientras no sea superior al actual
	modificar algun precio o dato
	eliminar


ordenar los datos por anio y mes
buscar todos los datos de un anio()
comparar anualmente en x mes(ejemplo: cuanto valio en el mes 2 en todos los anios)

Nota: lo que tiene las dos rayitas adelante ya esta

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

def obtener_datos():
	#obtiene los valores del archivo csv
	df = pd.read_csv("precio-promedio-por-litro-de-leche.csv",encoding = "ISO-8859-1",sep=';', header=None)
	return df
	
@app.route('/datos')
def mostrar_datos():
	datos=obtener_datos()
	return render_template('datos.html', l=datos)#retorna un template que muestra el listado completo de los datos
		
def comparar(lista, comparador):#ver si se puede hacer con un reduce
	#ejemplo:  reduce(comparar, lista)
	
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
