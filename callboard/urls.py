from django.urls import path, include

from .views import home_page, AnnounceCreateView


urlpatterns = [
    path('', home_page, name='home'),
    path('create/', AnnounceCreateView.as_view(), name='create'),
]
