from django.urls import path
import accounts.views as views

urlpatterns = [
    path('register/', views.register, name='register'),
]