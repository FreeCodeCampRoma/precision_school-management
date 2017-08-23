from django.conf.urls import url
from django.contrib.auth.views import (login, logout, logout_then_login,
                                       password_change, password_change_done, password_reset,
                                       password_reset_done, password_reset_confirm, password_reset_complete)

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


    # Password Change
    # ===============
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


    # Password Reset
    # ==============
    url(
        regex=r'^password-reset/$',
        view=password_reset,
        name='password_reset',
    ),

    url(
        regex=r'^password-reset/done/$',
        view=password_reset_done,
        name='password_reset_done'
    ),

    url(
        regex=r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        view=password_reset_confirm,
        name='password_reset_confirm'
    ),

    url(
        regex=r'^password-reset/complete/$',
        view=password_reset_complete,
        name='password_reset_complete'
    ),

]
