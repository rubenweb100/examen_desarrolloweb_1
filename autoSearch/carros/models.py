# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings


class car (models.Model):
    marca = models.CharField(max_length=140)
    text = models.TextField()
    modelos=models.CharField(max_length=140)
    color=models.CharField(max_length=150)
    precio=models.DecimalField(max_digits=10, decimal_places = 2)

    def __str__(self):
        return str (self.marca)
