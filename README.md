# Автотест API Яндекс.Самоката

Проверяет сценарий: создание заказа → получение заказа по треку → код ответа 200.
Дополнительно — smoke-проверка доступности сервера.

## Установка

```bash
pip install -r requirements.txt
```

## Настройка

В `configuration.py` заменить `URL_SERVICE` на адрес стенда.
При необходимости скорректировать `order_data` в `data.py` под актуальный контракт API.

## Запуск

```bash
pytest -v
```

## Структура

```
api_scooter_order_test/
├── configuration.py
├── data.py
├── sender_stand_request.py
├── test_create_and_get_order.py
├── database_tasks.sql            
├── requirements.txt
├── .gitignore
└── README.md
```

## Логи

`/var/www/backend/logs/error.log`