from django.urls import path
from . import views
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout_view,name="logout"),
    path('login/',views.login_view,name="login"),
    
]