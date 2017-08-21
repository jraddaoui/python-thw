# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
    context = {'hello': "Hello, world. You're at the ex50 index."}
    return render(request, 'ex50/index.html', context)
