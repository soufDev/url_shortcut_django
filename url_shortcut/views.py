from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponse, Http404

from url_shortcut.models import MiniURL
from .forms import URlForm

import random
import string
# Create your views here.


# function to generate the code for the URL
def generate(char_number):
    chars = string.ascii_letters + string.digits
    url_code = [random.choice(chars) for _ in range(char_number)]
    return ''.join(url_code)


# show all the urls sorted by the access number
def view_all(request):
    mini_urls = MiniURL.objects.order_by('access_number').all()
    return render(request, 'url_shortcut/urls.html', {'urls': mini_urls})


# return a home page
def view_home(request):
    title = "Welcome Every one"
    welcome_msg = "Hello On the Shortcut URLs App"
    return render(
        request,
        'url_shortcut/home.html',
        {
            'title': title,
            'message': welcome_msg
         }
    )


# add new shortcut url
def view_add_url(request):
    saving = False
    form = URlForm(request.POST or None)
    if form.is_valid():
        url = MiniURL()
        url.default_url = form.cleaned_data["url_form"]
        url.identifier_create = form.cleaned_data["identifier_form"]
        url.url_code = generate(8)
    return render(
        request,
        'url_shortcut/add_url.html',
        {
            'form': form,
            'saving': saving
        }
    )