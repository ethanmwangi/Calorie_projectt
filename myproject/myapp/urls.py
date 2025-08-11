from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]