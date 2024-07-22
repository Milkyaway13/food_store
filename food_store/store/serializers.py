from rest_framework import serializers

from .models import Cart, CartItem, Category, Product, SubCategory


class AddProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["id", "name", "slug", "image"]


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "image", "subcategories"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["name", "slug", "category", "price", "images"]

    def get_images(self, obj):
        return [
            obj.image_small.url if obj.image_small else None,
            obj.image_medium.url if obj.image_medium else None,
            obj.image_large.url if obj.image_large else None,
        ]


class RemoveProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source="cartitem_set", many=True)
    total_cart_value = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["user_name", "items", "total_cart_value", "total_quantity"]

    def get_total_cart_value(self, obj):
        return sum(
            item.quantity * item.product.price
            for item in obj.cartitem_set.all()
        )

    def get_total_quantity(self, obj):
        return sum(item.quantity for item in obj.cartitem_set.all())

    def get_user_name(self, obj):
        return obj.user.username


class CartDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    product_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["product", "quantity", "product_price", "total_price"]

    def get_product_price(self, obj):
        return str(obj.product.price)

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price
