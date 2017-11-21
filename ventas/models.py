from django.db import models
from medicamentos.models import Medicamentos
from clientes.models import Cliente
from django.db.models import signals
from compras.models import TimeStampModel


class Cabecera_Venta(TimeStampModel):
    ruc = models.CharField(max_length=10, unique=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.ruc


class todo_item(models.Model):
    list_id = models.ForeignKey(Cabecera_Venta)
    medicamento = models.ForeignKey(Medicamentos)
    cantidad = models.IntegerField()


def update_stock(sender, instance, **kwargs):
    instance.medicamento.stock -= instance.cantidad
    instance.medicamento.save()


# register the signal
signals.post_save.connect(update_stock, sender=todo_item, dispatch_uid="update_stock_count")
