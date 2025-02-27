from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Orders
from .serializers import OrdersSerializer
from rest_framework.exceptions import NotFound

# 모든 주문 조회
@api_view(['GET'])
def get_all_orders(request):
   orders = Orders.objects.all()
   serializer = OrdersSerializer(orders, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 주문 생성
@api_view(['POST'])
def create_order(request):
   serializer = OrdersSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 사용자 이름으로 주문 조회
@api_view(['GET'])
def get_orders_by_user(request, user):
    try:
        orders = Orders.objects.filter(user__name=user)
        if not orders:
            raise NotFound(detail="주문을 찾을 수 없습니다.")
    except NotFound:
        return Response({"detail": "사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

# 책 제목으로 주문 조회
@api_view(['GET'])
def get_orders_by_book(request, book):
    try:
        orders = Orders.objects.filter(book__title=book)
        if not orders:
            raise NotFound(detail="주문을 찾을 수 없습니다.")
    except NotFound:
        return Response({"detail": "책을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

# 주문 삭제
@api_view(['DELETE'])
def delete_order_by_id(request, id):
    try:
        order = Orders.objects.get(id=id)
        order.delete()  # 주문 삭제
        return Response({"detail": "주문이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
    except Orders.DoesNotExist:
        return Response({"detail": "주문을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
