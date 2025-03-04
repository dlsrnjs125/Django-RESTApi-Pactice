from rest_framework import serializers
from .models import Orders
from book.models import Books
from users.models import Users

class OrdersSerializer(serializers.ModelSerializer):
    # 사용자 정보를 직관적으로 반환하도록 수정
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    # 책 정보를 직관적으로 반환하도록 수정
    book = serializers.PrimaryKeyRelatedField(queryset=Books.objects.all())

    class Meta:
        model = Orders
        fields = ['id', 'user', 'book', 'address', 'total_price', 'created_at']
