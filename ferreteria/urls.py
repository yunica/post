from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # productos
    url(r'^', include('medicamentos.urls', namespace="medicamentos_app")),

    # agregar ventas.
    url(r'^ventas/', include('ventas.urls', namespace="ventas_app")),

    # login-users
    url(r'^', include('users.urls', namespace='users_app')),

    # CLientes
    url(r'^', include('clientes.urls', namespace='clientes_app')),

    url(r'^', include('distribuidor.urls', namespace='distribuidores_app')),

    # compras
    url(r'^', include('compras.urls', namespace='compras_app')),
    # compras
    url(r'^', include('laboratorio.urls', namespace='laboratorios_app')),

    url(r'^todolist/', include('inline.urls', namespace='todolist')),

    # factura
    url(r'^', include('factura.urls', namespace='factura_app')),

]
