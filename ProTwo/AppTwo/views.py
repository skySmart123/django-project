from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def help(request):
    my_dict = {'insert_me':"This is help page!"}
    return render(request, 'AppTwo/help.html', context=my_dict)