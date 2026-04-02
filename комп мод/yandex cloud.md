
## 1.Создание бакета
Нужно задать для бакета базовые настройки, такие как имя , задать макс. размер, указать класс( стандартное, холодное, ледяное), указать права доступа, шифрование и тд

<img width="636" height="723" alt="Screenshot 2026-04-02 155335" src="https://github.com/user-attachments/assets/9cccb796-055a-468e-9106-3589b7e1df21" />


Готов наш первый бакет был создан:
![[Pasted image 20260402155740.png]]


## 2.Создание сервисного аккаунта

В яндекс консоли ищем вкладку "Identity and Access Management", полсе чего выбираем создание своего первого сервисного аккаунта:
![[Pasted image 20260402161247.png]]


Готов аккаунт был создан:

![[Pasted image 20260402161408.png]]

Также создаём статический Api-ключ и сохраняем полученныйе индентификаторв ключа и личный секретный ключ


## 3.Предоставление сервисному аккаунта прав доступа:
Для этого возвращаемся в бакет -> Безопасность -> Права доступа -> Назначить роль:![[Pasted image 20260402161659.png]]
Выбираем созданный акк, и самое главное выдаём ему роль "editor", для наших задач (загрузка, скачивание, просмотр списка, удаление файлов)

## 4.Реализация функций для выполнения основных операций

Перед  началом нужно настроить конфигурацию для этого понадобится по пути User\.aws создать два файла:

config:
*[default]*
*region = ru-central1*

credentials:
*[default]*
*aws_access_key_id = ...*
*aws_secret_access_key = ...*

Для локальной работы был выбран boto3, установка:
**pip install boto3**

Всё готов к работе, переходим к реализации базовых функций:
Для начала пропишем:

```python
import boto3

def s3_client():
    session = boto3.session.Session()
    return session.client(
        service_name='s3',
        endpoint_url="https://storage.yandexcloud.net"
    )
```
### Загрузка файлов:

```python
def s3_upload(file:str, buck:str, key:str):
    s = s3_client()
    s.upload_file(file, buck, key)
```

Запуск функции:
```python
s3_upload("example.txt", buck, key)
```

После запуска в YandexCloud видим добавленный файл:
![[Pasted image 20260402225012.png]]

### Получение спика файлов:

```python
def s3_getAllFiles(buck: str):
    s = s3_client()
    for key in s.list_objects(Bucket=buck)['Contents']:
        print(key['Key'])
```

Запуск функции:
```python
s3_getAllFiles(buck)
```

Вывод в терминале:
![[Pasted image 20260402225127.png]]
Так как у нас пока только один добавленный файл, он нам и выводится
### Прочтение конкретного файла:

```python
def s3_get(buck:str, key:str):
    s = s3_client()
    get_obj = s.get_object(Bucket=buck, Key=key)
    print(get_obj['Body'].read())
```

Запуск функции;
```python
s3_get(buck, key)
```

Вывод в терминале:
![[Pasted image 20260402225322.png]]

### Удаление файла:

```python
def s3_delete(buck:str, key:str):
    s = s3_client()
    forDeletion = [{'Key':'object_name'}, {'Key': key }]
    response = s.delete_objects(Bucket=buck, Delete={'Objects': forDeletion})
```

Запуск функции:
```python
s3_delete(buck, key)
```

После выполнения функции в YandexCloud уже будет отсутсвовать файл, так как он был удалён:
![[Pasted image 20260402225431.png]]

