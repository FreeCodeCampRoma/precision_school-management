from django.conf.uls import url
from .views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home')
]
