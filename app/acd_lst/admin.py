from django.contrib import admin
from .models import *
#List, Rubricas, CargoEmprego, OrgaoSiape, GratPontuacao, GratValorPonto, T21ListaTabelasDCP, T01TabelaDCP

class RubricasAdmin(admin.ModelAdmin):
	list_display = ['codigorubrica', 'nomerubrica']
	orderby = ['codigorubrica']

class GratValorPontoAdmin(admin.ModelAdmin):
	list_display = ('nomegrat','datainicio','datafinal','nivel','classe','padrao','valorponto')

class GratPontuacaoAdmin(admin.ModelAdmin):
	list_display = ('nomegrat','pontuacao','datainicio','datafinal')

class CargoEmpregoAdmin(admin.ModelAdmin):
	list_display = ('codcargo','codgrupocargo','nomecargo', 'nivel')

class OrgaoSiapeAdmin(admin.ModelAdmin):
	list_display = ('codigo','nome')
	orderby = ['nome']




class T01TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t01_data','t01_cod_indexador','t01_var_per_mensal','t01_num_indice_var_mensal','t01_fator_vigente','t01_indice_correcao')
	ordering = ['t01_data']

class T02TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t02_data','t02_cod_indexador','t02_var_per_mensal','t02_num_indice_var_mensal','t02_fator_vigente','t02_indice_correcao')
	ordering = ['t02_data']

class T03TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t03_data','t03_cod_indexador','t03_var_per_mensal','t03_num_indice_var_mensal','t03_fator_vigente','t03_indice_correcao')
	ordering = ['t03_data']	

class T04TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t04_data','t04_cod_indexador','t04_var_per_mensal','t04_num_indice_var_mensal','t04_fator_vigente','t04_indice_correcao')
	ordering = ['t04_data']	

class T05TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t05_data','t05_cod_indexador','t05_var_per_mensal','t05_num_indice_var_mensal','t05_fator_vigente','t05_indice_correcao')
	ordering = ['t05_data']	

class T06TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t06_data','t06_cod_indexador','t06_var_per_mensal','t06_num_indice_var_mensal','t06_fator_vigente','t06_indice_correcao')
	ordering = ['t06_data']		

class T07TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t07_data','t07_cod_indexador','t07_var_per_mensal','t07_num_indice_var_mensal','t07_fator_vigente','t07_indice_correcao')
	ordering = ['t07_data']

class T08TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t08_data','t08_cod_indexador','t08_var_per_mensal','t08_num_indice_var_mensal','t08_fator_vigente','t08_indice_correcao')
	ordering = ['t08_data']

class T09TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t09_data','t09_cod_indexador','t09_var_per_mensal','t09_num_indice_var_mensal','t09_fator_vigente','t09_indice_correcao')
	ordering = ['t09_data']

class T10TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t10_data','t10_cod_indexador','t10_var_per_mensal','t10_num_indice_var_mensal','t10_fator_vigente','t10_indice_correcao')
	ordering = ['t10_data']

class T11TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t11_data','t11_cod_indexador','t11_var_per_mensal','t11_num_indice_var_mensal','t11_fator_vigente','t11_indice_correcao')
	ordering = ['t11_data']				

class T12TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t12_data','t12_cod_indexador','t12_var_per_mensal','t12_num_indice_var_mensal','t12_fator_vigente','t12_indice_correcao')
	ordering = ['t12_data']	

class T13TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t13_data','t13_cod_indexador','t13_var_per_mensal','t13_num_indice_var_mensal','t13_fator_vigente','t13_indice_correcao')
	ordering = ['t13_data']

class T14TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t14_data','t14_cod_indexador','t14_var_per_mensal','t14_num_indice_var_mensal','t14_fator_vigente','t14_indice_correcao')
	ordering = ['t14_data']			

class T15TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t15_data','t15_cod_indexador','t15_var_per_mensal','t15_num_indice_var_mensal','t15_fator_vigente','t15_indice_correcao')
	ordering = ['t15_data']





class T21TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t21_data','t21_cod_indexador','t21_var_per_mensal','t21_num_indice_var_mensal','t21_fator_vigente','t21_indice_correcao')
	ordering = ['t21_data']	

class T22TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t22_data','t22_cod_indexador','t22_var_per_mensal','t22_num_indice_var_mensal','t22_fator_vigente','t22_indice_correcao')
	ordering = ['t22_data']

class T23TabelaDCPAdmin(admin.ModelAdmin):
	list_display = ('t23_data','t23_cod_indexador','t23_var_per_mensal','t23_num_indice_var_mensal','t23_fator_vigente','t23_indice_correcao')
	ordering = ['t23_data']




class T21ListaTabelasDCPAdmin(admin.ModelAdmin):
	list_display = ('t21_cod_tabela','t21_nome_tabela', 't21_obs_tabela', 't21_indexador')
	ordering = ['t21_cod_tabela']



admin.site.register(List)
admin.site.register(CargoEmprego,CargoEmpregoAdmin)
admin.site.register(OrgaoSiape,OrgaoSiapeAdmin)
admin.site.register(Rubricas, RubricasAdmin)
admin.site.register(GratValorPonto, GratValorPontoAdmin)
admin.site.register(GratPontuacao, GratPontuacaoAdmin)

admin.site.register(T21ListaTabelasDCP,T21ListaTabelasDCPAdmin)

admin.site.register(T01TabelaDCP,T01TabelaDCPAdmin)
admin.site.register(T02TabelaDCP,T02TabelaDCPAdmin)
admin.site.register(T03TabelaDCP,T03TabelaDCPAdmin)
admin.site.register(T04TabelaDCP,T04TabelaDCPAdmin)
admin.site.register(T05TabelaDCP,T05TabelaDCPAdmin)
admin.site.register(T06TabelaDCP,T06TabelaDCPAdmin)
admin.site.register(T07TabelaDCP,T07TabelaDCPAdmin)
admin.site.register(T08TabelaDCP,T08TabelaDCPAdmin)
admin.site.register(T09TabelaDCP,T09TabelaDCPAdmin)
admin.site.register(T10TabelaDCP,T10TabelaDCPAdmin)
admin.site.register(T11TabelaDCP,T11TabelaDCPAdmin)
admin.site.register(T12TabelaDCP,T12TabelaDCPAdmin)
admin.site.register(T13TabelaDCP,T13TabelaDCPAdmin)
admin.site.register(T14TabelaDCP,T14TabelaDCPAdmin)
admin.site.register(T15TabelaDCP,T15TabelaDCPAdmin)


admin.site.register(T21TabelaDCP,T21TabelaDCPAdmin)
admin.site.register(T22TabelaDCP,T22TabelaDCPAdmin)
admin.site.register(T23TabelaDCP,T23TabelaDCPAdmin)