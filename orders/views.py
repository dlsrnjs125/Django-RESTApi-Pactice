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
    # 요청 데이터에서 user_id와 book_id를 받아오기
    user_id = request.data.get('user_id')
    book_id = request.data.get('book_id')

    if not user_id or not book_id:
        return Response({"error": "User ID and Book ID are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # 사용자와 책을 가져오기
        user = get_object_or_404(Users, id=user_id)
        book = get_object_or_404(Books, id=book_id)

        # 주소와 가격을 받기
        address = request.data.get('address')
        total_price = request.data.get('total_price')

        # 주소와 가격이 없으면 에러 반환
        if not address or not total_price:
            return Response({"error": "Address and Total Price are required"}, status=status.HTTP_400_BAD_REQUEST)

        # 주문 생성
        order = Orders.objects.create(user=user, book=book, address=address, total_price=total_price)

        # 생성된 주문에 대한 응답 반환
        serializer = OrdersSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Users.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
    except Books.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_orders_by_user(request, user_id):
    # 사용자의 주문 목록 조회
    orders = Orders.objects.filter(user_id=user_id)
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_orders_by_book(request, book_id):
    # 책의 주문 목록 조회
    orders = Orders.objects.filter(book_id=book_id)
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
