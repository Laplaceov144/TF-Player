from django.urls import path
from . import views

urlpatterns = [
    path("refresh-titles/", views.index, name="index"),
    path('api/submit-playlist/', views.submit_playlist, name='submit_playlist'),
    path('refresh-titles/onsubmit', views.submit_titles, name='submit_titles')
]
