from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Cart, CartItem, Category, Product
from .serializers import (
    AddProductSerializer,
    CartDetailSerializer,
    CartSerializer,
    CategorySerializer,
    ProductSerializer,
    RemoveProductSerializer,
)


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]


class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Cart.objects.filter(user=self.request.user)

    def get_object(self):
        return get_object_or_404(Cart, user=self.request.user)

    @action(detail=False, methods=("post",))
    def add_product(self, request):
        serializer = AddProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        product_id = serializer.validated_data["product_id"]
        quantity = serializer.validated_data["quantity"]

        product = get_object_or_404(Product, id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={"quantity": quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response(
            {"status": "Product added to cart"}, status=status.HTTP_200_OK
        )

    @action(detail=False, methods=("post",))
    def remove_product(self, request):
        serializer = RemoveProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        product_id = serializer.validated_data["product_id"]

        cart = self.get_object()
        cart_item = get_object_or_404(
            CartItem, cart=cart, product_id=product_id
        )
        cart_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=("post",))
    def clear_cart(self, request):
        cart = Cart.objects.get(user=request.user)
        cart.cartitem_set.all().delete()
        return Response({"status": "cart cleared"})

    @action(detail=False, methods=("get",))
    def view_cart(self, request):
        cart = Cart.objects.get(user=request.user)
        serializer = CartDetailSerializer(cart)
        return Response(serializer.data)

    @action(detail=True, methods=("patch",))
    def update_quantity(self, request, pk=None):
        cart_item = get_object_or_404(CartItem, id=pk, cart__user=request.user)
        quantity = request.data.get("quantity")
        if quantity is not None and int(quantity) > 0:
            cart_item.quantity = quantity
            cart_item.save()
            return Response({"status": "quantity updated"})
        else:
            return Response(
                {"error": "Invalid quantity"},
                status=status.HTTP_400_BAD_REQUEST,
            )
