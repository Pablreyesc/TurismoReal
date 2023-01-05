import requests
import json
import random
from django.conf import settings
from .models import *
import jwt
from django.shortcuts import render, get_object_or_404, redirect




def crearTransaccion(id_r,id_c, id_depto):
	print("ingreso")
	#se crea la orden de compra
	datos=Order.objects.filter(id=id_r).order_by('id').all()
	costumer = Costumer.objects.get(user=id_c)
	depaid = get_object_or_404(Departamento, id_depto=id_depto)
	print("entro")
	for dato in datos:
		precio= dato.valor

	try:
		
		orden=OrdenDeCompra1.objects.filter(customer=costumer, departamento_id_depto=depaid,estado_id=3).get()
		print("filtro orden")
	except OrdenDeCompra1.DoesNotExist:
		orden=OrdenDeCompra1.objects.create(customer=costumer, departamento_id_depto=depaid,valor=precio,estado_id=3)
		print("creo orden")
		print(orden)


	buy_order = f"orden{orden.id}"
	session_id = str(random.randrange(1000000, 99999999))
	amount = precio
	ruta=f"{settings.BASE_URL}webpay-respuesta/"
	endpoint=settings.WEBPAY_URL
	payload={
		 "buy_order": buy_order,
		 "session_id": session_id,
		 "amount": amount,
		 "return_url": ruta
		}
	print('direccion:'+str(endpoint))
	print('ruta'+str(ruta))
	cabeceros = {'content-type': 'application/json', 'Tbk-Api-Key-Id': settings.WEBPAY_ID, 'Tbk-Api-Key-Secret': settings.WEBPAY_SECRET}
	response= requests.post(endpoint, json=payload, headers=cabeceros)
	#response.status_code
	respuesta=json.loads(response.text)
	print("token"+str(respuesta))
	#guardo el token recibido
	OrdenDeCompra1.objects.filter(id=orden.id).update(token_ws=respuesta['token'])
	#retorno token y URL
	ruta=f"{respuesta['url']}{respuesta['token']}"
	return respuesta


def verificarTransaccion(token):
	endpoint=f"{settings.WEBPAY_URL}/{token}"
	cabeceros = {'content-type': 'application/json', 'Tbk-Api-Key-Id': settings.WEBPAY_ID, 'Tbk-Api-Key-Secret': settings.WEBPAY_SECRET}
	response= requests.put(endpoint, headers=cabeceros)
	#response.status_code
	respuesta=json.loads(response.text)
	if response.status_code ==200:
		return [respuesta['status'], respuesta['card_detail']['card_number'], respuesta['transaction_date']]
	else:
		return ['vacio']