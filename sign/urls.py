from django.urls import path

from .views import ProfileDetailView, ProfileUpdateView


urlpatterns = [
    path('<slug:slug>/', ProfileDetailView.as_view(), name='profile'),
    path('<slug:slug>/update/', ProfileUpdateView.as_view(), name='profile_update'),
]
