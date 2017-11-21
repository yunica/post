from django.conf.urls import url
from .views import Home, userlogin, LogOut

urlpatterns = [url(r'^$', userlogin, name="login"),
               url(r'^salir/$', LogOut, name='logout'),
               # principal
               url(r'^home', Home.as_view(), name='home'),
               ]
