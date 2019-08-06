### Как создать подключение к БД MySQL ###

1. скачиваем MySQL https://dev.mysql.com/downloads/mysql и устанавливаем
    login sa
    pass bmssa
    
2. скачиваем драйвер для соединения python - MySQL https://dev.mysql.com/downloads/connector/python/
    перед скачиваем выбираем в выборе Select Operating system: Platform Independent
    скачиваем ZIP распаковываем, открываем терминал в распакованной папке 
    запускаем команду py setup.py install

3. Создание БД и таблиц для веб приложения
    открываем терминал MySQL и вводим mysql -u root -p
    создаем БД create database vsearchlogDB;
    создаем учетную запись и даем полные права на БД
        create user 'vsearch' identified by 'vsearchpasswd';
        grant all on vsearchlogDB.* to vsearch;
        quit

4. создаем таблицу в БД
    для начала нужно подключиться в БД новым пользователем
    открываем терминал в установленном каталоге MySQL (C:\Program Files\MySQL\MySQL Server 8.0\bin)
     и вводим: mysql -u vsearch -p vsearchlogDB
     затем пароль для пользователя vsearch: vsearchpasswd

    создаем таблицу с именем log
    mysql> create table log (
        -> id int auto_increment primary key,
        -> ts timestamp default current_timestamp,
        -> phrase varchar(128) not null,
        -> letters varchar(32) not null,  
        -> ip varchar(16) not null,
        -> browser_string varchar(256) not null,
        -> results varchar(64) not null );
    
    посмотреть что было создано в таблице командой: describe log;
    показать имена всех таблиц БД: show tables;
    показать все записи в таблице log: select * from log;

