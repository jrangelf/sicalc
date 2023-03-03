from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('uncross/<list_id>', views.uncross, name='uncross'),
    path('extrator/', views.extrator, name='extrator'),
    path('extrator-lista/', views.extratorlista, name='extrator-lista'),
    path('lista/', views.lista, name='lista'),
    path('obitos/', views.obitos, name='obitos'),
    path('obitos-lista/', views.obitoslista, name='obitos-lista'),
    path('gratificacoes/', views.gratificacoes, name='gratificacoes'),
    path('especificos/', views.especificos, name='especificos'),
    path('customizados/', views.customizados, name='customizados'),
    path('tabelasdcp/', views.tabelasdcp, name='tabelasdcp'),
    path('tabelasdcp-lista/', views.tabelasdcp, name='tabelasdcp-lista'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('upload_home/', views.upload_file, name='upload_home'),
    path('upload/',views.upload_file,name='upload'),
    path('testnav/', views.teste, name='teste'),
]