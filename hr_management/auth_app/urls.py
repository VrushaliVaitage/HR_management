from django.urls import path
from . import views


urlpatterns   = [
    path('spv/', views.signup_view, name='signup_url'),
    path('lig/', views.login_view, name='signin_url'),
    path('log/', views.logout_view, name='signout_url'),

]