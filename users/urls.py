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
    # 사용자 이름으로 조회
    path('name/<str:name>/', views.get_users_by_name, name='get_users_by_name'),
    # 특정 나이 이상의 사용자 조회
    path('age_gte/<int:age>/', views.get_users_by_age_gte, name='get_users_by_age_gte'),
    # 사용자 삭제
    path('delete/<int:id>/', views.delete_user_by_id, name='delete_user_by_id'),
]
