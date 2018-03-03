from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query_utils import Q
from django_tables2 import RequestConfig
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .tables import CorrespondenciaTable
from .filters import CorrespondenciaListFilter
from .utils import PagedFilteredTableView
from .models import correspondencia
from .forms import CorrespondenciaListFormHelper

def index(request):

	if request.user.is_authenticated:
		return render(request, "scc/ingreso.html", {})
	else:
		return render(request,"scc/login.html",{})

@login_required(login_url='')
def ingreso(request):

	user = request.user
	return render(request,"scc/ingreso.html",{'user':user,'user_name':user.first_name +  ' ' + user.last_name})


@login_required
def busqueda(request):
	user = request.user
	_documents = ['Hi']
	return render(request,"scc/busqueda.html",{'user':user,'user_name':user.first_name +  ' ' + user.last_name, 'documents': _documents})


@login_required
def enlace(request):
	user = request.user
	return render(request,"scc/enlace.html",{'user':user,'user_name':user.first_name +  ' ' + user.last_name})


@login_required
def reportes(request):
	user = request.user
	return render(request,"scc/reportes.html",{'user':user,'user_name':user.first_name +  ' ' + user.last_name})


class CorrespondenciaListView(LoginRequiredMixin, GroupRequiredMixin, PagedFilteredTableView):
	model = correspondencia
	template_name = 'scc/testbusqueda.html'
	context_object_name = 'correspondencia'
	ordering = ['-codigo']
	group_required = u'company-user'
	table_class = CorrespondenciaTable
	filter_class = CorrespondenciaListFilter
	formhelper_class = CorrespondenciaListFormHelper

	def get_queryset(self):
		qs = super(CorrespondenciaListView, self).get_queryset()
		return qs

	def post(self, request, *args, **kwargs):
		return PagedFilteredTableView.as_view()(request)

	def get_context_data(self, **kwargs):
		context = super(CorrespondenciaListView, self).get_context_data(**kwargs)
		context['nav_correspondencia'] = True
		search_query = self.get_queryset()
		table = CorrespondenciaTable(search_query)
		RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
		context['table'] = table

		return context