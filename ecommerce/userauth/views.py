from django.shortcuts import render

# Create your views here.

def signup(request):
    context = {
        'email':'email'
    }
    return render(request, 'userauth\signup.html', context)
