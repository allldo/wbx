from __future__ import annotations

from django.db import models
from django.shortcuts import get_object_or_404
from geopy.distance import geodesic
import random


class Cargo(models.Model):
    """ Cargo model """
    pick_up_location = models.ForeignKey('Location', on_delete=models.SET_NULL, related_name='pick_up_locations',
                                         null=True, verbose_name='Pickup location for a cargo')
    delivery_location = models.ForeignKey('Location', on_delete=models.SET_NULL, related_name='delivery_locations',
                                          null=True, verbose_name='Delivery location for a cargo')
    weight = models.PositiveIntegerField(null=False, verbose_name='Weight of a cargo')
    description = models.TextField(null=False, verbose_name='Description of a cargo')

    def get_quantity_of_closest_trucks(self) -> int:
        """ Here we are looking for closest trucks to pickup location """
        first_point = (self.pick_up_location.latitude, self.pick_up_location.longitude)
        quantity = 0
        for truck in Truck.objects.filter(current_location__city__isnull=False):
            if geodesic(first_point, (truck.current_location.latitude, truck.current_location.longitude)).miles <= 450:
                quantity += 1
        return quantity

    def get_trucks(self) -> dict:
        """ Getting all trucks with a distance to cargo """
        trucks = {}
        coordinates_of_cargo = (self.pick_up_location.latitude, self.pick_up_location.longitude)
        for truck in Truck.objects.all():
            trucks[truck.license_plate] = geodesic(coordinates_of_cargo, (truck.current_location.latitude,
                                                                          truck.current_location.longitude)).miles
        return trucks

    def edit_cargo(self, data) -> Cargo:
        self.weight = data['weight']
        self.description = data['description']
        self.save()

        return self


class Truck(models.Model):
    """ Truck model, instances are loaded randomly from script """
    license_plate = models.CharField(max_length=5, null=False, unique=True, verbose_name='License plate of a truck')
    current_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True,
                                         verbose_name='Current location for a truck')
    load_capacity = models.PositiveIntegerField(null=False, verbose_name='Load capacity of a truck')

    def edit_truck(self, data: dict) -> Truck:
        self.license_plate = data['license_plate']
        self.current_location = get_object_or_404(Location, zip_index=data['zip_index'])
        self.load_capacity = data['load_capacity']
        self.save()
        return self

    def set_location(self):
        self.current_location = random.choice(Location.objects.all())
        self.save()


class Location(models.Model):
    """ Location model, instances are loaded from csv file """
    city = models.CharField(max_length=255, null=False, verbose_name='City of a location')
    state = models.CharField(max_length=255, null=False, verbose_name='State of a location')
    zip_index = models.CharField(max_length=100, null=False, verbose_name='Zip of a location')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name='Longitude of a location')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name='Latitude of a location')

