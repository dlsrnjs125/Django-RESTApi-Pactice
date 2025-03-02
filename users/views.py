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

@api_view(['GET'])
def search_users(request, search_field, search_value):
    if search_field == 'name':
        users = Users.objects.filter(name__icontains=search_value)  # 부분 검색 가능
    elif search_field == 'email':
        users = Users.objects.filter(email__icontains=search_value)
    elif search_field == 'age':
        try:
            age_value = int(search_value)
            users = Users.objects.filter(age__gte=age_value)  # 특정 나이 이상 검색
        except ValueError:
            return Response({"error": "Invalid age value"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Invalid search field"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# ID로 사용자 조회
@api_view(['GET'])
def get_user_by_id(request, id):
   try:
       user = Users.objects.get(id=id)
       serializer = UsersSerializer(user)
       return Response(serializer.data, status=status.HTTP_200_OK)
   except Users.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

# 사용자 삭제
@api_view(['DELETE'])
def delete_user_by_id(request, id):
   try:
       user = Users.objects.get(id=id)
       user.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   except Users.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)


