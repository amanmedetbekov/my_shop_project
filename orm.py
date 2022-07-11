"""SELECT"""

# SELECT * FROM product;
# Product.objects.all()
#
# 
# SELECT name, price FROM   product;
# Product.objects.only(name, price)
#  
#  
# SELECT * FROM product WHERE условие;
# Product.objects.filter(условие)

"сравнения"
            # ==
            # SELECT * FROM product WHERE category_id = 'tv';
            # Product.object.filter(category_id='tv')


            # !=
            # SELECT * FROM product WHERE Not category_id = 'tv';
            # Product.object.filter(~Q(category_id='tv'))
            # Product.object.exclude(category_id='tv')


            # >
            # SELECT * FROM product WHERE price > 30000;
            # Product.object.filter(price__gt=30000)


            # <
            # SELECT * FROM product WHERE price > 30000;
            # Product.object.filter(price__lt=30000)

            # >=
            # SELECT * FROM product WHERE price > 30000;
            # Product.object.filter(price__gte=30000)

            # <=
            # SELECT * FROM product WHERE price > 30000;
            # Product.object.filter(price__lte=30000)




"IN"
    # SELECT * FROM product WHERE category_id IN ('tv', 'smartphones');
    # Product.object.filter(category_id__in=['tv', 'smartphones'])



"BETWEEN"
    # SELECT * FROM products WHERE price BETWEEN 40000 AND 50000;
    # Product.object.filter(price__range=[40000, 50000])



"LIKE ILIKE"
'str'
    # SELECT * FROM products WHERE name LIKE 'Apple Iphone 13';
    # Product.object.filter(name__exact='Apple Iphone 13')


    # SELECT * FROM products WHERE name ILIKE 'Apple Iphone 13';
    # Product.object.filter(name__iexact='Apple Iphone 13')



'str%'
    # SELECT * FROM products WHERE name LIKE 'Apple%';
    # Product.object.filter(name__startswith='Apple')

    # SELECT * FROM products WHERE name ILIKE 'Apple%';
    # Product.object.filter(name__istartswith='Apple')



'%str'
    # SELECT * FROM products WHERE name LIKE '%Apple';
    # Product.object.filter(name__endswith='Apple')

    # SELECT * FROM products WHERE name ILIKE '%Apple';
    # Product.object.filter(name__iendswith='Apple')


'%str%'
    # SELECT * FROM products WHERE name LIKE '%Apple%';
    # Product.object.filter(name__contains='Apple')

    # SELECT * FROM products WHERE name ILIKE '%Apple%';
    # Product.object.filter(name__icontains='Apple')


"ORDER BY"
# SELECT * FROM producr ORDER BY price ASC;
# Product.object.order_by('price')

# SELECT * FROM producr ORDER BY price DESC;
# Product.object.order_by('-price')


"LIMIT"
# SELECT * FROM product LIMIT 10;
# Product.object.all()[:10]

# SELECT * FROM product LIMIT 10 OFFSET 5;
# Product.object.all()[5:10]

 



"""INSERT"""
'одна запись'
# INSERT INTO product (name, description, category, price, image) VALUES('name', 'description', 'category', 'price', 'image');
# Product.objects.create(name= '...', description='...' и тд)

'еще один метод'
# product = Product(name='...', description='...' и тд)
# product.save()

'несколько записей'
# INSERT INTO product (fields) VALUSE ('name', 'description', 'category', 'price', 'image'), ('name', 'description', 'category', 'price', 'image');
# Poduct.objects.bulk_create([Product(...), Product(...)])






"""UPDATE"""
# UPDATE product SET price = 50000;
# Poduct.objects.update(price=50000)

'выборочное обновление записей'
# UPDATE product SET price = 50000 WHERE category_id = 'notebooks';
# Poduct.objects.filter(category_id='notebooks').update(price=50000)






"""DELETE"""
# DELETE FROM product;
# Product.objects.delete()

'выборочное удаление записей'
# DELETE FROM product WHERE price > 50000;
# Product.objects.filter(price__gt=50000).delete()



"""Получение одного объекта"""
# Category.object.get(slug='tv')
# Product.objects.get(id=2)


'исключения'
# DoesNotExist, MultipleObjectsReturned





'количество записей'
# SELECT COUNT(*) FROM product;
# Product.objects.count()


# SELECT COUNT(*) FROM product WHERE price < 20000;
# Product.objects.filter(price__lt=20000).count()