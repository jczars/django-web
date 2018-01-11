"""dj_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from newapp.views import home, lista, novo, atualiza, deletar

urlpatterns = [
    url(r'^$', home),
    url(r'^lista-todos/$', lista),
    url(r'^novo/$', novo),
    url(r'^atualizar/(?P<id>\d+)/$', atualiza, name='atualizar'),
    url(r'^deletar/(?P<id>\d+)/$', deletar, name='deletar'),
]
