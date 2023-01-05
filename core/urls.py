from django.urls import path
from .views import deptoUnico, carro_webpay_respuesta,home, depto, lista_reserva,eliminar_reserva, pago, registro, carro_webpay, login,pdfArriendo,  contacto, lista_arriendo, logout_vista, listar_depa, modificar_departamento, pdf, eliminar_depto, reserva, arriendo

urlpatterns = [
    path('', home, name="index"),
    path('depto/', depto, name="departamento"),
    path('registro/', registro,name="registro"),
    path('registrodepto/', listar_depa, name="registrodepto"),
    path('depto/', listar_depa, name="depto"),
    path('login/', login, name="login"),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('contacto/', contacto, name="contacto"),
    path('modificar-depto/<id_depto>/', modificar_departamento, name="modificar_depto"),
    path('eliminar_depto/<id_depto>/', eliminar_depto, name="eliminar_depto"),
    path('deptoUnico/<id_depto>/', deptoUnico, name="deptoUnico"),
    path('reserva/<id_depto>/<id_c>/', reserva, name="reserva"),
    path('modificar_reserva/',lista_reserva, name="modificar_reserva"),
    path('arriendo/<id_r>/<id_depto>/<id_c>/',arriendo,name="arriendo"),
    path('eliminar_reserva/<id_r>/',eliminar_reserva,name="eliminar_reserva"),
    path('pago/<id_r>/<id_c>/<id_depto>/',pago, name="pago"),
    path('pdf/<id_r>/', pdf , name="pdfReserva"),
    path('listaArriendos/', lista_arriendo , name="listaArriendo"),
    path('pdfArriendo/<id_a>/', pdfArriendo , name="pdfArriendo"),
    path('webpay/<id_r>/<id_c>/<id_depto>/', carro_webpay, name="carro_webpay"),
    path('webpay-respuesta/', carro_webpay_respuesta, name="carro_webpay_respuesta"),
    

]