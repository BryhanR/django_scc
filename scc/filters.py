# filters.py
import django_filters
from .models import correspondencia


class CorrespondenciaListFilter(django_filters.FilterSet):
    class Meta:
        model = correspondencia
        fields = ['oficio','fecha_recibido','codigo']
        order_by = ['pk']