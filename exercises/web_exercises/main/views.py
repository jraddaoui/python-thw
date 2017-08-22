# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
    context = {
        'exercises': [
            ('ex50:index', 'Exercise 50')
        ]
    }
    return render(request, 'main/index.html', context)
