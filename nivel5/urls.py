from django.urls import path
from . import views


urlpatterns = [
    path('nivel5/', views.Nivel5CreateListView.as_view(), name='nivel5-create-list'),
    path('nivel5/<int:pk>/', views.Nivel5RetrieveUpdateDestroyView.as_view(), name='nivel5-detail-view'),
]
