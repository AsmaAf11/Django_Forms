from django import forms
from .models import Project


class ExampleForm(forms.Form):
    text_input = forms.CharField(max_length=10)
    password_input = forms.CharField(widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()


class project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
