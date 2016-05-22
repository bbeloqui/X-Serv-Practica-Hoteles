"""practica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

urlpatterns = [
    url(r'^(.*)/xml$',"hoteles.views.usuario_xml"),
    url(r'^more$', "hoteles.views.more"),
    url(r'^$', "hoteles.views.init"),
    url(r'^xml$', "hoteles.views.xml_init"),
    url(r'^canalRSS$', "hoteles.views.canalRSS"),
    url(r'^about$', "hoteles.views.about"),
    url(r'^alojamientos/(\d+)/xmlingles$',"hoteles.views.show_aloj_id_ingles"),
    url(r'^alojamientos/(\d+)/xmlfrances$',"hoteles.views.show_aloj_id_frances"),
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^alojamientos/admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/profile/$', 'hoteles.views.auth_view'),
    url(r'^alojamientos/accounts/profile/$', 'hoteles.views.auth_view'),
    url(r'^alojamientos$',"hoteles.views.show_aloj"),
    url(r'^alojamientos/(\d+)$',"hoteles.views.show_aloj_id"),
    url(r'^alojamientos/alojamiento/accounts/profile/$', 'hoteles.views.auth_view'),
    url(r'^admin/', admin.site.urls),
    #url(r'^alojamientos/(.*)$',"hoteles.views.usuario"),

    url(r'^(.*)$',"hoteles.views.usuario"),

]
