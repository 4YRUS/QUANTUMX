
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('crypto/',views.crypto,name='crypto'),
    path('exchange/',views.exchange,name='exchange'),
    path('getresponse/',views.get_response,name='response'),
    path('mutual/',views.mutual,name='mutual'),
    path('mutualfund/<str:symbol>',views.mutualfund,name='mutualfund'),
    path('stock/<str:symbol>',views.stock,name='stock'),
    
]
