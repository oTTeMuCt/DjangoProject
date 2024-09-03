from .views import *
from django.urls import include, path

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path('reviews/', include('reviews.urls')),
]
