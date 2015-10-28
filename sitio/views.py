from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count

from datos.models import *

# Create your views here.
class Home(ListView):
    model = Politico

    def get_queryset(self):
    	return Politico.objects.all().annotate(total=Count('evento')).order_by('-total')