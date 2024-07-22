from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("Слаг", unique=True)
    image = models.ImageField("Фото", upload_to="images/categories/")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("Слаг", unique=True)
    image = models.ImageField("Фото", upload_to="images/subcategories/")

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(
        SubCategory,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Подкатегория",
    )
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("Слаг", unique=True)
    image_small = models.ImageField(
        "Маленькое фото", upload_to="images/products/small/"
    )
    image_medium = models.ImageField(
        "Среднее фото", upload_to="images/products/medium/"
    )
    image_large = models.ImageField(
        "Большое фото", upload_to="images/products/large/"
    )
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)

    def __str__(self):
        return self.name

    @property
    def category(self):
        return self.subcategory.category


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    products = models.ManyToManyField(
        Product, through="CartItem", verbose_name="Продукты"
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        ordering = ("user",)

    def __str__(self):
        return f"Корзина пользователя {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, verbose_name="Корзина"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    quantity = models.PositiveIntegerField("Количество")

    class Meta:
        verbose_name = "Продукт в корзине"
        verbose_name_plural = "Продукты в корзине"
        ordering = ("product",)

    def __str__(self):
        return f"Продукт - {self.product.name}, продукт - {self.quantity}"
