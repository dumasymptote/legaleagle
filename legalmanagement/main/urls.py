from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'main'

urlpatterns=[
    path('', views.HomeView.as_view(), name='index'),
    path('dashboard/', login_required(views.DashboardView.as_view()), name="dashboard" )
]