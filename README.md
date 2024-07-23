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

### Клонируйте репозиторий

```bash
git clone git@github.com:Milkyaway13/food_store.git
```
### Перейдите в директорию:
```
cd food_store
```
### Cоздайте и активируйте виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```
* Обновите установщик пакетов
    ```
    python -m pip install --upgrade pip
    ```

* Установите зависимости из файла requirements.txt:

    ```
    pip install -r requirements.txt
    ```

* Выполните миграции:

    ```
    python manage.py migrate
    ```

* Запустите проект:

    ```
    python manage.py runserver
    ```
## Примеры запросов

#### Добавление продукта в корзину

- **URL:** `/store/cart/add_product/`
- **Метод:** `POST`
- **Тело запроса (JSON):**

  ```json
  {
      "product_id": 1,
      "quantity": 2
  }
  ```
- Ответ:
  ```json
  {
      "status": "Product added to cart"
  }
  ```
#### Удаление продукта из корзины

- **URL:** `/store/cart/remove_product/`
- **Метод:** `POST`
- **Тело запроса (JSON):**

  ```json
  {
      "product_id": 8
  }
  ```
 - Ответ:
 
      Код состояния HTTP 204 No content
   
## Автор
[Боярчук Василий](https://github.com/Milkyaway13/)
  
  

