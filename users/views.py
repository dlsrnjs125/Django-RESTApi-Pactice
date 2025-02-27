from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Users
from .serializers import UsersSerializer

# 모든 사용자 조회
@api_view(['GET'])
def get_all_users(request):
   users = Users.objects.all()
   serializer = UsersSerializer(users, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자 생성
@api_view(['POST'])
def create_user(request):
   serializer = UsersSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ID로 사용자 조회
@api_view(['GET'])
def get_user_by_id(request, id):
   try:
       user = Users.objects.get(id=id)
       serializer = UsersSerializer(user)
       return Response(serializer.data, status=status.HTTP_200_OK)
   except Users.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

# 사용자 이름으로 조회
@api_view(['GET'])
def get_users_by_name(request, name):
   users = Users.objects.filter(name=name)
   serializer = UsersSerializer(users, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 특정 나이 이상의 사용자 조회
@api_view(['GET'])
def get_users_by_age_gte(request, age):
   users = Users.objects.filter(age__gte=age) # gte : 크거나 같다
   serializer = UsersSerializer(users, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자 삭제
@api_view(['DELETE'])
def delete_user_by_id(request, id):
   try:
       user = Users.objects.get(id=id)
       user.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   except Users.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)


