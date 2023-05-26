Как запустить проект: 
1. Клонировать репозиторий `git clone https://github.com/allldo/wbx.git` 
2. Перейти в папку с проектом`cd wbx`
3. Поднять докер`docker compose up -d`
4. Список ендпоинтов:
  1. api/get_cargo_list (GET)
  2. api/get_cargo_by_id/<int:id> (GET)
  3. api/edit_cargo_by_id/<int:id> (POST)
    Принимает weight и description
  5. api/edit_truck_by_id/<int:id> (POST)
    Принимает license_plate, zip_index и load_capacity
  7. api/create_cargo (POST)
    Принимает pick_up, delivery, weight, description
  9. api/delete_cargo_by_id/<int:id> (POST)
