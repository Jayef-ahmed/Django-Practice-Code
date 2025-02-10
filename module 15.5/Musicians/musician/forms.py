from django import forms
from .models import Musician

class musician_forms(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"