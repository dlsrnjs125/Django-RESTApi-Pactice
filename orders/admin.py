from django.contrib import admin
from .models import Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'book_id', 'book_title', 'address', 'quantity', 'total_price', 'created_at')

    def user_id(self, obj):
        return obj.user.id
    user_id.admin_order_field = 'user'  # 정렬 필드 지정
    user_id.short_description = 'User ID'  # 컬럼 제목 설정

    def user_name(self, obj):
        return obj.user.name  # user 모델의 name 필드 사용
    user_name.admin_order_field = 'user__name'  # 정렬 필드 지정
    user_name.short_description = 'User Name'  # 컬럼 제목 설정

    def book_id(self, obj):
        return obj.book.id
    book_id.admin_order_field = 'book'  # 정렬 필드 지정
    book_id.short_description = 'Book ID'  # 컬럼 제목 설정

    def book_title(self, obj):
        return obj.book.title  # book 모델의 title 필드 사용
    book_title.admin_order_field = 'book__title'  # 정렬 필드 지정
    book_title.short_description = 'Book Title'  # 컬럼 제목 설정

