# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    context = {'hello': 'Hello', 'name': 'Nobody', 'error_message': None}

    if request.method == 'POST':
        try:
            hello = request.POST['hello']
            name = request.POST['name']
            context['hello'] = hello
            context['name'] = name
        except KeyError:
            context['error_message'] = 'Hello and name are required'

    return render(request, 'ex51/index.html', context)
