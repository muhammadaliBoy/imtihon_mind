from django.forms import ModelForm
from app.models import Ariza


class ContactForm(ModelForm):
    class Meta:
        model = Ariza
        fields = '__all__'