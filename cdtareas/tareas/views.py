# coding=UTF-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from forms import *
from tareas.models import Tarea, ComentarioTarea
from userprofile.models import UserProfile
import json
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage #Importamos la librería para enviar los correos


@login_required(login_url='/login')
def nueva_tarea(request):
    if request.method=='POST':
        formulario = TareaForm(request.POST)
        if formulario.is_valid():
            tarea = Tarea(
            fecha = formulario.cleaned_data['fecha'],
            nombre = formulario.cleaned_data['nombre'],
            detalle = formulario.cleaned_data['detalle'],
            aquien = formulario.cleaned_data['aquien'],
            dquien = request.user.get_profile())
            tarea.save()
            email = EmailMessage('Asunto', 'Mensaje', to=[request.user.email])
            email.send()
            return HttpResponseRedirect('/')
    else:
        formulario = TareaForm()
    return render_to_response('tarea/nuevatarea2.html',
    	{'formulario':formulario}, 
    	context_instance=RequestContext(request))# Create your views here.

@login_required(login_url='/login')
def detalle_tarea(request, tarea_slug):
    tarea = Tarea.objects.get(slug=tarea_slug)
    if request.method=='POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            xComent = ComentarioTarea(
            comentario=form.cleaned_data['comentario'],
            usuario=request.user.get_profile(),
            tarea=tarea)
            xComent.save()
            return HttpResponseRedirect('/')
    else:
        form = ComentarioForm()
    return render_to_response('tarea/ver_tarea.html',
        {'tarea':tarea, 'form':form}, 
        context_instance=RequestContext(request))



def cargo_tareasjs(request):
    
	tareas = Tarea.objects.filter(status=Tarea.ACTIVA).order_by("-fecha")
	data = serializers.serialize("json", tareas)
	return HttpResponse(data, mimetype="application/json; charset=uft8")

"""
def cargo_tareas(request):

	tareas = Tarea.objects.filter(status=Tarea.ACTIVA, aquien=request.user.get_profile()).order_by("-fecha")
	data = list()
	for tarea in tareas:
		data.append({ 'id': tarea.pk, 
		'nombre': tarea.nombre, 'slug': tarea.slug, 
		'detalle': tarea.detalle, 'fecha': str(tarea.fecha.date()),
		'dquien': str(tarea.dquien)})

	return HttpResponse(
		json.dumps({'tareas': data}),
		content_type="application/json; charset=uft8"
		)
"""
def cargo_tareas(request):
    tareas = Tarea.objects.filter(status=Tarea.ACTIVA, aquien=request.user.get_profile()).order_by("-fecha")

    paginator = Paginator(tareas, 25) # Show 25 contacts per page    
    page = request.GET.get('page')
    try:
        tareas = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        tareas = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        tareas = paginator.page(paginator.num_pages)

    return render_to_response('tarea/mistareas.html',
                            {'tareas':tareas}, 
                            context_instance=RequestContext(request))

def cargo_tareassoli(request):
    tareas = Tarea.objects.filter(status=Tarea.ACTIVA, dquien=request.user.get_profile()).order_by("-fecha")

    paginator = Paginator(tareas, 25) # Show 25 contacts per page    
    page = request.GET.get('page')
    try:
        tareas = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        tareas = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        tareas = paginator.page(paginator.num_pages)

    return render_to_response('tarea/tareassolicitadas.html',
                            {'tareas':tareas}, 
                            context_instance=RequestContext(request))    
