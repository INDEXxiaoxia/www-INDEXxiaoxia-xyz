"""ftp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from sample import views
from filedown.views import file_Download
from tsubasa.views import indexadd,add,ajax_list,ajax_dict


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^folder/(?P<url>.+)/$', views.show_folder),
    url(r'^file/(?P<url>.+)/$', views.show_folder),
    url(r'^$', views.index),
    url(r'^download/$',file_Download),
    url(r'^newadd/$', indexadd,name='home'),
    url(r'^add/$', add,name='add'),
    url(r'^ajax_list/$', ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', ajax_dict, name='ajax-dict'),
]