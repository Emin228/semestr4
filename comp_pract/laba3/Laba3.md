## Запросы через telnet

Команда для подключения:
```c
telnet jsonplaceholder.typicode.com 80
```

Get
```c
GET /posts/1 HTTP/1.1
Host: jsonplaceholder.typicode.com
```
Результат:
```c
HTTP/1.1 200 OK
Date: ...
Content-Type: application/json; charset=utf-8
Content-Length: ...
{
   "userId": 1,
                 "id": 1,
                           "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                                                                                                                   "body
": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostru
m rerum est autem sunt rem eveniet architecto"
                                              }
```

Post
```c
POST /post HTTP/1.1
Host: httpbin.org
Content-Type: application/json
Content-Length: 28
Connection: close
{"title":"test","body":"123"}
```
Результат:
```c
{"title":"test","body":"123"}
```

## cURL
get
![](Pasted%20image%2020260603193729.png)
post
![](Pasted%20image%2020260603194333.png)

## Insomnia 
![](Pasted%20image%2020260603195917.png)
get-запрос
```cmd
http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/03/2025&date_req2=07/03/2025&VAL_NM_RQ=R01239
```

## Простейший чат
Понадобиться запустить сразу два терминала 

Запуск сервера(1):
![](Pasted%20image%2020260603200454.png)
Подключение к хосту(2):
![](Pasted%20image%2020260603200512.png)

Теперь чтобы мы не напислаи ни в один из терминалов, он сразу отправиться во второй:
![](Pasted%20image%2020260603200554.png)
Для выхода Cntrl+C

