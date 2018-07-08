from django.shortcuts import render

# Create your views here.

def register(request):
    context = {
        'title' : 'Register',
    }
    return render(request, 'register/register.html', context)