from typing import List

from django.shortcuts import get_object_or_404

from api.models import Location, Cargo
from api.serlializers import SingleCargoSerializer


def add_new_cargo(data: dict) -> bool:
    try:
        pickup_location = get_object_or_404(Location, zip_index=data['pick_up'])
        delivery_location = get_object_or_404(Location, zip_index=data['delivery'])
        weight = data['weight']
        description = data['description']
        Cargo.objects.create(
            pick_up_location=pickup_location, delivery_location=delivery_location,
            weight=weight, description=description)
    except Exception as e:
        return False

    return True


def delete_cargo(cargo_id: int) -> bool:
    try:
        get_object_or_404(Cargo, id=cargo_id).delete()
    except Exception as e:
        return False

    return True


def get_serialized_cargo(cargo_id: int) -> dict:
    cargo = get_object_or_404(Cargo, id=cargo_id)
    return SingleCargoSerializer(cargo).data
