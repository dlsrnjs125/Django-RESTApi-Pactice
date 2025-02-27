from django.urls import path
from . import views

app_name = 'orders'  # alias 설정

urlpatterns = [
    # 모든 주문 조회
    path('', views.get_all_orders, name='get_all_orders'),
    # 주문 생성
    path('create/', views.create_order, name='create_order'),
    # 사용자 이름으로 조회
    path('user/<str:user>/', views.get_orders_by_user, name='get_orders_by_user'),
    # 책 제목으로 조회
    path('book/<str:book>/', views.get_orders_by_book, name='get_orders_by_book'),
    # 주문 삭제
    path('delete/<int:id>/', views.delete_order_by_id, name='delete_order_by_id'),
]