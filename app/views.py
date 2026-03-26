from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from django.shortcuts import redirect
from app.models import Jamoa, Kurs, Ariza


class IndexView(ListView):
    model = Jamoa
    template_name = 'index.html'
    context_object_name = 'jamoas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Kurs.objects.all()
        return context

class ArizaView(FormView):
    form_class = Ariza
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

