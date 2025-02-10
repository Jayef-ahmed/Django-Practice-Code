from django import forms
from .models import Albums

class album_forms(forms.ModelForm):
    class Meta:
        model = Albums
        fields = "__all__"