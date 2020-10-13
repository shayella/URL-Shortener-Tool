from django.urls import path
from .views import shortenurl_redirect_view,home

urlpatterns = [
    path('',home, name='home' ),
    path('<slug:shortcode>/', shortenurl_redirect_view,name='shortenurl'),
]
