from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('market/', views.MarketListView.as_view(), name='market'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/new/', views.ItemCreateView.as_view(), name='item_create'),
    path('item/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_edit'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
]
