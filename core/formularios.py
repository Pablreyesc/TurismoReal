from home.models import *
from datetime import date
from django.utils.html import format_html
from utilidades import dreamhost

def getFechaActual():
	return date.today()

def get_perfiles_choices():
    return [
        (valve.pk, valve.nombre) for valve in Perfiles.objects.all()
    ]

def get_paises_choices():
    return [
        (valve.pk, valve.nombre) for valve in Pais.objects.all()
    ]


def get_estados_choices():
    return [
        (valve.pk, valve.nombre) for valve in Estado.objects.filter(id__in=[1, 2]).all()
    ]

def get_estados_obra_choices():
    return [
        (valve.pk, valve.nombre) for valve in Estado.objects.filter(id__in=[3, 4]).all()
    ]



def get_generos_choices():
    return [
        (valve.pk, valve.nombre) for valve in Genero.objects.all()
    ]

def get_producto_categoria_choices():
    return [
        (valve.pk, valve.nombre) for valve in ProductoCategoria.objects.all()
    ]

def get_proveedor_choices():
    return [
        (valve.pk, valve.nombre) for valve in Proveedor.objects.all()
    ]

def get_servicios_choices():
    return [
        (valve.pk, valve.nombre) for valve in Servicio.objects.all()
    ]
############HELPERS MODELOS

def set_estado(obj):
    return obj.estado.nombre
set_estado.short_description = 'Estado'

def set_genero(obj):
    return obj.genero.nombre
set_genero.short_description = 'Género'

def set_pais(obj):
    return obj.pais.nombre
set_pais.short_description = 'País'

def set_perfiles(obj):
    return obj.perfiles.nombre
set_perfiles.short_description = 'Perfil'

def set_user(obj):
    return f"{obj.user.first_name} {obj.user.last_name}"
set_user.short_description = 'Usuario'


def set_users_metadata(obj):
    return f"{obj.users_metadata.user.first_name} {obj.users_metadata.user.last_name}"
set_users_metadata.short_description = 'Usuario'


def set_producto_categoria(obj):
    return obj.producto_categoria.nombre
set_producto_categoria.short_description = 'Categoría'


def set_producto(obj):
    return obj.producto.nombre
set_producto.short_description = 'Producto'


def set_correo(obj):
    return obj.user.username
set_correo.short_description = 'E-Mail'


def get_descripcion(obj):
    return format_html(f"""<div style="word-wrap: break-word;width:200px;">{obj.descripcion[0:100]}......</div>""")
get_descripcion.short_description = 'Descripción'


def get_foto_producto(obj):
    if dreamhost.existeArchivo('producto', obj.foto)==False:
        dreamhost.moverArchivoProducto(obj.foto, obj.id)
    return format_html(f"""<a href="/assets/upload/producto/{obj.foto}" target="_blank">{obj.foto}</a>""")
get_foto_producto.allow_tags = True
get_foto_producto.short_description="Foto"




def get_foto_producto_galeria(obj):
    if dreamhost.existeArchivo('producto', obj.foto)==False:
        dreamhost.moverArchivoProductoGaleria(obj.foto, obj.id)
    return format_html(f"""<a href="/assets/upload/producto/{obj.foto}" target="_blank">{obj.foto}</a>""")
get_foto_producto_galeria.allow_tags = True
get_foto_producto_galeria.short_description="Foto"