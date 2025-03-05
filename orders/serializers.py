from rest_framework import serializers
from .models import Orders
from book.models import Books
from users.models import Users

class OrdersSerializer(serializers.ModelSerializer):
    # 사용자 정보를 직관적으로 반환하도록 수정
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    user_name = serializers.CharField(source='user.name')  # User 모델의 'name' 필드

    # 책 정보를 직관적으로 반환하도록 수정
    book = serializers.PrimaryKeyRelatedField(queryset=Books.objects.all())
    book_title = serializers.CharField(source='book.title')  # Books 모델의 'title' 필드

    class Meta:
        model = Orders
        fields = ['id', 'user', 'user_name', 'book', 'book_title', 'address', 'quantity', 'total_price', 'created_at']

    def get_user_name(self, obj):
        return obj.user.name  # user 모델의 username 필드 사용

    def get_book_title(self, obj):
        return obj.book.title  # book 모델의 title 필드 사용

