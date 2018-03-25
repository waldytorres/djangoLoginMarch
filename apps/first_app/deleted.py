from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
import bcrypt

def index(request):
    return render(request, 'first_app/loginreg.html')


def process(request):
    hash1 = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
    print hash1
    registable.objects.create(firstname=request.POST["firstname"], lastname=request.POST["lastname"], email=request.POST["email"], password=request.POST["password"])
    return redirect('/wall')
	

def wall(request):
    return render(request, 'first_app/wall.html')