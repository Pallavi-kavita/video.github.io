from . import views
from django.urls import path

urlpatterns = [
    path('',views.video, name = 'video'),
   # path('login/',),
    path('register/',views.register, name = 'register_url'),
    #path('logout/',),
]