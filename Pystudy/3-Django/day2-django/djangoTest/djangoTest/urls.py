"""djangoTest URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
import users.urls
import argsTest.urls
import  responseTest.urls
import cookie_app.urls
import  session_app.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/',include(users.urls,namespace='users')),
    # url(r'^users/',include(users.urls)),
    url(r'^argsTest/',include(argsTest.urls,namespace='argsTest')),
    # url(r'^argsTest/',include("argsTest.urls")),
    url(r'^responseTest/', include(responseTest.urls, namespace='responseTest')),

    url(r'^cookie_app/', include(cookie_app.urls, namespace='cookie_app')),

    url(r'^session_app/', include(session_app.urls, namespace='session_app')),


]