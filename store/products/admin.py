from django.contrib import admin

# Register your models here.
from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)  # указуем с какой моделью работаем
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # дает возможность видеть поля при выборе таблицы
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')  # улучшает вид при выборе товара
    readonly_fields = ('description', )  # неизменяемое поле
    search_fields = ('name',)  # поле для поиска
    ordering = ('name', )  # поле для стандартного отображения товаров по алфавитному порядку


class BasketAdmin(admin.TabularInline):  # для отображении корзины у филдах юзера как бы
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp', )
    extra = 0
