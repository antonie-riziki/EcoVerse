from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('registration', views.registration, name="registration"),
    path('signin', views.signin, name="signin"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('settings', views.settings, name="settings"),
    path('analytics', views.analytics, name="analytics"),
    path('impact', views.impact, name="impact"),
    path('rewards', views.rewards, name="reward"),

]