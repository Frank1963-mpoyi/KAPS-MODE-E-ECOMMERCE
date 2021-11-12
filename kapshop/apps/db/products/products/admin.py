from django.contrib import admin

from .models import Product
from kapshop.apps.db.products.sizes.models import Size
from kapshop.apps.db.products.colors.models import Color
from kapshop.apps.db.products.categories.models import Category
from kapshop.apps.db.accounting.orders.models import Order
from kapshop.apps.db.accounting.orderitems.models import OrderItem
from kapshop.apps.db.kaps_admins.models import KapsAdmin
# Register your models here.


admin.site.register([Product, Size, Color,  Category, Order, OrderItem, KapsAdmin])