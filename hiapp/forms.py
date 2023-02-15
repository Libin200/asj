from django import forms
from hiapp.models import hi

class hiform(forms.ModelForm):
    class Meta:
        model=hi
        fields="__all__"