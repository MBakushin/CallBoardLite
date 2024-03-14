from django.urls import path, include

from .views import AnnounceListView, AnnounceCreateView, AnnounceDetailView, \
    AnnounceUpdateView, AnnounceDeleteView, CategoryListView, CategoryDetailView,\
    RespondCreateView


urlpatterns = [
    path('announce/', AnnounceListView.as_view(), name='home'),
    path('announce/create/', AnnounceCreateView.as_view(), name='create_announce'),
    path('announce/<slug:slug>/', AnnounceDetailView.as_view(), name='announce_detail'),
    path('announce/<int:pk>/respond/create/', RespondCreateView.as_view(), name='respond_create'),
    path('announce/<slug:slug>/update/', AnnounceUpdateView.as_view(), name='update_announce'),
    path('announce/<slug:slug>/delete/', AnnounceDeleteView.as_view(), name='delete_announce'),
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('announce/<int:pk>/respond/create/', RespondCreateView.as_view(), name='create_respond'),
]
