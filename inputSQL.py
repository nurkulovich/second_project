# CREATE DATABASE test; создать базу данных с названием test

# \l -> вывод списка всех имеющихся баз данных (q - чтобы выйти мз окна просмотра списков)
# \c test  ->  установления соединения с базой данных по имени test

типы полей:
1. Числовые поля
SMALLINT - целые числа ограниченные по значению(2 байт)
от -32768 до 32768
INTEGER - целые числа(4 байт)
от -2147483648 до 2147483648 
BIGINT - целын числа (8 байт)
от -9223372036854775808 до 9223372036854775807

SMALLSERIAL - целые числа с автоинкриментом(2 байт)
от 1 до 32768
SERIAL - 4 байт, от 1 до 2147483648 
BIGSERIAL - 8 байт, от 1 до 9223372036854775807

REAL - 4 байта, дробные числа  точностью до 6 знаков
DOUBLE PRECISION - 8 байт, точность до 15 знаков
NUMERIC - точность до 131072 знаков до запятой и 16383 знаков после запятой
DECIMAL - точность до 131072 знаков до запятой и 16383 знаков после запятой

MONEY - 8 байт -92233720368547758.08 to +92233720368547758.07


2. Строчные

CHAR - строка постоянной длины
VARCHAR - строка переменной длины 
'iPhone 7'
CHAR(10) - 'iPhone 7  '
VARCHAR(10) - 'iPhone 7'
TEXT - Строки неограниченной длины

3. Дата и время

DATE

TIME 

4. Остальные

BOOLEAN - 1 байт 't', 'f'

ENUM() - выбор из нескольких вариантов

Ограничения (Constrains)

NOT NULL/NULL - является ли поле обязательным для заполнения при создании записи

UNIQUE - должны ли быть значения в определенном поле уникальными 

CHEK - проверка значения по определенному условию

PRIMARY KEY - первичный ключ

FOREIGN KEY - Внешний ключ

# \dt -  вывод списка таблиц

# \d name - вывод информации о таблице 

INSERT INTO название_таблицы (поле1, поле2, ...) VALUES (значени1, значение2, ...);

SELECT * FROM название_таблицы; - выборка всех данных по таблице

SELECT title, price FROM product; - выборка определенных полей 

# DELETE FROM название_таблицы;
# DELETE FROM название_таблицы WHERE email='user1@mail.ru';

Манипуляции с БД (Удаление БД, создание таблиц, редактирование таблиц, редактирование полей,Удаление таблиц и полей)

CREATE DATABASE название_БД; - создание БД
DROP DATABASE название_БД; - удаление БД
ALTER TABLE - изменение таблицы (переименование таблицы, добавление, редактирование, переименование и удаление полей,
добавление связей между таблицами)
ALTER TABLE client RENAME TO customer; переименование таблицы client на customer
ALTER TABLE customer ADD COLUMN address VARCHAR(50) NULL; добавление поля address  в таблицу customer
ALTER TABLE customer RENAME COLUMN first_name TO name; - переименование поля first_name на name в таблице customer
ALTER TABLE customer ALTER COLUMN last_name TYPE VARCHAR(100); - изменение типа поля last_name на VARCHAR(100) в таблице customer
ALTER TABLE customer ALTER COLUMN last_name SET NOT NULL; - изменение Ограничения поля last_name на NOT NULL 
ALTER TABLE customer ALTER COLUMN last_name DROP NOT NULL; - изменение Ограничения поля last_name на NULL 
ALTER TABLE product ADD CONSTRAINT product_title_unique UNIQUE (title); - добавление ограничения UNIQUE под названием product_title_unique на поле title 
ALTER TABLE product DROP CONSTRAINT product_title_unique; - удаление ограничения
КАк составить название ограничения
название_таблицы_название_поля_название ограничения
 ALTER TABLE customer DROP COLUMN address; -удаление поля  address с таблицы customer


Манипуляции с данными (INSERT, UPDATE, SELECT, DELETE)
INSERT - вставка(создание записей)
INSERT INTO название_таблицы (назв_полей) VALUES (значения), (значения);

SELECt - выборка (получение) записей
SELECT * FROM название_таблицы;

получение определенных полей
SELECT title, price FROM product;

филтрация данных(записей)
SELECT название_полей FROM название_таблицы WHERE условия;

условия по числовым полям и дате
операции сравнения:
"=" - равенство
"==", "<>" -неравенство
">" - больше
"<" - меньше
">=" - больше или равно 
"<=" - меньше или равно
SELECT * FROM product WHERE price >= '50000';

AND, OR - и, или
SELECT * FROM product WHERE price > '50000' AND price < '60000';

BETWEEN
SELECT * FROM product WHERE price BETWEEN '50000' AND '60000';

IN - проверка на вхождения
IS NULL - проверка на пустое значение 
IS NOT NULL - проверка на не пустое значение
NOT - отрицание условия


условия по текстовым полям

"=" - равенство
LIKE - проверка на вхождение подстроки (учитывает регистр)
ILIKE - проверка на вхождение подстроки (НЕучитывает регистр)


SELECT * FROM product WHERE title LIKE 'Apple%'; проверка что title начинается со слова Apple
SELECT * FROM product WHERE title LIKE '%iPhone%'; проверка что в title есть слово iPhone
проверка подстроки на вхождение в строку

SELECT * FrOM product WHERE price IN ('45000', '50000');



IN - проверка на вхождения в список вариантов
AND, OR - и, или




сортировка

SELECT * FROM product ORDER BY price ASC; по возрастанию
SELECT * FROM product ORDER BY price DESC; в порядке убывания

SELECT * FROM product ORDER BY title; по алфавиту

 SELECT title  FROM product whERE price BETWEEN '45000' and '50000' ORDER BY price DESC;

SeleCT * FROM product LimiT 2;
SeleCT * FROM product LimiT 2 OFFSET 2;
для ограничения получения используется LIMIT , а OFFSET чтобы пропустить
 SELECT title  FROM product whERE price BETWEEN '45000' and '50000' ORDER BY price DESC LIMIT 2 OFFSET 2;


группировка
присоединение данных из других таблиц(join)


UPDATE = изменение существующих записей

UPDATE product SET description='крутой телефон от XIAOMI' WHERE id = 5;

UPDATE product SET price = price - '10000'; - если WHERE не указывать то обновляется все записи 

UPDATE product SET price = price - '1000' WHERE title ILIKE '%Apple%'; - обновление цены где в имени определенная строка 

UpdATE product SET description = 'акция', price = price - '1000' WHERE id IN (2, 5);
обновленик двух полей сразу по айди

DELETE - удаление записи

 deLETE FROM product WHERE title ILIKE '%xiaomi%'; - удаление по условию если в поле title содержится строка xiaomi
 DelEte FROM product WHERE id = 1; удаление записи по айди
 DELEtE FrOM product; -  удалить все записи 



Связи между таблицами и виды связей
 
Связь между таблицами - это когда значение поля в одной таблице является записью в другой таьлице

Типы связей:
1. Один к одному 

человек - паспорт (человек имеет только один паспорт, паспорт выдается только одному лицу)

2. Один ко многим 

категория - товары(товары могут иметь одну категорию, в одной категории может быть много товаров)

3. Много ко многим 

книги - авторы(один человек может написать много книг, книга может иметь много авторов)

продукты - заказы (в одном заказе может быть много продуктов, один и тот же заказ может быть во многих заказах)



 ALTER TABLE passport ADD CONstRAINT passport_person_unique UNIQUE(person_id);

SELECT pp.purchase, pr.title, pp.quantity, pr.price, (pr.price * pp.quantity) AS total FROM purchase_product AS pp JOIN product AS pr ON pr.id = pp.product;

SELECT pp.purchase, pr.title, pp.quantity, pr.price FROM purchase_product AS pp JOIN product AS pr ON pr.id = pp.product;

ALTER TABLE category ADD COLUMN parent VARCHAR(50) NULL, ADD CONSTRAINT fk_category_parent FOREIGN KEY (parent) REFERENCES category(slug);

SELECT cat.title, cat.slug, parent.title AS p FROM category AS cat JOIN category AS parent ON cat.parent = parent.slug;

