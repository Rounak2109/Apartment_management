from django.shortcuts import render
from .models import Apartment, FlatTypes
from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class AboutView(TemplateView):
    template_name = "about.html"


def send_mail(request):

    return render(request, 'apartment/contact.html', {})


def apartment_list(request):
    apartment_list = Apartment.objects.all()
    return render(request, 'apartment/propertypage.html', {'apartments':apartment_list})


def property_details(request, pk):
    # filter_category_3,filter_category_2,filter_category_1,filter_category_4
    apartment = Apartment.objects.get(id=pk)
    apartment_amenities = apartment.amenities.split(",")
    flat_specifications = FlatTypes.objects.filter(apartment__name = apartment.name)
    return render(request, 'apartment/property_details.html', {'apartment':apartment_amenities, 'flattypes':flat_specifications})

