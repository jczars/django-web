from django.conf.urls import url
from meuslivros.views import home, lista

urlpatterns = [
    url(r'^$', home),
    url(r'^lista-todos/$', lista),
]