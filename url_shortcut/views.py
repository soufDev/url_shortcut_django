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
    form = URlForm(request.POST)
    if request.method == "POST":
        form = URlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(view_all)
        else:
            form = URlForm()
    return render(
        request,
        'url_shortcut/add_url.html',
        {
            'form': form
        }
    )


def redirection(request, code):
    """redirect to the saving url"""
    mini = get_object_or_404(MiniURL, url_code=code)
    mini.access_number += 1
    mini.save()

    return redirect(mini.default_url, permanent=True)
