from django import forms
from .models import Lezione

class LezioneForm(forms.ModelForm):

    class Meta:
        model = Lezione
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 
                    'type': 'date'
                    }),
            'ora_inizio': forms.TimeInput(
                attrs={'class': 'form-control', 
                    'type': 'time'
                    }),
            'tipologia': forms.RadioSelect
        }
