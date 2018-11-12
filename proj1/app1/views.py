# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Product

# Create your views here.
def fun(a):
	products=[product.name+"," for product in Product.objects.all()]
	return HttpResponse(products)
