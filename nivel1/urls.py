from django.urls import path
from . import views


urlpatterns = [
    path('nivel1/', views.Nivel1CreateListView.as_view(), name='nivel1-create-list'),
    path('nivel1/<int:pk>/', views.Nivel1RetrieveUpdateDestroyView.as_view(), name='nivel1-detail-view'),
]
