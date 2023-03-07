from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class DashboardLogin(TemplateView):
    template_name = "index_dashboard.html"


