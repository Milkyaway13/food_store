from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from store.models import Cart, CartItem, Category, Product, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "image")
    search_fields = ("name", "slug")


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "category", "image")
    list_filter = ("category",)
    search_fields = ("name", "slug", "category__name")


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "subcategory",
        "price",
        "image_small",
        "image_medium",
        "image_large",
    )
    list_filter = ("subcategory",)
    search_fields = ("name", "slug", "subcategory__name")
    list_per_page = 20


class CartAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username",)


class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "cart",
        "product",
        "quantity",
        "product_price",
        "total_price",
    )
    list_filter = ("cart", "product")
    search_fields = ("cart__user__username", "product__name")
    list_per_page = 20

    def product_price(self, obj):
        return obj.product.price

    def total_price(self, obj):
        return obj.quantity * obj.product.price

    product_price.short_description = "Цена продукта"
    total_price.short_description = "Общая стоимость"


class UserAdmin(BaseUserAdmin):
    ordering = ("username",)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("username", "email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
