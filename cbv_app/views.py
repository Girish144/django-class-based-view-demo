from django.shortcuts import render
from.models import school
from django.views.generic import (ListView,CreateView,UpdateView,DetailView,DeleteView,)
from django.urls import reverse_lazy
# Create your views here.
class create_view(CreateView):
    model=school
    fields='__all__'
    template_name='school/school_form.html'
    success_url = reverse_lazy('create_view')


class list_view(ListView):
    model=school
    template_name='school/school_list.html'
    context_object_name='school_list'

class detail_view(DetailView):
    model=school
    template_name='school/school_detail.html'
    context_object_name='school'

class update_view(UpdateView):
    model=school
    fields='__all__'
    template_name='school/school_update.html'
    context_object_name='form'

class delete_view(DeleteView):
    model=school
    template_name='school/school_delete.html'
    context_object_name='school'