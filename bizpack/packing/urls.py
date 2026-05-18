from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:pk>/toggle/', views.toggle_item, name='toggle_item'),
    path('item/<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('trip/<int:trip_pk>/add/', views.add_item, name='add_item'),
]
