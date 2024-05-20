from django.urls import path
from . import views


urlpatterns = [
    path('plano_financeiro/', views.PlanoFinanceiroCreateListView.as_view(), name='plano_financeiro-create-list'),
    path('plano_financeiro/<int:pk>/', views.PlanoFinanceiroRetrieveUpdateDestroyView.as_view(), name='plano_financeiro-detail-view'),
]
