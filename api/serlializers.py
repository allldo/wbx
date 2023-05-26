from rest_framework import serializers
from api.models import Cargo, Truck


class CargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargo
        fields = ['id', 'pick_up_location', 'delivery_location', 'weight', 'description']


class AllCargoSerializer(serializers.ModelSerializer):
    """ Serializer for /get_cargo_list , returns all cargos and number of trucks within 450 miles """

    number_of_closest_trucks = serializers.SerializerMethodField('get_number_of_closest_trucks')

    class Meta:
        model = Cargo
        fields = ['id', 'pick_up_location', 'delivery_location', 'number_of_closest_trucks', 'weight', 'description']

    def get_number_of_closest_trucks(self, cargo_object) -> int:
        return cargo_object.get_quantity_of_closest_trucks()


class SingleCargoSerializer(serializers.ModelSerializer):
    """ Serializer for /get_cargo_by_id/<int:cargo_id> , returns single cargo and all trucks with distance to it """

    trucks = serializers.SerializerMethodField('get_trucks_for_cargo')

    class Meta:
        model = Cargo
        fields = ['id', 'pick_up_location', 'delivery_location', 'trucks', 'weight', 'description']

    def get_trucks_for_cargo(self, cargo_object) -> dict:
        return cargo_object.get_trucks()


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ['id', 'license_plate', 'current_location', 'load_capacity']