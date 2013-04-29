# coding=UTF-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from forms import *
from tareas.models import Tarea
from userprofile.models import UserProfile

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
			return HttpResponseRedirect('/')
    else:
        formulario = TareaForm()
    return render_to_response('tarea/nuevatarea.html',
    	{'formulario':formulario}, 
    	context_instance=RequestContext(request))# Create your views here.
