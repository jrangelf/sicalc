from django.contrib import admin
from django.urls import path, include
from sicalc import views

admin.site.site_header = 'SICALC - Painel de Administração'
admin.site.site_title = 'Painel'

urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include ('sicalc.urls')),
]

