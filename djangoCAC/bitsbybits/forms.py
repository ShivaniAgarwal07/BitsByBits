from django import forms
from .models import BitsByBits

class BitsByBitsForm(forms.ModelForm):
    class Mets:
        model = BitsByBits
        fields = ['text', 'photo']