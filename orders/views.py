from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Orders
from .serializers import OrdersSerializer
from users.models import Users
from book.models import Books


@api_view(['GET'])
def get_all_orders(request):
    orders = Orders.objects.all()
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_order(request):
    user_id = request.data.get('user_id')
    book_id = request.data.get('book_id')
    quantity = request.data.get('quantity', 1)  # 기본 수량 1
    address = request.data.get('address')

    if not user_id or not book_id or not address:
        return Response({"error": "User ID, Book ID, and Address are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = get_object_or_404(Users, id=user_id)
        book = get_object_or_404(Books, id=book_id)

        quantity = max(1, int(quantity))  # 최소 1 이상 보장
        total_price = book.price * quantity  # 총 가격 자동 계산

        order = Orders.objects.create(user=user, book=book, address=address, quantity=quantity, total_price=total_price)

        serializer = OrdersSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except (Users.DoesNotExist, Books.DoesNotExist):
        return Response({"error": "User or Book not found"}, status=status.HTTP_400_BAD_REQUEST)

# user_id, user_name, book_id, book_title 로 조회 가능하도록 수정
@api_view(['GET'])
def search_orders(request, search_field, search_value):
    if search_field == "user_id":
        orders = Orders.objects.filter(user__id=search_value)
    elif search_field == "user_name":
        orders = Orders.objects.filter(user__name__icontains=search_value)
    elif search_field == "book_id":
        orders = Orders.objects.filter(book__id=search_value)
    elif search_field == "book_title":
        orders = Orders.objects.filter(book__title__icontains=search_value)
    else:
        return Response({"error": "Invalid search field"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_order_by_id(request, order_id):
    try:
        # 주문을 삭제
        order = Orders.objects.get(id=order_id)
        order.delete()
        return Response({"message": "Order deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Orders.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
