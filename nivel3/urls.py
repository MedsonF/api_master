from django.urls import path
from . import views


urlpatterns = [
    path('nivel3/', views.Nivel3CreateListView.as_view(), name='nivel3-create-list'),
    path('nivel3/<int:pk>/', views.Nivel3RetrieveUpdateDestroyView.as_view(), name='nivel3-detail-view'),
]
