## Часть 1
```
grep -E '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$' addresses.list
```
Результат:
![](Pasted%20image%2020260518011023.png)

## Часть 2
не смог выполнить так как линукс астра не  позволяет установить нужные пакеты для считывания файлов, а файлы с разрешением *txt* к сожалению отсутсвуют
## Часть 3

```
tar -xOzf service.logs.tar.gz | grep -i "denied" | grep -oE "\b165\.103\.[0-9]{1,3}\.[0-9]{1,3}\b" | sort -u > subnet-one.list
```
```
tar -xOzf service.logs.tar.gz | grep -i "fulfilled" | grep -oE "\b185\.222\.[0-9]{1,3}\.[0-9]{1,3}\b" | sort -u > subnet-two.list
```

Архивируем:
```
tar - czf task3.tar.gs ips.list subnet-one.list subnet-two.list
```
