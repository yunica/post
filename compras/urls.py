from django.conf.urls import url
from .views import ListaCompras, realizar_compra, reportecompras  # , generar_reporte_lista_compras
from django.views.generic import TemplateView

urlpatterns = [
    url(r'compras/realizar_compra/$', realizar_compra, name="realizar_compra"),
    url(r'compras/confirmacion_compra$', TemplateView.as_view(template_name="compras/confirmacion_compra.html")),
    url(r'compras/lista_compras/$', ListaCompras.as_view(), name='lista_compras'),
    url(r'compras/reporte_compras/(?P<pk>\d+)/$', reportecompras, name='reporte_compras'),
    # url(r'compras/generar_reporte_lista_compras/$', generar_reporte_lista_compras,
    #    name='generar_reporte_lista_compras'),
]
