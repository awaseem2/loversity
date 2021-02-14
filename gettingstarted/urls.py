from django.urls import path, include
from django.conf.urls import url, include

from django.contrib import admin
from django.views.generic import ListView, DetailView
from hello.views import Users


admin.autodiscover()

import hello.views
from hello.models import Users

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    #url('submit/', ListView.as_view(queryset=Users.objects.all(), template_name = 'submit.html')),
    path("submit/", hello.views.submit, name="submit"),
    path("admin/", admin.site.urls)
]
