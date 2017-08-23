from django.conf.urls import url
from django.contrib.auth.views import (login, logout, logout_then_login,
                                       password_change, password_change_done, password_reset,
                                       password_reset_done, password_reset_confirm, password_reset_complete)

from .views import RegisterView

urlpatterns = [

    # Authentication
    # ==============
    url(r'^login/$',
        login,
        name='login'
    ),

    url(r'^logout/$',
        logout,
        name='logout'
    ),

    url(r'^logout-then-login/$',
        logout_then_login,
        name='logout_then_login'
    ),

    url(r'^register/$',
        RegisterView,
        name='register'
    ),


    # Password Change
    # ===============
    url(r'^password-change/$',
        password_change,
        {'post_change_redirect': 'accounts:password_change_done'},
        name='password_change'
    ),

    url(r'^password-change/done/$',
        password_change_done,
        name='password_change_done'
    ),


    # Password Reset
    # ==============
    url(r'^password-reset/$',
        password_reset,
        {'post_reset_redirect': 'accounts:password_reset_done'},
        name='password_reset'
    ),

    url(r'^password-reset/done/$',
        password_reset_done,
        name='password_reset_done'
    ),

    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm,
        {'post_reset_redirect': 'accounts:password_reset_complete'},
        name='password_reset_confirm'
    ),

    url(r'^password-reset/complete/$',
        password_reset_complete,
        name='password_reset_complete'
    ),

]
