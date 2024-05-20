from django.urls import path
from . import views


urlpatterns = [
    path('nivel0/', views.Nivel0CreateListView.as_view(), name='nivel0-create-list'),
    path('nivel0/<int:pk>/', views.Nivel0RetrieveUpdateDestroyView.as_view(), name='nivel0-detail-view'),
]
