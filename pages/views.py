# pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class ParkenPageView(TemplateView):
    template_name = "parken.html"


class VerpflegungPageView(TemplateView):
    template_name = "verpflegung.html"


class MusikPageView(TemplateView):
    template_name = "musik.html"
