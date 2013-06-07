from django.forms import ModelForm
from django import forms
from tareas.models import Tarea
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.forms.extras.widgets import SelectDateWidget
import datetime



class TareaForm(forms.Form):

	fecha = forms.DateField(label='Fecha', 
		widget=forms.TextInput(
		attrs={'class':'dates', }), required=True)


	nombre = forms.CharField(label=_(u'Nombre'), max_length=30, 
                               widget=forms.TextInput(
                               attrs={'class':'input-text'}),
                               required=True)

	detalle = forms.CharField(label=u"Tarea", 
                            	required=False, 
                          		widget=forms.Textarea(
                          		attrs ={'class':'txt-area', 
                                        'cols': '70', 'rows': '3'}))


	aquien = forms.ModelChoiceField(queryset=UserProfile.objects.none())


	def __init__(self, *args, **kwargs):
		super(TareaForm, self).__init__(*args, **kwargs)
		self.fields['aquien'].queryset = UserProfile.objects.filter(user__is_active=True)


class ComentarioForm(forms.Form):
	comentario = forms.CharField(label=u"Comentario", 
                            	required=False, 
                          		widget=forms.Textarea(
                          		attrs ={'class':'txt-area', 
                                        'cols': '70', 'rows': '3'}))
