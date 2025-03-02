from django.urls import path
from . import views

app_name = 'users'  # alias 설정

urlpatterns = [
    # 모든 사용자 조회
    path('', views.get_all_users, name='get_all_users'),
    # 사용자 생성
    path('create/', views.create_user, name='create_user'),
    # ID로 사용자 조회
    path('<int:id>/', views.get_user_by_id, name='get_user_by_id'),
    # name, email, age(특정 나이 이상)으로 조회
    path('search/<str:search_field>/<str:search_value>/', views.search_users, name='search_users'),
    # 사용자 삭제
    path('delete/<int:id>/', views.delete_user_by_id, name='delete_user_by_id'),
]
