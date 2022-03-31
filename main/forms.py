from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Session number", max_length=200)
