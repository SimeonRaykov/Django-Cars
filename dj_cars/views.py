from django.shortcuts import render

from .models import Make, Car
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.db import connection


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, './error_404.html', data)


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def index(request):
    # Raw query
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM dj_cars_car '
                   'INNER JOIN dj_cars_make'
                   ' ON dj_cars_make.id = dj_cars_car.car_make_id_id')
    rows = dictfetchall(cursor)

    latest_car_list = Car.objects.select_related('car_make_id_id').values('car_model', 'horsepower','car_make_id__car_make').order_by('-horsepower')
    print(type(latest_car_list))
    fastest_car = Car.objects.select_related('car_make_id_id').values('car_model', 'horsepower', 'car_make_id__car_make').order_by('-horsepower')[:1].first()
    context = {'latest_car_list': latest_car_list,
               'fastest_car': fastest_car,
               'test': rows}
    # (rows)
    return render(request, '../templates/cars/cars.html', context)
