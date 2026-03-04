
### Задание 1:

Раздел «Instance» («Экземпляр БД»):
1. Раздел «Startup / Shutdown».  
    В разделе осуществляется управление состоянием сервера базы данных. Предусмотрены следующие возможности:  
    a. Запуск сервера.  
    b. Остановка сервера.  
    c. Перезапуск сервера.  
    d. Контроль текущего состояния службы сервера.
    
2. Раздел «Options File».  
    В разделе выполняется настройка конфигурационного файла сервера (my.cnf или my.ini). Параметры сгруппированы по категориям. Можно выделить следующие группы настроек:  
    a. Параметры памяти (размер буферов, кэширование).  
    b. Параметры подключений (максимальное число соединений, тайм-ауты).  
    c. Настройки журналирования (включение логов, журнал медленных запросов).  
    d. Параметры механизмов хранения данных.  
    e. Репликация и сетевые параметры.
    
3. Раздел «Environment».  
    В разделе отображается информация о среде функционирования сервера. Можно выделить следующие сведения:  
    a. Пути к системным и рабочим каталогам.  
    b. Расположение файлов базы данных.  
    c. Используемые переменные окружения.  
    d. Версия сервера и операционной системы.
    
4. Раздел «Users and Privileges».  
    В разделе осуществляется управление учетными записями пользователей. Доступны следующие функции:  
    a. Создание и удаление пользователей.  
    b. Назначение ролей.  
    c. Настройка прав доступа к базам данных и объектам.  
    d. Управление способами аутентификации.
    
5. Раздел «Data Export / Data Import».  
    В разделе реализованы средства резервного копирования и восстановления данных:  
    a. Экспорт баз данных в SQL-файлы.  
    b. Импорт дампов баз данных.  
    c. Выбор отдельных схем и таблиц для экспорта.  
    d. Настройка параметров резервного копирования.


---

Раздел «Performance» («Производительность»):

1. Раздел «Performance Dashboard».  
    В разделе отображаются основные показатели работы сервера в режиме реального времени. Информация представлена в виде графиков и диаграмм. Можно выделить следующие показатели:  
    a. Загрузка процессора.  
    b. Использование оперативной памяти.  
    c. Количество активных подключений.  
    d. Число выполняемых запросов.  
    e. Операции чтения и записи.
    
2. Раздел «Performance Reports».  
    В разделе формируются аналитические отчёты о работе сервера. Можно выделить следующие типы отчетов:  
    a. Медленные запросы.  
    b. Наиболее ресурсоемкие операции.  
    c. Статистика использования индексов.  
    d. Информация о блокировках.
    
3. Раздел «Query Statistics».  
    В разделе отображается статистика выполнения SQL-запросов. Представлена следующая информация:  
    a. Время выполнения запросов.  
    b. Частота выполнения.  
    c. Объем обрабатываемых данных.  
    d. Сравнительный анализ запросов по нагрузке.
    
4. Раздел «Clients and Connections».  
    В разделе отображается информация о текущих подключениях к серверу:  
    a. Список активных пользователей.  
    b. Текущие выполняемые запросы.  
    c. Состояние потоков.  
    d. Параметры подключений.
    
5. Раздел «Server Logs».  
    В разделе предоставляется доступ к журналам сервера. Можно выделить следующие типы журналов:  
    a. Журнал ошибок.  
    b. Общий журнал запросов.  
    c. Журнал медленных запросов.  
    d. Журнал двоичного логирования (при включении).
    

---

Задание 3:
```mysql
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

```

Заданиие 4:

```mysql
INSERT INTO `simpledb`.`users` (`id`, `name`, `email`) VALUES ('', 'Emin', 'emingo055@gmail.com');
INSERT INTO `simpledb`.`users` (`name`, `email`) VALUES ('Sanya', 'newtelephone228@gmail.com');

```

```mysql
UPDATE `simpledb`.`users` SET `email` = 'sanyakrut228@gmail.com' WHERE (`id` = '2');
```


Задание 5:
```mysql
ALTER TABLE `simpledb`.`users` 
ADD COLUMN `gender` ENUM('M', 'F') NULL AFTER `email`,
ADD COLUMN `bday` DATE NULL AFTER `gender`,
ADD COLUMN `postal_code` VARCHAR(10) NULL AFTER `bday`,
ADD COLUMN `rating` FLOAT NOT NULL AFTER `postal_code`,
ADD COLUMN `created` TIMESTAMP NOT NULL AFTER `rating`,
CHANGE COLUMN `name` `name` VARCHAR(50) NOT NULL ;
```

Задание 6
Вручную в таблицу были внесены следующие данные:
![[Pasted image 20260304114213.png]]

C помощью SQl-запроса было добавлено еще 2 юзера
![[Pasted image 20260304114437.png]]

Задание 7
```mysql
INSERT INTO `` (`id`,`name`,`email`,`gender`,`bday`,`postal_code`,`rating`,`created`) VALUES (1,'Emin','emingo055@gmail.com','M','2006-08-12','1123',0,'2026-02-04 11:20:20');
INSERT INTO `` (`id`,`name`,`email`,`gender`,`bday`,`postal_code`,`rating`,`created`) VALUES (2,'Sanya','sanyakrut228@gmail.com','M','2001-02-11','3312',0,'2026-02-04 11:30:20');
INSERT INTO `` (`id`,`name`,`email`,`gender`,`bday`,`postal_code`,`rating`,`created`) VALUES (3,'Andrey','sdfvjiko2134@gmail.com','M','2010-10-10','1323',10,'2026-02-04 11:40:20');
INSERT INTO `` (`id`,`name`,`email`,`gender`,`bday`,`postal_code`,`rating`,`created`) VALUES (4,'Ekaterina','ekaterina.petrova@outlook.com','F','2000-02-11','145789',1.123,'2026-03-04 11:42:47');
INSERT INTO `` (`id`,`name`,`email`,`gender`,`bday`,`postal_code`,`rating`,`created`) VALUES (5,'Paul','paul@superpochta.ru','M','1998-08-12','123789',1,'2026-03-04 11:42:47');

```

Задание 8:

```mysql
CREATE TABLE `simpledb`.`resume` (
  `resumeid` INT NOT NULL AUTO_INCREMENT,
  `userid` INT NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `skills` TEXT NULL,
  `created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`resumeid`),
  INDEX `userid_idx` (`userid` ASC) VISIBLE,
  CONSTRAINT `userid`
    FOREIGN KEY (`userid`)
    REFERENCES `simpledb`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

```

Так как мы задали тип удаления CASCADE, то при удалении значений из таблицы, все связанные с ним значения из других таблиц тоже будут удалены
Задание 9:
	При попытке добавить в таблицу resume пользователя ID которого не сущестует, высветиться следующая ошибкa
	![[Pasted image 20260304120815.png]]
```mysql
INSERT INTO `` (`resumeid`,`userid`,`title`,`skills`,`created`) VALUES (1,1,'zxc','xxxx','2026-03-04 12:06:49');
INSERT INTO `` (`resumeid`,`userid`,`title`,`skills`,`created`) VALUES (2,2,'qaz','zzzz','2026-03-04 12:06:49');
INSERT INTO `` (`resumeid`,`userid`,`title`,`skills`,`created`) VALUES (5,4,'wedf','asz','2026-03-04 12:08:53');
INSERT INTO `` (`resumeid`,`userid`,`title`,`skills`,`created`) VALUES (6,2,'fgfd','asdada','2026-03-04 12:08:53');
```

Задание 10:
```mysql
DELETE FROM `simpledb`.`users` WHERE (`id` = '5' or 'id' = '4');
```

После удаления пользвателя из таблицы users 
его резюме будет удалено из таблицы resume:
![[Pasted image 20260304121246.png]]

Попробуем изменить айди пльзователя имеющего резюме в таблице reums
```mysql
UPDATE `simpledb`.`users` SET `id` = '10' WHERE (`id` = '1');
```
 Результат:
 ![[Pasted image 20260304121356.png]]
как мы видим таблица resume автоматически обновится и заменит ID.