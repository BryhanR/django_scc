import django_tables2 as tables
from django_tables2.utils import A
from .models import correspondencia


class CorrespondenciaTable(tables.Table):
    #oficio = tables.LinkColumn('correspondencia-detail', args=[A('pk')])
    #fecha_recibido = tables.LinkColumn('correspondencia-detail', args=[A('pk')])

    class Meta:
        model = correspondencia
        fields = (
            'codigo',
            'fecha Oficio',
            'fecha_Recibido',
            'Asunto',
            'Destinatario',
            'Copia'
            'Remitente',
            'Recibido',
            'Estado',
            'Enlaces',
            'Edicion',
            'Alarma')
        attrs = {"class": "table-striped table-bordered"}

        empty_text = "There are no news matching the search criteria..."