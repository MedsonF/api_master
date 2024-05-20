from django.urls import path
from . import views


urlpatterns = [
    path('nivel2/', views.Nivel2CreateListView.as_view(), name='nivel2-create-list'),
    path('nivel2/<int:pk>/', views.Nivel2RetrieveUpdateDestroyView.as_view(), name='nivel2-detail-view'),
]
