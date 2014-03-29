# -*- encoding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.ventas.models import Producto
from apps.home.forms import ContactForm


def index_view(request):
    return render_to_response('home/index.html', 
            context_instance=RequestContext(request))

def about_view(request):
    mensaje = "Esto es un mesanje desde mi vista"
    ctx = {'msg': mensaje}
    return render_to_response('home/about.html',
            ctx, 
            context_instance=RequestContext(request))

def productos_view(request):
    # Select * from ventas_productos where status = True
    mis_productos = Producto.objects.filter(status = True)
    ctx = {'productos': mis_productos}
    return render_to_response('home/productos.html',
                              ctx,
                              context_instance=RequestContext(request))

# Haremos cambios para recibir la información del POST
def contacto_view(request):
    info_enviado = False 
    email, texto, titulo = '','',''
    
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['Email']
            titulo = formulario.cleaned_data['Titulo']
            texto = formulario.cleaned_data['Texto']
    else:
        formulario = ContactForm()
    ctx = {'form':formulario, 'email':email, 
           'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
    return render_to_response('home/contacto.html',
                              ctx,
                              context_instance=RequestContext(request))

