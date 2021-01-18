from django.urls import path
from .views import(
  ImageListView,
  ImageUpdateView,
  ImageDetailView,
  ImageDeleteView,
  ImageCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', ImageUpdateView.as_view(), name='image_edit'),
    path('<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('<int:pk>/delete/', ImageDeleteView.as_view(), name='image_delete'),
    path('image_create/', ImageCreateView.as_view(), name='image_create'),
    path('', ImageListView.as_view(), name='image_list'),
]
