from django.shortcuts import render

def homepage(request):
    nickname = '點兒'
    name = 'Lisa Chen'
    birthday = '850926'
    cellphone = '0958092685'
    return render(request, 'double_seven/homepage.html', {'nickname':nickname})
# Create your views here.
