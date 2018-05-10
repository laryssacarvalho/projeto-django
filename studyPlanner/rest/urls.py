from django.conf.urls import url
from django.contrib import admin

from studyPlanner.rest.views import api_users, api_classes, api_tasks

urlpatterns = [
    url(r'^users', api_users, name='api_users'),
    url(r'^classes', api_classes, name='api_classes'),
    url(r'^tasks', api_tasks, name='api_tasks'),

]