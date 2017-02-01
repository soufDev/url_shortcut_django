from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponse, Http404
from django.views.generic.edit import DeleteView

from url_shortcut.models import MiniURL
from .forms import URlForm

import random
import string

from django.views.generic import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.


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


class URLCreate(CreateView):
    model = MiniURL
    template_name = 'url_shortcut/add_url.html'
    form_class = URlForm
    success_url = reverse_lazy('all_urls')


class URLUpdate(UpdateView):
    model = MiniURL
    template_name = 'url_shortcut/add_url.html'
    form_class = URlForm
    success_url = reverse_lazy('add_url')

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniURL, url_code=code)

    def form_valid(self, form):
        self.object = form.save()
        # send a message to the user
        messages.success(self.request, "Your Profil has been updated with success")
        return HttpResponseRedirect(self.get_success_url())


class URLDelete(DeleteView):
    model = MiniURL
    context_object_name = 'url_shortcut'
    template_name = 'url_shortcut/delete.html'
    success_url = reverse_lazy('all_urls')

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniURL, url_code=code)
