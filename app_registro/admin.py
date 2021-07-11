from django.contrib import admin
from .models import  Clientes, Cuenta,Depocito, Retiro

admin.site.register(Clientes)

# ------------------------------------------------------------------------
#class CuentaaAdmin(admin.ModelAdmin):
 #   list_display = ('id', 'fecha_registo', 'estado', 'saldo', 'clientes')
  #  list_editable = ('estado')

admin.site.register(Cuenta)
admin.site.register(Depocito)
admin.site.register(Retiro)

# Register your models here.
