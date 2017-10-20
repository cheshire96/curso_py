'''
COSAS QUE HACER

-- obtener datos del dataset
-- que mes fue el mas caro y cual el mas barato
-- promedio anual del precio
- verificar que los datos ingresados son validos
CRUD:
--	mostrar todos los datos
	ingresar nuevo mes y año mientras no sea superior al actual
	modificar algun precio o dato
	eliminar


ordenar los datos por anio y mes
-- buscar todos los datos de un producto()

Nota: lo que tiene las dos rayitas adelante ya esta. lo que tiene una rayita adelante esta a medias

'''

from flask import Flask
from flask import request
from flask import render_template
from decimal import Decimal
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt


app = Flask(__name__)

def obtener_datos():
	#obtiene los valores del archivo csv
	df = pd.read_csv("precio-promedio-por-litro-de-leche.csv",encoding = "ISO-8859-1",sep=';', header=None)
	return df

def obtener_datos_por_anio(anio):
	lista_t_p=lista_precios()#listado de todos los precios registrados
	lista_r=[]
	lista_p=[]
	j=len(lista_t_p)
	
	for i in range(1,j):
		a=lista_t_p[i][0]
		if anio==a:
			m=lista_t_p[i][1]
			pre=lista_t_p[i][2]
			lista_r.insert(0, a)#anio
			lista_r.insert(1, m)#mes
			lista_r.insert(2, pre)#precio		
			lista_p.insert(i, lista_r.copy())
			lista_r.clear()
	return lista_p

	
	
		
def lista_precios():
	#obtiene listado de precios promedios por mes y anio
	datos=obtener_datos()
	lista_r=[]
	lista_p=[]
	j=len(datos)
	for i in range(1,j):
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
	if request.method == 'POST':
		#precios=promedio_anual(2016)
		#precios=comparar(2016,'menor')
		#print (precios) 
		return graficar()
		
def comparar(anio,comparador):
	#compara cual mes/anio es el menor o mayor
	
	pre_m=[]
	pre_m.insert(0,0)
	pre_m.insert(1,0)
	pre_m.insert(2,0)
	
	lista_r=[]
	lista=obtener_datos_por_anio(anio)
	j=len(lista)
	if(comparador=='mayor'):
		#recorre la lista y busca cual es el mayor
		for i in range(0,j):
			pre=lista[i][2]
			if pre>pre_m[2]:
				pre_m[0]=lista[i][0]
				pre_m[1]=lista[i][1]
				pre_m[2]=pre
		
	elif(comparador=='menor'):
		#recorre la lista y busca cual es el menor
		for i in range(0,j):
			pre=lista[i][2]
			if (pre<pre_m[2]) or (pre_m[2]==0):
				pre_m[0]=lista[i][0]
				pre_m[1]=lista[i][1]
				pre_m[2]=pre	
	else:
		#error el comparador no es valido
		pass
	return pre_m


def promedio_anual(anio):
	#calcula el promedio anual
	lista=obtener_datos_por_anio(anio)
	t_pre=0#total de precio
	j=len(lista)
	for i in range(0,j):
		t_pre+=lista[i][2]
	return t_pre/12 #devuelve el precio promedio que tuvo en un anio
	

def verificar_datos(datos):
	#verifica que los datos ingresados sean validos
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
	
