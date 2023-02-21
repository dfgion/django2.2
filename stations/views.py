from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    with open(file=BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_of_stations = [element for element in reader]
        paginator = Paginator(list_of_stations, 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page
        }
    return render(request, 'stations/index.html', context)
