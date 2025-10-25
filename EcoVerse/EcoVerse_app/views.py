from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def registration(request):
    return render(request, 'registration.html')


def signin(request):
    return render(request, 'signin.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def settings(request):
    return render(request, 'settings.html')


def rewards(request):
    return render(request, 'rewards.html')


def impact(request):
    return render(request, 'impact.html')


def analytics(request):
    return render(request, 'analytics.html')