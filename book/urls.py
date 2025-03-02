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
    # 책 제목으로 조회
    path('title/<str:title>/', views.get_books_by_title, name='get_books_by_title'),
    # 작가 이름으로 조회
    path('author/<str:author>/', views.get_books_by_author, name='get_books_by_author'),
    # 출판사 이름으로 조회
    path('publisher/<str:publisher>', views.get_books_by_publisher, name='get_books_by_publisher'),
    # 책 삭제
    path('delete/<int:id>/', views.delete_book_by_id, name='delete_book_by_id'),
    # 주문 API 추가
    path('order/<int:id>/', views.order_book, name='order_book'),
]