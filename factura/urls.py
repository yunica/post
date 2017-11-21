from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'factura/lista_ventas/$', views.ListaVentas.as_view(), name='lista_ventas'),
    url(r'^factura/venta$', views.facturaCrear, name="factura_venta"),
    url(r'^factura/buscar_cliente$', views.buscarCliente),
    url(r'^factura/buscar_producto$', views.buscarProducto),
    url(r'^factura/consultar$', views.consultarFactura, name="consultar_factura"),
    #url(r'factura/generar_reporte_factura/$', views.generar_pdf, name='generar_reporte_factura'),
    url(r'factura/reporte_ventas/(?P<pk>\d+)/$', views.reporteventas, name='reporte_ventas'),
]
