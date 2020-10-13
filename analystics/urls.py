from django.urls import path
from . import views
urlpatterns = [
    path('',views.url_count,name='url_count'),
    path('<slug:shortcode>/',views.url_count,name='url_count')
]
