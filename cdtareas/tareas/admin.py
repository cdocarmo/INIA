from django.contrib import admin
from models import *

class TareaAdmin(admin.ModelAdmin):
	fieldsets = (
			(None, {
					'fields': (('nombre', 'status', 'fecha'), 
						('aquien', 'dquien'), 'detalle')
				}),
		)
	list_display = ['nombre', 'status', 'detalle', 'fecha']
	list_filter = ['fecha']
	search_fields = ('nombre', )
	ordering = ('nombre', )

admin.site.register(Tarea, TareaAdmin)
