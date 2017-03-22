from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^locacaoveiculos/$', views.login_now, name='login_now'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
]