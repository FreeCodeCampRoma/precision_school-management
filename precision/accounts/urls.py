from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done
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

    # Password Change
    # ===============
    url(
        regex=r'^logout-then-login/$',
        view=logout_then_login,
        name='logout_then_login'
    ),

    url(
        regex=r'^password-change/$',
        view=password_change,
        name='password_change'
    ),

    url(
        regex=r'^password-change/done/$',
        view=password_change_done,
        name='password_change_done'
    ),
]
