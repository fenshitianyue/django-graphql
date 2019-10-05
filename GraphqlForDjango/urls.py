"""GraphqlForDjango URL Configuration

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
from . import testdb
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register_form/$', testdb.register_form),
    url(r'^register/$', testdb.register),
    url(r'^get_user/$', testdb.get_user),
    url(r'^comment_form/$', testdb.push_comment_form),
    url(r'^comment/$', testdb.push_comment),
    url(r'^get_comment/$', testdb.get_comment),
    url(r'^graphql/&', GraphQLView.as_view(graphiql=True)),
]
