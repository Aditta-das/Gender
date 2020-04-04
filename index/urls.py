from django.urls import path
from . import views
from .views import AuthorProfileView, index, ProfileView, include

urlpatterns = [
    path('', include, name='include'),
    path('index/', views.index, name='index'),
    path('author/', AuthorProfileView.as_view(), name='author'),
    path('profile/<user>', ProfileView.as_view(), name='profile'),
]
