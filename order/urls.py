from django.conf.urls import url
from . import views

app_name = 'order'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'comanda_plasata/', views.comanda_plasata, name='comanda_plasata'),
]