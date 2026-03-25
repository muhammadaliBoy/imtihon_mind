from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView

from app.models import Jamoa, Kurs


class IndexView(ListView):
    model = Jamoa
    template_name = 'index.html'
    context_object_name = 'jamoas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Kurs.objects.all()
        return context
