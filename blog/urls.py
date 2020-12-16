from django.urls import path
from .views import HomePageView, DetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/', DetailView.as_view(), name='post_detail')
]