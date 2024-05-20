from django.urls import path
from . import views


urlpatterns = [
    path('nivel4/', views.Nivel4CreateListView.as_view(), name='nivel4-create-list'),
    path('nivel4/<int:pk>/', views.Nivel4RetrieveUpdateDestroyView.as_view(), name='nivel4-detail-view'),
]
