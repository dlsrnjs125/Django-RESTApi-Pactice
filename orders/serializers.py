from rest_framework import serializers
from .models import Orders
from .models import Books
from .models import Users

class OrdersSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=Users.objects.all())
    book_id = serializers.PrimaryKeyRelatedField(source='book', queryset=Books.objects.all())

    class Meta:
       model = Orders
       fields = ['id', 'user_id', 'book_id', 'address', 'price']