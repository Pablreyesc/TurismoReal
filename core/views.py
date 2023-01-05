from dataclasses import dataclass
import email

from this import d
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
#Importar al usuario
from django.contrib.auth.models import User, Group
#Librerias de autentificación
from django.contrib.auth import authenticate,logout,login as login_autent
#--
from django.contrib.auth.decorators import login_required,permission_required
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import DeptoForm
from core.models import Arrendado, Checkin, Checkout, Costumer, Departamento, Inventario, ServicioExtra1, Ubicacion, Order, Rentar, OrdenDeCompra1
# Create your views here.
from .decorators import allowed_users
from core import webpay
from core import utilidades
from django.contrib import messages

import datetime




#IMPORT FOR PDF
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


def home(request):
    return render(request, 'core/index.html')

def depto(request):
    departamento = Departamento.objects.all()
    inventario = Inventario.objects.all()
    ubicacion = Ubicacion.objects.all()

    data = {

        'departamento': departamento,
        'inventario': inventario,
        'ubicacion': ubicacion,
        'form': DeptoForm()
    }
    return render(request, 'core/departamentos.html',data)

def deptoUnico(request, id_depto):
    departamento = get_object_or_404(Departamento, id_depto=id_depto)
    costumer = Costumer.objects.all()

    lista = [departamento]

    data = {

        'departamento': lista,
        'usuario':costumer
    }
    return render(request, 'core/Deptos.html',data)

def contacto(request):
    return render(request, 'core/contacto.html')

def registrodepartamento(request):
    return render(request, 'core/registrodepartamento.html')   

def logout_vista(request):
    logout(request)
    return render(request,'core/index.html')    

def login(request):
    if request.POST:
        usuario = request.POST.get("txt_usuario")
        password = request.POST.get("txt_pass")
        us = authenticate(request,username=usuario,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            return render(request,'core/index.html',{'msg':'ususario  registrado'})
        else:
            return render(request,'core/login.html',{'msg':'ususario no registrado'})

    return render(request, 'core/login.html')

def registro(request):
    if request.POST:
        nombre  = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        correo = request.POST.get("txtEmail")
        try:
            u = User.objects.get(email=correo)
            messages.success(request, "Correo ya registrado")
            return render(request, 'core/registro.html')
        except:
            usuario = request.POST.get("txtUsuario")
            passs = request.POST.get("txtPass")
        try:
            u = User.objects.get(username=usuario)
            messages.success(request, "Usuario existente")
            return render(request, 'core/registro.html')
        except:
            u = User()
            u.first_name = nombre
            u.last_name = apellido
            u.email = correo
            u.username = usuario
            u.set_password(passs)
            u.save()
            group = Group.objects.get(name='customer')
            u.groups.add(group)
            Costumer.objects.create(
                user=u,
                nombre=u.first_name,
                apellido=u.last_name
                )
            us = authenticate(request, username=usuario, password=passs)
            login_autent(request,us)
            return render(request, 'core/index.html')
    return render(request, 'core/registro.html')     

def listar_depa(request):

    departamento = Departamento.objects.all()
    inventario = Inventario.objects.all()
    ubicacion = Ubicacion.objects.all()
    costumer = Costumer.objects.all()

    data = {

        'departamento': departamento,
        'inventario': inventario,
        'ubicacion': ubicacion,
        'usuario':costumer,
        'form': DeptoForm()
    }
    if request.method == 'POST':
        formulario = DeptoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registrado Correctamente")
        else:
            data["form"] = formulario

        

    return render(request,'core/registrodepartamento.html',data) 

def modificar_departamento(request, id_depto):

    departamento = get_object_or_404(Departamento, id_depto=id_depto)

    data = {

        'form':DeptoForm(instance=departamento)
    }

    if request.method == 'POST':
        formulario = DeptoForm(data=request.POST, instance=departamento, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="registrodepto")
        data["form"] = formulario

    return render(request, 'core/registrodepartamento.html',data)

def eliminar_depto(request, id_depto):
    departamento = get_object_or_404(Departamento, id_depto=id_depto)
    departamento.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="registrodepto")

def reserva(request,id_depto,id_c):
    departamento = get_object_or_404(Departamento, id_depto=id_depto)
    costumer = Costumer.objects.get(user=id_c)
    servicio = ServicioExtra1.objects.all()


    lista = [departamento]

    data = {

        'departamento': lista,
        'servicio':servicio
    }

    if request.method == 'POST':

        
        fecha = request.POST.get("txtFechaReserva")
        fechan = fecha.replace("-", '')
        fechaActual = datetime.date.today()
        fechaActual = str(fechaActual).replace("-",'')
        print(fechan)
        print(fechaActual)
        comentario = request.POST.get("txtComentario")
        valor = request.POST.get("txtValor")
        acompanante = request.POST.get("txtAcompanante")
        depaid = get_object_or_404(Departamento, id_depto=id_depto)
        costumer = costumer
        estado = "No disponible"

        if fechan < fechaActual:
            messages.add_message(request, messages.INFO, 'Le quedan 2 intentos más.')
            return render(request, 'core/reserva.html',data)
        else:

            reserva = Order(
                fecha_reserva = fecha,
                comentario= comentario,
                valor = valor,
                cant_acompanante=acompanante,
                departamento_id_depto=depaid,
                customer=costumer

            )
            reserva.save()
            Departamento.objects.filter(id_depto=id_depto).update(estado=estado)
            messages.success(request, "Registrado Correctamente")
            return render(request, 'core/index.html')

    return render(request, 'core/reserva.html',data)

@allowed_users(allowed_roles=['customer'])
def lista_reserva(request):

    departamento = Departamento.objects.all()
    reserva = request.user.costumer.order_set.all()

    data = {

        'reserva':reserva,
        'departamento': departamento,



    }
    return render(request, 'core/modificareserva.html',data)

def eliminar_reserva(request,id_r):
    reserva = get_object_or_404(Order, id=id_r)
    estado = "Disponible"
    reserva.delete()
    messages.success(request, "Eliminado Correctamente")
    Departamento.objects.filter(id_depto=reserva.departamento_id_depto.id_depto).update(estado=estado)
    return redirect(to="modificar_reserva")

def pago(request,id_r,id_c,id_depto):
    reserva = get_object_or_404(Order, id=id_r)
    depaid = get_object_or_404(Departamento, id_depto=id_depto)
    costumer = Costumer.objects.get(user=id_c)
    lista = [reserva]

    data = {
        'reserva':lista,
        'usuario':costumer

    }
    return render(request, 'core/pago.html',data)

def carro_webpay(request, id_r,id_c,id_depto):
    print("id depto:"+str(id_r))
    reserva = get_object_or_404(Order, id=id_r)
    costumer = Costumer.objects.get(user=id_c)
    print("HOLA ENTRE"+request.method)
    if request.method == 'POST':
        result=webpay.crearTransaccion(id_r,id_c,id_depto)
        return render(request, 'core/contacto.html', {'url': result['url'], 'token': result['token']})
    return render(request, 'core/pago.html')

def pdf(request,id_r):
    reserva = get_object_or_404(Order, id=id_r)
    lista = [reserva]

    data = {
        'reserva':lista
    }
    template_path = 'core/pdf.html'
    context = data  

    # Crear objeto django tipo response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="DetalleReserva.pdf"'

    # Renderizado de la template
    template = get_template(template_path)
    html = template.render(context)

    # Crear el pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
       
    # En caso de error, avisa aqui
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def arriendo(request,id_r,id_depto, id_c):
    departamento = get_object_or_404(Departamento, id_depto=id_depto)
    reserva = get_object_or_404(Order, id=id_r)
    costumer = Costumer.objects.get(user=id_c)

    lista = [reserva]

    data = {
        "departamento":departamento,
        "reserva":lista
    }
    #revisar crud
    if request.method == 'POST':

       
        valor = request.POST.get("txtValor")
        condicion = request.POST.get("txtCondicion")
        fechainicio = request.POST.get("txtCheckin")
        fechasalida = request.POST.get("txtCheckout")
        departamento = get_object_or_404(Departamento, id_depto=id_depto)
        costumer = Costumer.objects.get(user=id_c)

        rest = Arrendado(
            tarifa=valor,
            condicion=condicion,
            departamento_id_depto=departamento,
            checkout=fechasalida,
            checkin=fechainicio,
            customer=costumer

        )
        rest.save()
        

        checkin = Checkin(
            fecha_ingreso = fechainicio
        )
        checkin.save()
        checkout = Checkout(
            fecha_regreso = fechasalida
        )
        checkout.save()
        

    return render(request, 'core/arriendo.html',data)

def lista_arriendo(request):

    departamento = Departamento.objects.all()
    arriendo = OrdenDeCompra1.objects.all()
    arrendado = Arrendado.objects.all()

    data = {
        'departamento': departamento,
        'arriendo' : arrendado,
    }

    return render(request, 'core/listadoArriendos.html',data)

def pdfArriendo(request,id_a):
    arriendo = get_object_or_404(Arrendado, id=id_a)
    lista = [arriendo]

    data = {
        'arrendado': lista,   
    }
    template_path = 'core/pdfArriendo.html'
    context = data  

    # Crear objeto django tipo response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="DetalleArriendo.pdf"'

    # Renderizado de la template
    template = get_template(template_path)
    html = template.render(context)

    # Crear el pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    
    # En caso de error, avisa aqui
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def carro_webpay_respuesta(request):
    userid = request.user.id
    costumer = Costumer.objects.get(user=userid)
    if not request.GET.get('token_ws'):
        raise Http404
    token=request.GET.get('token_ws')
    result=webpay.verificarTransaccion(token)
    #return render(request, 'carro/webpay_respuesta.html', {'result': result[0]})
    #return HttpResponse(result[0])
    if result[0]=='vacio':
        raise Http404
    if result[0]=='AUTHORIZED':
        try:
            orden=OrdenDeCompra1.objects.filter(customer=costumer, estado_id=3).get()
        except OrdenDeCompra1.DoesNotExist:
            raise Http404
        OrdenDeCompra1.objects.filter(customer=costumer, estado_transbank=0).update(token_ws= token, estado_transbank=result[0], fecha_transbank=result[2], tarjeta=result[1], estado_id=6)
        
        #datos=Departamento.objects.filter(Departamento, id_depto=id_depto).order_by('-id').all()
        messages.add_message(request, messages.SUCCESS, f'La orden de compra N° {orden.id} ha sido generada exitosamente. Tu número de transacción de Transbank es {token} .Nos pondremos en contacto contigo a la brevedad para coordinar el envío de los productos. Gracias por tu compra!!! ')
        return render(request, 'core/index.html')
    if result[0]=='FAILED':
        OrdenDeCompra1.objects.filter(customer=request.session['customer']).filter(estado_transbank=0).update(token_ws= token, fecha_transbank=result[2], tarjeta=result[1], estado_id=5)
        return HttpResponseRedirect('')
    








