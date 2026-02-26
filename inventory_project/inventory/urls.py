from django.urls import path
from inventory import views

urlpatterns = [
    path('api/items/', views.items, name='items-list'),
    path('api/items/<int:pk>', views.items_details, name='items-details'),
    path('api/items/export/pdf', views.export_items_pdf, name='export-pdf'),
    path('api/items/export/excel', views.export_items_excel, name='export-excel')
]   
