from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "Hello I'm from Fourth App"}
    return render(request, 'fourth_app/index.html', context=my_dict)
