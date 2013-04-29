# coding=UTF-8

from django.db import models
from django.utils.translation import ugettext as _
import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from userprofile.models import UserProfile
# Create your models here.

class Tarea(models.Model):
	TERMINADA = 1
	ACTIVA = 2
	NEGADA = 3
	STATUS = (
			(TERMINADA, _('TERMINADA')),
			(ACTIVA, _('ACTIVA')),
			(NEGADA, _('NEGADA')),
			)
	nombre = models.CharField(max_length=200)
	slug = models.SlugField(editable=False)
	detalle = models.TextField()
	aquien = models.ForeignKey(UserProfile, related_name='Usuario')
	dquien = models.ForeignKey(UserProfile, related_name='Solicitante')
	status = models.IntegerField(choices=STATUS, default=2)
	fecha_creacion = models.DateTimeField(auto_now=True)
	fecha = models.DateTimeField(blank=True, null=True)


	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.aquien.user.username + "-" + self.nombre)
		super(Tarea, self).save(*args, **kwargs)		
