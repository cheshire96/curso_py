'''

COSAS QUE HACER

-- obtener datos del dataset
-que anio/mes fue el mas caro y cual el mas barato
-promedio anual del precio
un grafico de como varia el precio
- verificar que los datos ingresados son validos
CRUD:
--	mostrar todos los datos
	ingresar nuevo mes y año mientras no sea superior al actual
	modificar algun precio o dato
	eliminar


ordenar los datos por anio y mes
buscar todos los datos de un anio()
comparar anualmente en x mes(ejemplo: cuanto valio en el mes 2 en todos los anios)


Nota: lo que tiene las dos rayitas adelante ya esta. lo que tiene una rayita adelante esta a medias


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
from decimal import Decimal
import pandas as pd
import numpy as np
import datetime


app = Flask(__name__)


def obtener_datos():
	#obtiene los valores del archivo csv
	df = pd.read_csv("precio-promedio-por-litro-de-leche.csv",encoding = "ISO-8859-1",sep=';', header=None)
	return df
	
def lista_precios():
	#obtiene listado de precios promedios por mes y anio
	datos=obtener_datos()
	lista_r=[]
	lista_p=[]
	for i in range(1,75):
		anio=int(datos[2][i])
		mes=int(datos[3][i])
		pre=Decimal(datos[6][i].replace(',', '.'))
		lista_r.insert(0, anio)#anio
		lista_r.insert(1, mes)#mes
		lista_r.insert(2, pre)#precio
		
		lista_p.insert(i, lista_r.copy())
		lista_r.clear()
	return lista_p

@app.route('/datos', methods=['GET', 'POST'])
def datos():
	if request.method == 'GET':
		datos=obtener_datos()
		return render_template('datos.html', l=datos)#retorna un template que muestra el listado completo de los datos
	elif request.method == 'POST':
		
		mensaje=verificar_datos(request.form)
		if mensaje=='ok':
			return 'Todo ok'
		else:
			return mensaje
	else:
		return 'Metodo no soportado'
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
	if request.method == 'GET':
		datos=obtener_datos()
		return render_template('formulario.html')#retorna un template con un formulario
	if  request.method == 'POST':
		precios=promedio_anual(2016)
		print (precios) 
		
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

def promedio_anual(anio):
	#calcula el promedio anual
	#usa lista precio
	lista_t_p=lista_precios()#listado de todos los precios registrados
	t_pre=0#total de precio
	for i in range(1,74):
		a=lista_t_p[i][0]
		pre=lista_t_p[i][2]
		if anio==a:
			t_pre+=pre
	return t_pre/12
	

def verificar_datos(datos):
	#verifica que los datos ingresados sean validos
	pass
	#datos que tiene:
	#Pais_id Pais Anio Mes ccpa Producto Precio_promedio_Kg Moneda_id
	if datos['pais']!='Argentina':
		return 'El pais no es valido'
		
	if datos['producto']!='Leche cruda':
		return 'El producto no es valido'

	x = datetime.datetime.now()
	if int(datos['anio'])>x.year:
		return 'El anio ingresado no es valido'
	if int(datos['mes'])>x.month:
		return 'El mes ingresado no es valido'
		

def graficar(datos):
	#grafica como varia el precio. Puede ser tanto anual como periodicamente(?????????)
	pass
