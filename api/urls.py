from django.contrib import admin
from django.urls import path, include


from .views import create_cargo, get_cargo_list, get_cargo_by_id, edit_cargo_by_id, delete_cargo_by_id, edit_truck_by_id


urlpatterns = [
    path('create_cargo', create_cargo),
    path('get_cargo_list', get_cargo_list),
    path('get_cargo_by_id/<int:cargo_id>', get_cargo_by_id),
    path('edit_cargo_by_id/<int:cargo_id>', edit_cargo_by_id),
    path('delete_cargo_by_id/<int:cargo_id>', delete_cargo_by_id),
    path('edit_truck_by_id/<int:truck_id>', edit_truck_by_id)
]
