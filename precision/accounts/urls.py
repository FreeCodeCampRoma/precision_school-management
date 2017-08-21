from django.conf.urls import url

from .views import SignInView


urlpatterns = [
    url(
        regex=r'^sign-in/$',
        view=SignInView.as_view(),
        name='login'
    ),
]
