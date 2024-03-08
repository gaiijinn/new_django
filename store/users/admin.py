from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from users.models import User


admin.site.register(User)
=======

from users.models import User
from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin, )

>>>>>>> after_pause
