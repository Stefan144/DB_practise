 Выполнил: Николич Стефан (БПМИ144)
 
 ### Содержание
1. Постановка задачи
1. Концептуальное проектирование
    a. Описание предметной области.
    b. Описание построения инфологической модели.
    c. ER-диаграмма.
2. Проектирование реляционной модели
    a. Описание процесса перехода к "многие ко многим" моделям.
    b. Диаграмма схемы БД.
3. Развертывание БД в выбранной СУБД
    a. DDL-скрипт создания схемы БД.
    b. Примеры DML-операторов вставки тестовых данных.
4. Примеры работы
    a. SQL-запросы
5. Заключение

### Постановка задачи



### Концептуальное проектирование
a) Предметная среда - киноиндустрия. Состоит из огромного стека компонент(режиссеры, актеры, студия и т.д.), задача которых в коллаборации произвести фильм готовый к показу. 

b) На уровне концептуального проектирования было выделено 5 основных сущностей предметной области: фильмы(films), кинокомпании (film\_studio), режиссеры(film\_director), актеры(actors) и страны(coutries). Сущностям же были подобраны соответствующие им основные атрибуты(все изображено ниже).

c)ER-diagram(нотация Чена)
![](http://i.imgur.com/tUR8cDS.png)

### Проектирование реляционной модели
a) В процессе создания базы на PostgreSQL стало понятно, что не разумно хранить в атрибуте какой-либо сущности несколько разных значений, причем сами значения повторяются на разных объектах - это называется отношение многие ко многим(например, в нашем случае - у фильма может быть несколько стран производителей + страна может участвовать в создании многих фильмов). Разумно было создать вспомогательные таблицы, которые бы, хранили парно нужные атрибуты. В нашем случае их образовалось 2 - film\_country и film\_actors(тоже самое: один актер может участвовать во многих фильмах и в одном фильме, разумеется, участвует больше одного актера). Хранение каждого атрибута осуществляете в разумном для него типе данных, что дает уверенность в соответствии данных истине.

b) Table-Relationship Digram
![](http://i.imgur.com/cifmDXL.png)



### Развертывание БД в выбранной СУБД
a) DDL-скрипт создания схемы БД.
```sql
CREATE TABLE director (
	director_id serial PRIMARY KEY,
	director_name varchar(50) NOT NULL,
	director_last_name varchar(50) NOT NULL
);

CREATE TABLE countries (
	country_id serial PRIMARY KEY,
    country_name varchar(50) NOT NULL,
	average_gdp smallint NOT NULL
);

CREATE TABLE film_studio (
	studio_id serial PRIMARY KEY,
	studio_name varchar(50) NOT NULL,
	country_id int REFERENCES countries(country_id)  ON UPDATE CASCADE
);

CREATE TABLE films (
	film_id serial PRIMARY KEY,
    film_title varchar(50) NOT NULL,
	production_year smallint NOT NULL,
	budget real NOT NULL,
	box_office real NOT NULL,
	director_id serial REFERENCES director(director_id) ON UPDATE CASCADE,
	studio_id serial REFERENCES film_studio(studio_id) ON UPDATE CASCADE
);

CREATE TABLE film_country (
	film_id int REFERENCES films(film_id)  ON UPDATE CASCADE,
    country_id int REFERENCES countries(country_id)  ON UPDATE CASCADE,
	CONSTRAINT film_country_pkey PRIMARY KEY (film_id, country_id)
);

CREATE TABLE actors (
	actor_id serial PRIMARY KEY,
	actor_name varchar(50) NOT NULL,
	actor_last_name varchar(50) NOT NULL
);

CREATE TABLE film_actors (
	film_id int REFERENCES films(film_id)  ON UPDATE CASCADE,
    actor_id int REFERENCES actors(actor_id)  ON UPDATE CASCADE,
	CONSTRAINT film_actor_pkey PRIMARY KEY (film_id, actor_id)
);
```

### Примеры работы


