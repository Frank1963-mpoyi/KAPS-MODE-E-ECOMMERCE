import random

from django.conf                                            import settings
from django.db.models                                       import Q

from kapshop.common                                          import process as process_common
from kapshop.apps.db.products.products.models                import Product


#MEDIA_PATH = settings.KAPS_DIR

def get_products(i):

    products = Product.objects \
        .exclude(
            Q(bool_deleted = True)
        ) \
        .select_related('category', 'subcategory', 'color',  'size').order_by('title')

    return products


def get_product(i):

    products = get_products(i)

    product = None
    if i.get('item_name'):
        product = get_products(i).filter(Q(slug = i['item_name'])).first()

    if product:
        if product.image:
            product.image = product.image.url

        product.discount_amount = process_common.process_discount_prices(product.price, product.discount_price)

    return product


# def get_first_product(i):
#
#     product = get_products(i).first()
#
#     if product:
#         if product.image:
#             product.image = product.image.url
#
#         product.discount_amount = process_common.process_discount_prices(product.price, product.discount_price)
#
#     return product

#
# def get_products_by_category(products):
#
#     products_mens   = []
#     products_womens = []
#     products_bags   = []
#     products_shoes  = []
#
#     for product in products:
#
#         if product.image:
#             product.image = product.image.url
#
#         product.discount_amount = process_common.process_discount_prices(product.price, product.discount_price)
#
#         if str(product.category_id) == 'fa6d7ef4-0612-491d-ac66-257d3a16aa36':
#             products_mens.append(product)
#
#         if str(product.category_id) == '03a902c6-8fad-41db-b1a3-ca9801162f0c':
#             products_womens.append(product)
#
#         if str(product.category_id) == 'eb1d30c5-6a4c-4816-a448-d6e6e1341e1e':
#             products_bags.append(product)
#
#         if str(product.category_id) == '15d094c1-b9e5-46ac-88b3-a23e42d5b976':
#             products_shoes.append(product)
#
#     if len(products_mens) > 4:
#         products_mens = random.sample(products_mens, 4)
#     if len(products_womens) > 4:
#         products_womens = random.sample(products_womens, 4)
#     if len(products_bags) > 4:
#         products_bags = random.sample(products_bags, 4)
#     if len(products_shoes) > 4:
#         products_shoes = random.sample(products_shoes, 4)
#
#     return products_mens, products_womens, products_bags, products_shoes
