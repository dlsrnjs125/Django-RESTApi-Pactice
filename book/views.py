from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Books
from .serializers import BooksSerializer

# 모든 책 조회
@api_view(['GET'])
def get_all_books(request):
   books = Books.objects.all()
   serializer = BooksSerializer(books, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 책 생성
@api_view(['POST'])
def create_book(request):
   serializer = BooksSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ID로 사용자 조회
@api_view(['GET'])
def get_book_by_id(request, id):
   try:
       user = Books.objects.get(id=id)
       serializer = BooksSerializer(user)
       return Response(serializer.data, status=status.HTTP_200_OK)
   except Books.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

# 책 제목으로 조회
@api_view(['GET'])
def get_books_by_title(request, title):
   books = Books.objects.filter(title=title)
   serializer = BooksSerializer(books, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 작가 이름으로 조회
@api_view(['GET'])
def get_books_by_author(request, author):
   books = Books.objects.filter(author=author)
   serializer = BooksSerializer(books, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 출판사 이름으로 조회
@api_view(['GET'])
def get_books_by_publisher(request, publisher ):
   books = Books.objects.filter(publisher=publisher)
   serializer = BooksSerializer(books, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 특정 가격 이상의 책 조회
@api_view(['GET'])
def get_books_by_price_gte(request, price):
   users = Books.objects.filter(price__gte=price) # gte : 크거나 같다
   serializer = BooksSerializer(users, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 책 삭제
@api_view(['DELETE'])
def delete_book_by_id(request, id):
   try:
       book = Books.objects.get(id=id)
       book.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   except Books.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)


