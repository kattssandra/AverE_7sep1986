БД “Продукты”

Table 1: products (Продукты)

Columns:
o	product_id (int, primary key)
o	product_name (varchar)
o	category_id (int, foreign key)
    calories (int)
o	price (decimal)

Table 2: categories (Категории)
Columns:
o	category_id (int, primary key)
o	category_name (varchar)

Table 3: Nutritional Information (Пищевая ценность)
Columns:
o	product_id (int, foreign key referencing Products)
    protein (decimal)
    carbohydrates (decimal)
    fat (decimal)
    fiber (decimal)

Связи таблиц:
•	Таблица продуктов (products) имеет внешний ключ (category_id), который связывает ее с таблицей категорий (categories). 
Это отношение указывает на категорию каждого продукта.
•	Информация о пищевой ценности имеет однозначное отношение к Продуктам, связываясь с Продуктами через внешний ключ Product_id

Составьте следующие запросы:

1.	Выведите все уникальные названия продуктов.

SELECT DISTINCT name
FROM Nutritional Information;

    2.  Выведите ид, название и стоимость продуктов с содержанием клетчатки (fiber) более 5 граммов..

SELECT products.product_name, products.product_id, products.price
FROM products
JOIN Nutritional Information ON products.product_id = Nutritional Information.product_id
WHERE Nutritional Information.fiber > 5;

3. Выведите название продукта с самым высоким содержанием белка (protein).

SELECT products.product_name
FROM products
JOIN Nutritional Information ON products.product_id = Nutritional Information.product_id
WHERE Nutritional Information.protein > 1
ORDER BY Nutritional Information.size DESC
LIMIT 1;

4. Подсчитайте общую сумму калорий для продуктов каждой категории. Выведите - id категории, сумму калорий.

SELECT c.id AS category_id, COUNT(p.calories) AS products_calories
FROM products p
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.id
ORDER BY products_calories DESC;

5.  Выведите названия всех продуктов, с калорийностью 1000, и относятся к категории “Десерт”.


SELECT products.name
FROM products
JOIN categories ON products.category_id = categories.category_id
JOIN Nutritional Information ON products.product_id = Nutritional Information.product_id
WHERE products.calories = 100 
AND categories.name = 'Десерт'
