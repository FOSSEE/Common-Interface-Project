from django.shortcuts import render
from django.http import JsonResponse
import requests

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            r = requests.post('http://127.0.0.1:8000/api/set_block_parameters/', data=form.cleaned_data)
            json = r.json()
            print(json)
            # redirect to a new URL:
            return render(request, 'frontend/name2.html', {'json': json})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'frontend/name.html', {'form': form})
