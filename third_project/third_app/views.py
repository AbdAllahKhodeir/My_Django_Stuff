from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello I am from third_app/index.html!"}
    return render(request, 'third_app/index.html', context=my_dict)

def help(request):
    help_dict = {'help_insert': 'HELP PAGE'}
    return render(request, 'third_app/help.html', context=help_dict)
