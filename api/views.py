from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Cargo, Truck
from api.serlializers import AllCargoSerializer, SingleCargoSerializer, CargoSerializer, TruckSerializer
from api.services import add_new_cargo, delete_cargo, get_serialized_cargo


@api_view(['POST'])
def create_cargo(request) -> Response:
    """ To create cargo you must pass pick_up, delivery, weight, description """
    result = add_new_cargo(request.data)
    if result:
        return Response({
            'result': 'CargoAdded'
        })
    else:
        return Response({
            'result': 'Error while creating Cargo'
        })


@api_view(['GET'])
def get_cargo_list(request):
    """ Returns all cargos with number of trucks within 450 miles """
    return Response({
        'cargos': AllCargoSerializer(Cargo.objects.all(), many=True).data
    })


@api_view(['GET'])
def get_cargo_by_id(request, cargo_id):
    cargo_serialized = get_serialized_cargo(cargo_id)
    return Response({
        'cargo': cargo_serialized
    })


@api_view(['POST'])
def edit_cargo_by_id(request, cargo_id):
    """ To edit cargo you must pass weight and description """
    edited_cargo = get_object_or_404(Cargo, id=cargo_id).edit_cargo(request.data)
    return Response({
        'cargo': CargoSerializer(edited_cargo).data
    })


@api_view(['POST'])
def delete_cargo_by_id(request, cargo_id):
    result = delete_cargo(cargo_id)
    if result:
        return Response({
            'result': 'Cargo was successfully deleted'
        })
    else:
        return Response({
            'result': 'Error while deleting Cargo'
        })


@api_view(['POST'])
def edit_truck_by_id(request, truck_id):
    """ To edit cargo you must pass license_plate, zip_index, load_capacity """
    edited_truck = get_object_or_404(Truck, id=truck_id).edit_truck(request.data)
    return Response({
        'truck': TruckSerializer(edited_truck).data
    })
