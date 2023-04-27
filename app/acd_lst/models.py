from django.db import models
from django import forms

"""
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
"""
NOME_GRATIFICACAO = (
	('GDATA','GDATA'),
	('GDPGTAS','GDPGTAS'),
	('GDASST','GDASST'),
	('GDPGPE','GDPGPE'),
	)


class T01TabelaDCP(models.Model):
	t01_data = models.DateTimeField('DATA', db_column='T01_DATA', blank=True, null=True)
	t01_cod_indexador = models.CharField('INDEXADOR', db_column='T01_INDEXADOR',max_length=20, blank=True, null=True)
	t01_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T01_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t01_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T01_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t01_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T01_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t01_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T01_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t01_data']
		verbose_name_plural = '1. Tabela c.m. cond. geral IPCA-e'



class T02TabelaDCP(models.Model):
	t02_data = models.DateTimeField('DATA', db_column='T02_DATA', blank=True, null=True)
	t02_cod_indexador = models.CharField('INDEXADOR', db_column='T02_INDEXADOR',max_length=20, blank=True, null=True)
	t02_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T02_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t02_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T02_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t02_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T02_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t02_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T02_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t02_data']
		verbose_name_plural = '2. Tabela IPCA-e + SELIC 2003-2009'



class T03TabelaDCP(models.Model):
	t03_data = models.DateTimeField('DATA', db_column='T03_DATA', blank=True, null=True)
	t03_cod_indexador = models.CharField('INDEXADOR', db_column='T03_INDEXADOR',max_length=20, blank=True, null=True)
	t03_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T03_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t03_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T03_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t03_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T03_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t03_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T03_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t03_data']
		verbose_name_plural = '3. Tabela TR até mar2015'



class T04TabelaDCP(models.Model):
	t04_data = models.DateTimeField('DATA', db_column='T04_DATA', blank=True, null=True)
	t04_cod_indexador = models.CharField('INDEXADOR', db_column='T04_INDEXADOR',max_length=20, blank=True, null=True)
	t04_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T04_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t04_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T04_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t04_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T04_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t04_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T04_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t04_data']
		verbose_name_plural = '4. Tabela TR até mar2015 + SELIC 2003-2009'



class T05TabelaDCP(models.Model):
	t05_data = models.DateTimeField('DATA', db_column='T05_DATA', blank=True, null=True)
	t05_cod_indexador = models.CharField('INDEXADOR', db_column='T05_INDEXADOR',max_length=20, blank=True, null=True)
	t05_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T05_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t05_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T05_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t05_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T05_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t05_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T05_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t05_data']
		verbose_name_plural = '5. Tabela c.m. TR jul2009 em diante'



class T06TabelaDCP(models.Model):
	t06_data = models.DateTimeField('DATA', db_column='T06_DATA', blank=True, null=True)
	t06_cod_indexador = models.CharField('INDEXADOR', db_column='T06_INDEXADOR',max_length=20, blank=True, null=True)
	t06_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T06_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t06_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T06_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t06_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T06_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t06_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T06_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t06_data']
		verbose_name_plural = '6. Tabela TR + SELIC 2003-2009'


class T07TabelaDCP(models.Model):
	t07_data = models.DateTimeField('DATA', db_column='T07_DATA', blank=True, null=True)
	t07_cod_indexador = models.CharField('INDEXADOR', db_column='T07_INDEXADOR',max_length=20, blank=True, null=True)
	t07_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T07_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t07_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T07_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t07_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T07_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t07_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T07_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t07_data']
		verbose_name_plural = '7. Tabela c.m. cond. geral TR set2017'



class T08TabelaDCP(models.Model):
	t08_data = models.DateTimeField('DATA', db_column='T08_DATA', blank=True, null=True)
	t08_cod_indexador = models.CharField('INDEXADOR', db_column='T08_INDEXADOR',max_length=20, blank=True, null=True)
	t08_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T08_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t08_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T08_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t08_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T08_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t08_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T08_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t08_data']
		verbose_name_plural = '8. TR até set2017 + SELIC 2003-2009'



class T09TabelaDCP(models.Model):
	t09_data = models.DateTimeField('DATA', db_column='T09_DATA', blank=True, null=True)
	t09_cod_indexador = models.CharField('INDEXADOR', db_column='T09_INDEXADOR',max_length=20, blank=True, null=True)
	t09_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T09_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t09_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T09_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t09_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T09_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t09_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T09_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t09_data']
		verbose_name_plural = '9. TR dez2013 IPCA-e jan2014'



class T10TabelaDCP(models.Model):
	t10_data = models.DateTimeField('DATA', db_column='T10_DATA', blank=True, null=True)
	t10_cod_indexador = models.CharField('INDEXADOR', db_column='T10_INDEXADOR',max_length=20, blank=True, null=True)
	t10_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T10_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t10_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T10_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t10_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T10_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t10_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T10_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t10_data']
		verbose_name_plural = '10. TR dez2013 IPCA-e jan2014-SELIC'



class T11TabelaDCP(models.Model):
	t11_data = models.DateTimeField('DATA', db_column='T11_DATA', blank=True, null=True)
	t11_cod_indexador = models.CharField('INDEXADOR', db_column='T11_INDEXADOR',max_length=20, blank=True, null=True)
	t11_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T11_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t11_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T11_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t11_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T11_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t11_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T11_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t11_data']
		verbose_name_plural = '11. Tabela c.m. desapropriação'



class T12TabelaDCP(models.Model):
	t12_data = models.DateTimeField('DATA', db_column='T12_DATA', blank=True, null=True)
	t12_cod_indexador = models.CharField('INDEXADOR', db_column='T12_INDEXADOR',max_length=20, blank=True, null=True)
	t12_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T12_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t12_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T12_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t12_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T12_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t12_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T12_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t12_data']
		verbose_name_plural = '12. Tabela c.m. benef. INPC'



class T13TabelaDCP(models.Model):
	t13_data = models.DateTimeField('DATA', db_column='T13_DATA', blank=True, null=True)
	t13_cod_indexador = models.CharField('INDEXADOR', db_column='T13_INDEXADOR',max_length=20, blank=True, null=True)
	t13_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T13_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t13_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T13_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t13_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T13_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t13_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T13_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t13_data']
		verbose_name_plural = '13. Tabela c.m. benef. TR mar2015'



class T14TabelaDCP(models.Model):
	t14_data = models.DateTimeField('DATA', db_column='T14_DATA', blank=True, null=True)
	t14_cod_indexador = models.CharField('INDEXADOR', db_column='T14_INDEXADOR',max_length=20, blank=True, null=True)
	t14_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T14_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t14_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T14_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t14_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T14_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t14_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T14_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t14_data']
		verbose_name_plural = '14. Trabalhista TR jul2009'



class T15TabelaDCP(models.Model):
	t15_data = models.DateTimeField('DATA', db_column='T15_DATA', blank=True, null=True)
	t15_cod_indexador = models.CharField('INDEXADOR', db_column='T15_INDEXADOR',max_length=20, blank=True, null=True)
	t15_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T15_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t15_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T15_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t15_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T15_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t15_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T15_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t15_data']
		verbose_name_plural = '15. Trabalhista IPCA-e abr2015 a nov2017'


class T16TabelaDCP(models.Model):
	t16_data = models.DateTimeField('DATA', db_column='T16_DATA', blank=True, null=True)
	t16_cod_indexador = models.CharField('INDEXADOR', db_column='T16_INDEXADOR',max_length=20, blank=True, null=True)
	t16_meta_selic = models.DecimalField('META SELIC COPOM', db_column='T16_META_SELIC', max_digits=18, decimal_places=10, blank=True, null=True)
	t16_taxa_mensal = models.DecimalField('TAXA MENSAL', db_column='T16_TAXA_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
		
	class Meta:
		ordering = ['t16_data']
		verbose_name_plural = '16. Juros Poupança'



class T17TabelaDCP(models.Model):
	t17_data = models.DateTimeField('DATA', db_column='T17_DATA', blank=True, null=True)
	t17_cod_indexador = models.CharField('INDEXADOR', db_column='T17_INDEXADOR',max_length=20, blank=True, null=True)
	t17_x1 = models.DecimalField('X1', db_column='T17_X1', max_digits=18, decimal_places=10, blank=True, null=True)
	t17_x2 = models.DecimalField('X2', db_column='T17_X2', max_digits=18, decimal_places=10, blank=True, null=True)
	t17_x3 = models.DecimalField('X3', db_column='T17_X3', max_digits=18, decimal_places=10, blank=True, null=True)
	t17_x4 = models.DecimalField('X4', db_column='T17_X4', max_digits=18, decimal_places=10, blank=True, null=True)
	t17_x5 = models.DecimalField('X5', db_column='T17_X5', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t17_data']
		verbose_name_plural = '17. Juros 0,5% \\até jun2009'



class T18TabelaDCP(models.Model):
	t18_data = models.DateTimeField('DATA', db_column='T17_DATA', blank=True, null=True)
	t18_cod_indexador = models.CharField('INDEXADOR', db_column='T17_INDEXADOR',max_length=20, blank=True, null=True)
	t18_x1 = models.DecimalField('X1', db_column='T18_X1', max_digits=18, decimal_places=10, blank=True, null=True)
	t18_x2 = models.DecimalField('X2', db_column='T18_X2', max_digits=18, decimal_places=10, blank=True, null=True)
	t18_x3 = models.DecimalField('X3', db_column='T18_X3', max_digits=18, decimal_places=10, blank=True, null=True)
	t18_x4 = models.DecimalField('X4', db_column='T18_X4', max_digits=18, decimal_places=10, blank=True, null=True)
	t18_x5 = models.DecimalField('X5', db_column='T18_X5', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t18_data']
		verbose_name_plural = '18. Juros 1% \\até jul2001'



class T19TabelaDCP(models.Model):
	t19_data = models.DateTimeField('DATA', db_column='T19_DATA', blank=True, null=True)
	t19_cod_indexador = models.CharField('INDEXADOR', db_column='T19_INDEXADOR',max_length=20, blank=True, null=True)
	t19_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T19_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t19_data']
		verbose_name_plural = '19. Média SELIC parcelamento'



class T20TabelaDCP(models.Model):
	t20_ord = models.IntegerField('ORD', db_column='T20_ORDEM',blank=True, null=True) 	
	t20_vigencia = models.CharField('VIGÊNCIA', db_column='T20_VIGENCIA',max_length=30, blank=True, null=True)
	t20_moeda = models.CharField('MOEDA', db_column='T20_MOEDA',max_length=30, blank=True, null=True)
	t20_alteracao = models.CharField('ALTERAÇÃO', db_column='T20_ALTERACAO',max_length=250, blank=True, null=True)
	t20_legislacao = models.CharField('LEGISLAÇÃO', db_column='T20_LEGISLACAO',max_length=250, blank=True, null=True)
	
	class Meta:
		ordering = ['t20_ord']
		verbose_name_plural = '20. Série histórica das moedas'



class T21TabelaDCP(models.Model):
	t21_data = models.DateTimeField('DATA', db_column='T21_DATA', blank=True, null=True)
	t21_cod_indexador = models.CharField('INDEXADOR', db_column='T21_INDEXADOR',max_length=20, blank=True, null=True)
	t21_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T21_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t21_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T21_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t21_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T21_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t21_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T21_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t21_data']
		verbose_name_plural = '21. Tabela c.m. IPCA-e EC 113-2021'



class T22TabelaDCP(models.Model):
	t22_data = models.DateTimeField('DATA', db_column='T22_DATA', blank=True, null=True)
	t22_cod_indexador = models.CharField('INDEXADOR', db_column='T22_INDEXADOR',max_length=20, blank=True, null=True)
	t22_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T22_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t22_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T22_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t22_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T22_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t22_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T22_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t22_data']
		verbose_name_plural = '22. Tabela c.m. INPC'



class T23TabelaDCP(models.Model):
	t23_data = models.DateTimeField('DATA', db_column='T23_DATA', blank=True, null=True)
	t23_cod_indexador = models.CharField('INDEXADOR', db_column='T23_INDEXADOR',max_length=20, blank=True, null=True)
	t23_var_per_mensal = models.DecimalField('VAR PERC MENSAL', db_column='T23_VAR_PER_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t23_num_indice_var_mensal = models.DecimalField('NUM ÍNDICE VAR MENSAL', db_column='T23_NUM_INDICE_VAR_MENSAL', max_digits=18, decimal_places=10, blank=True, null=True)
	t23_fator_vigente = models.DecimalField('FATOR VIGENTE', db_column='T23_FATOR_VIGENTE', max_digits=18, decimal_places=10, blank=True, null=True)
	t23_indice_correcao = models.DecimalField('INDICE CORREÇÃO', db_column='T23_INDICE_CORRECAO', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t23_data']
		verbose_name_plural = '23. Tabela c.m. INPC + IPCA-E'



class T24TabelaDCP(models.Model):
	t24_data = models.DateTimeField('DATA', db_column='T24_DATA', blank=True, null=True)
	t24_cod_indexador = models.CharField('INDEXADOR', db_column='T24_INDEXADOR',max_length=20, blank=True, null=True)
	t24_fator_ipcae = models.DecimalField('FATOR IPCA-E', db_column='T24_FATOR_IPCAE', max_digits=18, decimal_places=10, blank=True, null=True)
	t24_fator_tr = models.DecimalField('FATOR TR', db_column='T24_FATOR_TR', max_digits=18, decimal_places=10, blank=True, null=True)
	t24_juros = models.DecimalField('JUROS', db_column='T24_JUROS', max_digits=18, decimal_places=10, blank=True, null=True)
	
	class Meta:
		ordering = ['t24_data']
		verbose_name_plural = '24. Tabela WebGCALC'



class T21ListaTabelasDCP(models.Model):
	t21_cod_tabela = models.IntegerField('CÓDIGO', db_column='T21_CODIGO', blank=True, null=True)
	t21_nome_tabela = models.CharField('NOME DA TABELA', db_column='T21_NOME_TABELA', max_length=50, blank=True, null=True)
	t21_obs_tabela = models.CharField('OBSERVAÇÕES', db_column='T21_OBS_TABELA', max_length=1000, blank=True, null=True)
	t21_indexador = models.CharField('INDEXADOR', db_column='T21_INDEXADOR',max_length=30, blank=True, null=True)

	class Meta:
		ordering = ['t21_cod_tabela']
		verbose_name = 'Tabelas-DCP'
		verbose_name_plural = 'Tabelas-DCP'
	
	def __str__ (self):
		return str(self.t21_cod_tabela) + '-' + self.t21_nome_tabela + "-" + str(self.t21_obs_tabela)


class t22IndexadoresDCP(models.Model):
	t03_cod_indexador = models.CharField(db_column='T22_CODIGO',max_length=20, blank=True, null=True)
	t03_nome_indexador = models.CharField(db_column='T22_NOME_INDEXADOR', max_length=50, blank=True, null=True)
	t03_descricao = models.CharField(db_column='T22_DESCRICAO', max_length=70, blank=True, null=True)


class CargoEmprego(models.Model):
	codcargo = models.CharField('Código',max_length=10)
	codgrupocargo = models.CharField('Grupo', max_length=10)
	nomecargo = models.CharField('Nome', max_length=200)
	nivel = models.CharField('Nível', max_length=10)

	class Meta:
		verbose_name = 'Cargo-Emprego'
		verbose_name_plural = 'Cargo-Emprego'

	def __str__ (self):
		return self.nomecargo + ' - ' + str(self.nivel)

class OrgaoSiape(models.Model):
	codigo = models.CharField('Código', max_length=10)
	nome = models.CharField('Nome', max_length=200)

	class Meta:
		verbose_name = 'Órgão Siape'
		verbose_name_plural = 'Órgão Siape'

	def __str__ (self):
		return self.nome


class Rubricas(models.Model):
	codigorubrica = models.CharField('Código', max_length=10)
	nomerubrica = models.CharField('Rubrica', max_length=200)

	class Meta:
		verbose_name = 'Rubrica'
		verbose_name_plural = 'Rubricas'

	def __str__ (self):
		return self.nomerubrica
	

class List (models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)


	def __str__ (self):
		return self.item + ' ' + str(self.completed)



class GratValorPonto(models.Model):
	nomegrat = models.CharField('Gratificação', max_length=10, choices=NOME_GRATIFICACAO)
	datainicio = models.CharField('Data de início',max_length=10)
	datafinal = models.CharField('Data final', max_length=10)
	nivel = models.CharField('Nível',max_length=3)
	classe = models.CharField('Classe', max_length=1)
	padrao = models.CharField('Padrão', max_length=1)
	valorponto = models.DecimalField('Valor do ponto', decimal_places=2, max_digits=8)

	class Meta:
		verbose_name = 'Valor do Ponto'
		verbose_name_plural = 'Valor do Ponto'



class GratPontuacao(models.Model):
	nomegrat = models.CharField('Gratificação', max_length=10, choices=NOME_GRATIFICACAO)
	pontuacao = models.DecimalField('Pontuação',decimal_places=2,max_digits=5)
	datainicio = models.CharField('Data de início',max_length=10)
	datafinal = models.CharField('Data final', max_length=10)

	class Meta:
		verbose_name = 'Pontuação'
		verbose_name_plural = 'Pontuação'
	


