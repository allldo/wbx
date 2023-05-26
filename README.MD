Как запустить проект: 
1. Клонировать репозиторий `git clone https://github.com/allldo/wbx.git` 
2. Перейти в папку с проектом`cd wbx`
3. Поднять докер`docker compose up -d`

## Доступные апи ендпоинты

#### Get all cargoes

```http
  GET /api/get_cargo_list
```

#### Get single cargo

```http
  GET /api/get_cargo_by_id/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |

#### Add cargo

```http
  POST /api/create_cargo/
```

| Arguments | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `pick_up`      | `str` | **Required**. Zip index of location |
`delivery`      | `str` | **Required**. Zip index of location |
`weight`      | `int` | **Required**. Weight of the cargo |
`description`      | `str` | **Required**. Description of the cargo |

#### Edit cargo

```http
  POST /api/edit_cargo_by_id/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |
| Arguments | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `weight`      | `int` | **Required**. Weight of the cargo |
| `description`      | `str` | **Required**. Description of the cargo |

#### Delete cargo


```http
  POST /api/delete_cargo_by_id/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |

#### Edit truck

```http
  POST /api/edit_truck_by_id/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to edit |

| Argument | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `license_plate`      | `str` | **Required**. Id of item to edit |
| `zip_index`      | `str` | **Required**. Id of item to edit |
| `load_capacity`      | `str` | **Required**. Id of item to edit |
