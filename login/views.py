from django.shortcuts import render

# Create your views here.


def login(request):
    print('login')
    return render(request,'login.html')