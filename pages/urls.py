# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, MusikPageView
from .views import ParkenPageView, VerpflegungPageView


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("parken/", ParkenPageView.as_view(), name="parken"),
    path("musik/", MusikPageView.as_view(), name="musik"),
    path("verpflegung/", VerpflegungPageView.as_view(), name="verpflegung"),
]
