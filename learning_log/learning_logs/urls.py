"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

# Helps Django distinguish this urls.py file from files of the same name in other apps within the project.
app_name = 'learning_logs'
# A list of individual pages that can be requested from the learning_logs app.
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic')
]