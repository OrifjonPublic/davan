from django.urls import path, include
from .views import HomeView, DetailView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<str:x>/', DetailView.as_view(), name='detail'),
]
