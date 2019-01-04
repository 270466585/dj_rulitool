"""dj_rulitool URL Configuration

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
from django.contrib import admin
from urls import views as urls_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$',urls_views.login),
    url(r'^register$',urls_views.register),
    url(r'^urlstool$',urls_views.home),
    url(r'^urls_all$',urls_views.urls_all),
    url(r'^logout$',urls_views.logout),
]
