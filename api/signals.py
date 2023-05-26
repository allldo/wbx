from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from .models import Location, Truck


@receiver(post_save, sender=Truck)
def add_location_to_truck(sender, instance, created, **kwargs):
    if created:
        instance.set_location()
