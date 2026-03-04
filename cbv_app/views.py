from django.shortcuts import render
from.models import school
from django.views.generic import (ListView,CreateView,UpdateView,DetailView,DeleteView,)

# Create your views here.
class create_view(CreateView):
    model=school
    fields='__all__'
    template_name='school/school_form.html'
    success_url = 'form'

