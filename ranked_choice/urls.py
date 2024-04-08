from django.urls import path

from . import views

app_name = "ranked_choice"

urlpatterns = [
    path("vote/<int:pk>", views.details, name="details"),
    path("", views.index, name="index"),
]
