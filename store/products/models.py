from django.db import models
from users.models import User
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'  # отображение в админне
        verbose_name_plural = 'Категории'   # отображение в админне в множине

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'  # отображение в админне
        verbose_name_plural = 'Продукты'  # отображение в админне в множине

    def __str__(self):
        return f"Название - {self.name} | Категория - {self.category.name}"

    def create_stripe_product_price(self): # для добавления товаров на страйп
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'],
            unit_amount=round(self.price * 100),
            currency='UAH'
        )
        return stripe_product_price

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.stripe_product_price_id:
            stripe_response = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_response['id']
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class BasketQuerySet(models.QuerySet):  # дополняем методами менеджер
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()  # указуем что используем его как менеджер вместо object.

    def __str__(self):
        return f"Корзина для {self.user.email} | Продукт {self.product.name}"

    def sum(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = 'Корзина'  # отображение в админне
        verbose_name_plural = 'Корзины'  # отображение в админне в множине
