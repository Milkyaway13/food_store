# Food Store

Food Store - это проект интернет-магазина с корзиной покупок, реализованный с использованием Django и Django REST Framework.

## Описание

Проект представляет собой интернет-магазин, где пользователи могут просматривать продукты, добавлять их в корзину и удалять их из корзины. В проекте реализованы основные CRUD-операции для управления корзиной и продуктами.

## Технологии

- Django
- Django REST Framework
- SQLite
- Djoser

## Установка

### Клонирование репозитория

```bash
git clone git@github.com:Milkyaway13/food_store.git
```
### Перейдите в директорию:
```
cd food_store
```
### Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```
* Обновите установщик пакетов
```
python3 -m pip install --upgrade pip
```

* Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

* Выполните миграции:

```
python3 manage.py migrate
```

* Запустите проект:

```
python3 manage.py runserver
```
## Использование

### API Эндпоинты

#### Добавление продукта в корзину

- **URL:** `/store/cart/add_product/`
- **Метод:** `POST`
- **Тело запроса (JSON):**

  ```json
  {
      "product_id": 1,
      "quantity": 2
  }

