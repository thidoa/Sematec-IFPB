from django.contrib import admin
from .models import Medico, Cliente, Consulta

# Register your models here.

@admin.register(Medico)

class medicoAdmin(admin.ModelAdmin):
    list_display = ('crm', 'crm_UF', 'cep', 'areaAtuacao')
    list_filter = ('areaAtuacao', )

@admin.register(Cliente)

class clienteAdmin(admin.ModelAdmin):
    list_display = ('num_pais', 'num_ddd', 'num_telefone', 'cep', )

@admin.register(Consulta)

class consiltaAdmin(admin.ModelAdmin):
    list_display = ('id_med', 'id_cli', 'data_requisito', 'data_consulta', 'obs', 'link_consulta', 'status', 'documento', )
