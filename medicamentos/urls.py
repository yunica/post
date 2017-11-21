from django.conf.urls import url
from .views import ListaMedicamentos, DetalleView, ActualizarView, CreateMedicamentos, EliminarView, CreatePresentacion

urlpatterns = [url(r'^medicamentos/$', ListaMedicamentos.as_view(), name='lista_medicamentos'),
               url(r'^medicamentos/detalle/(?P<pk>\d+)/$', DetalleView.as_view(), name='detalle_medicamentos'),
               url(r'^medicamentos/actualizar/(?P<pk>\d+)/$', ActualizarView.as_view(), name="actualizar_medicamentos"),
               url(r'^medicamentos/agregar$', CreateMedicamentos.as_view(), name='create_medicamentos'),
               url(r'^medicamentos/eliminar/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_medicamentos"),
               # exportar a excel
               # url(r'^expatenciones/$', 'apps.medicamentos.views.CargaAtenciones_ant',name='xds'),
               # url(r'^medicamentos/reporte/$', generar_reporte_medicamentos, name='reporte'),
               # presentacion
               url(r'^medicamentos/presentacion$', CreatePresentacion.as_view(), name='create_presentacion'),
               ]
