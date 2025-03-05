from django.urls import path
from . import views

app_name = 'orders'  # alias 설정

urlpatterns = [
    # 모든 주문 조회
    path('', views.get_all_orders, name='get_all_orders'),
    # 주문 생성 (user 와 book 정보를 받아서 주문 생성)
    path('create/', views.create_order, name='create_order'),
    # user_id, user_name, book_id, book_title 로 조회 가능하도록 수정
    path('search/<str:search_field>/<str:search_value>/', views.search_orders, name='search_orders'),
    # 주문 삭제
    path('delete/<int:order_id>/', views.delete_order_by_id, name='delete_order_by_id'),
]
