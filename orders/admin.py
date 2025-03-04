from django.contrib import admin
from .models import Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'address', 'total_price', 'created_at')

    # user_id와 book_id를 출력하고 싶다면
    def user_id(self, obj):
        return obj.user.id

    user_id.admin_order_field = 'user'  # 정렬 필드 지정
    user_id.short_description = 'User ID'  # 컬럼 제목 설정

    def book_id(self, obj):
        return obj.book.id

    book_id.admin_order_field = 'book'  # 정렬 필드 지정
    book_id.short_description = 'Book ID'  # 컬럼 제목 설정

    # list_display에 user_id와 book_id를 추가
    list_display = ('user_id', 'book_id', 'address', 'total_price', 'created_at')
