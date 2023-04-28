from django.forms import ModelForm
from .models import Lezione

class LezioneForm(ModelForm):

    class Meta:
        model = Lezione
        fields = '__all__'
