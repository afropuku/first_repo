from django.urls import path
from . import views


app_nam = 'cart'

urlpatterns = [
    path('cart/<int:pk>', views.CartDetailView.as_view(), name='detail'),
]
