from django.urls import path

from . import views

urlpatterns = [
  # path("january", views.january),
  # path("february", views.feburary),
  # path("march", views.march),
  path("<month>", views.monthly_challenge)
]