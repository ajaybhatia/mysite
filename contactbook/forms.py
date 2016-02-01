from django import forms


class MyForm(forms.Form):
	name = forms.CharField(max_length=200)
	email = forms.EmailField()
	age = forms.IntegerField()