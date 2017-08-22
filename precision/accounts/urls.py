from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login, 
from .views import SignInView


urlpatterns = [

    # Authentication
    # ==============
    url(
        regex=r'^login/$',
        view=login,
        name='login'
    ),

    url(
        regex=r'^logout/$',
        view=logout,
        name='logout'
    ),

    url(
        regex=r'^logout-then-login/$',
        view=logout_then_login,
        name='logout_then_login'
    ),
]
