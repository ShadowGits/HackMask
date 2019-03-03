
from django.urls import path
from .import views

urlpatterns = [
    path('',views.contact),
    path('parse/',views.parseUrl, name='parse'),
]
