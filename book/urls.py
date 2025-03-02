from django.urls import path
from . import views

app_name = 'books'  # alias 설정

urlpatterns = [
    # 모든 책 조회
    path('', views.get_all_books, name='get_all_books'),
    # 책 생성
    path('create/', views.create_book, name='create_book'),
    # ID로 사용자 조회
    path('<int:id>/', views.get_book_by_id, name='get_book_by_id'),
    # title, author, publisher, price(특정 가격 이상)으로 조회
    path('search/<str:search_field>/<str:search_value>/', views.search_books, name='search_books'),
    # 책 삭제
    path('delete/<int:id>/', views.delete_book_by_id, name='delete_book_by_id'),
    # 주문 API 추가
    path('order/<int:id>/', views.order_book, name='order_book'),
]