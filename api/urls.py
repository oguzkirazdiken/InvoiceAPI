from django.urls import path, re_path
from api import views

urlpatterns = [
    path('api/invoiceCreate/', views.invoice_create, name='invoice_create'),
    path('api/contactCreate/', views.contact_create, name='contact_create'),
    path('api/contactUpdate/<str:pk>/', views.contact_update, name='contact_update'),
    path('api/contactSuggest/', views.contact_suggest, name='contact_suggest'),
]
