from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('ask/', views.ask ,name='ask'),
    path('ask/', views.ask ,name='form')
]
