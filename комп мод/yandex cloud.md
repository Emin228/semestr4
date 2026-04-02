
## 1.Создание бакета
Нужно задать для бакета базовые настройки, такие как имя , задать макс. размер, указать класс( стандартное, холодное, ледяное), указать права доступа, шифрование и тд

<img width="636" height="723" alt="Screenshot 2026-04-02 155335" src="https://github.com/user-attachments/assets/9cccb796-055a-468e-9106-3589b7e1df21" />


Готов наш первый бакет был создан:
<img width="898" height="199" alt="Screenshot 2026-04-02 155732" src="https://github.com/user-attachments/assets/43d84d94-2882-4283-ae27-e17a543faf4b" />



## 2.Создание сервисного аккаунта

В яндекс консоли ищем вкладку "Identity and Access Management", полсе чего выбираем создание своего первого сервисного аккаунта:
<img width="720" height="390" alt="Screenshot 2026-04-02 161246" src="https://github.com/user-attachments/assets/ac5113b6-2ae1-414f-920f-6fb754a0089f" />



Готов аккаунт был создан:

<img width="1223" height="239" alt="Screenshot 2026-04-02 161406" src="https://github.com/user-attachments/assets/9075c6be-9610-4380-bb17-9bb9cb0c91a2" />


Также создаём статический Api-ключ и сохраняем полученныйе индентификаторв ключа и личный секретный ключ


## 3.Предоставление сервисному аккаунта прав доступа:
Для этого возвращаемся в бакет -> Безопасность -> Права доступа -> Назначить роль
<img width="706" height="474" alt="Screenshot 2026-04-02 161656" src="https://github.com/user-attachments/assets/595b343b-c840-45eb-bccd-26768fdbbe31" />

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
<img width="1077" height="293" alt="Screenshot 2026-04-02 225011" src="https://github.com/user-attachments/assets/57c1d547-464c-4ec5-a31b-3da8ef2e46b1" />


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
<img width="617" height="153" alt="Screenshot 2026-04-02 225125" src="https://github.com/user-attachments/assets/c06a0d68-1c37-485c-abc5-f42ece03f146" />

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
<img width="611" height="115" alt="Screenshot 2026-04-02 225312" src="https://github.com/user-attachments/assets/8f1504bb-d23c-4e6c-8f5b-8d123a073d7e" />


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
<img width="1122" height="537" alt="Screenshot 2026-04-02 225403" src="https://github.com/user-attachments/assets/e080b1ba-b32b-4817-b25d-18d6ca797661" />


