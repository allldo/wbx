import csv
from django.core.management import BaseCommand
from django.db import IntegrityError
from django.utils import timezone

from api.models import Location


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open("/drf_src/api/management/commands/uszips.csv", "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            skip_headers = next(data)
            pk = 0
            locations = []
            for row in data:
                location = Location(
                    id=pk,
                    zip_index=row[0],
                    latitude=row[1],
                    longitude=row[2],
                    city=row[3],
                    state=row[5]
                )
                pk += 1
                locations.append(location)
                if len(locations) > 3000:
                    try:
                        Location.objects.bulk_create(locations)
                    except IntegrityError:
                        break
                    locations = []
            if locations:
                try:
                    Location.objects.bulk_create(locations)
                except IntegrityError:
                    pass