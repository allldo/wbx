import string

from django.core.management import BaseCommand
import random
from api.models import Truck


class Command(BaseCommand):

    def handle(self, *args, **options):

        total_trucks = 20

        for truck in range(total_trucks):
            license_plate = f'{random.randint(1000, 9999)}{random.choice(string.ascii_uppercase)}'
            load_capacity = random.randint(1, 1000)
            try:
                Truck.objects.create(
                    license_plate=license_plate,
                    load_capacity=load_capacity
                )
            except Exception as e:
                print(e)