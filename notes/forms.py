from django import forms
from .models import Note

class AddNotes(forms.ModelForm):
    class Meta:
        model=Note
        fields = '__all__'
        exclude = ['user',]