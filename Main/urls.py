from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^arbitra_see$', views.arbitra_see, name='arbitra_see'),
    url(r'^arbitra_altera$', views.arbitra_altera, name='arbitra_altera'),
    url(r'^arbitra_remove$', views.arbitra_remove, name='arbitra_remove'),
    url(r'^partida$', views.partida, name='partida'),
    url(r'^', views.index, name='index'),
    url(r'^pdf2go',views.pdf2go, name='pdf2go')
]
