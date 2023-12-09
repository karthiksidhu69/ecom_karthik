from django.urls import path
from app.views import homepage,login,registration
app_name='app'
urlpatterns = [
    path('',login,name='login'),
    path('reg/',registration,name='registration'),
    path('home/',homepage,name='homepage')
    path('otp/<str:otp>/<str:password>/<str:email>/',otp,name='otp')
]
