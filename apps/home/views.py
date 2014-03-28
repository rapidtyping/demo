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

def contacto_view(request):
    formulario = ContactForm()
    ctx = {'form':formulario}
    return render_to_response('home/contacto.html',
                              ctx,
                              context_instance=RequestContext(request))
