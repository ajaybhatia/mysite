from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm


def home(request, name):
	a, b = 10, 20

	return render(
		request, 
		'index.html', {
			'name': name,
			'result': a + b
		})

def my_form(request):
	f = MyForm()

	if f.is_valid():
		return HttpResponse("Working");

	return render(request, 'form.html', {'my_form': f})