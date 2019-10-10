from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import redirect

from .models import *

#admin .site.register(Cliente)
#admin .site.register(Vehiculo)
#admin .site.register(Empleado)
#admin .site.register(Cotizacion)

class EmpleadoInline(admin.TabularInline):
	model = Empleado
	extra = 1
	fields = ('nombre_Empleado', 'codigo_Empleado','iniciales')

	def has_delete_permition(self, request, obj):
		return False

class UserAdmin(UserAdmin):
	model = User
	inlines = [EmpleadoInline, ]

class ClienteAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['nombre_Cliente','celular_Cliente','correo_Cliente']}),
	]
	
	def save_model(self, request, obj, form, change):
		obj.empleado=request.user.empleado
		super().save_model(request, obj, form, change)

	def response_add(self, request, obj, post_url_continue=None):
		return redirect('/admin/cotizador/vehiculo/add')

	def response_change(self, request, obj, post_url_continue=None):
		return redirect('/admin/cotizador/vehiculo/add')

class VehiculoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['cliente','marca','linea','tipo','asientos','valor']}),
	]

	def get_readonly_fields(self,request,obj=None):
		if obj:
			return ['cliente','marca','linea','tipo','asientos','valor']
		else:
			return []

	def response_add(self, request, obj, post_url_continue=None):
		return redirect('/admin/cotizador/cotizacion/add')

	def response_change(self, request, obj, post_url_continue=None):
		return redirect('/admin/cotizador/cotizacion/add')

	def get_form(self, request, obj=None, **kwargs):
		form = super(VehiculoAdmin, self).get_form(request, obj, **kwargs)
		if not obj:
			form.base_fields['cliente'].queryset = Cliente.objects.all().order_by('-id')
			form.base_fields['cliente'].initial=Cliente.objects.last()
		return form


class CotizacionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Información de cotización: ', {'fields': ['vehiculo','deducible','deducible_robo','lesiones','accidentes','anual_valor_Seguro']}),
	]
	readonly_fields = ('deducible','deducible_robo','lesiones','accidentes','anual_valor_Seguro')

	def get_readonly_fields(self,request,obj=None):
		if obj:
			return ['vehiculo','deducible','deducible_robo','lesiones','accidentes','anual_valor_Seguro']
		else:
			return ['deducible','deducible_robo','lesiones','accidentes','anual_valor_Seguro']

	def get_form(self, request, obj=None, **kwargs):
		form = super(CotizacionAdmin, self).get_form(request, obj, **kwargs)
		if not obj:
			form.base_fields['vehiculo'].queryset = Vehiculo.objects.all().order_by('-id')
			form.base_fields['vehiculo'].initial=Vehiculo.objects.last()
		return form


admin.site.register([Cliente], ClienteAdmin)
admin.site.register([Vehiculo], VehiculoAdmin)
admin.site.register([Cotizacion], CotizacionAdmin)
admin.site.unregister(User)
admin.site.register([User], UserAdmin)
#admin.site.register(Empleado)
admin.site.site_header = 'Asrural'
admin.site.site_title = 'Cotizador 105 Asrural'
admin.site.index_title = 'Bienvenido al Cotizador Mi Carro Seguro'
