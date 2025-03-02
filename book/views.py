from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Books
from .serializers import BooksSerializer

# 모든 책 조회
@api_view(['GET'])
def get_all_books(request):
   books = Books.objects.all()
   serializer = BooksSerializer(books, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

# 책 생성 (기본 재고 설정)
@api_view(['POST'])
def create_book(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        # 사용자가 재고를 입력하지 않으면 기본값(0)으로 설정
        if 'stock' not in serializer.validated_data:
            serializer.validated_data['stock'] = 10  # 기본 재고 설정
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 책 주문
@api_view(['POST'])
def order_book(request, id):
    try:
        book = Books.objects.get(id=id)
        quantity = request.data.get("quantity", 1)  # 주문 수량, 기본값 1

        if book.stock >= quantity:
            book.stock -= quantity  # 재고 감소
            book.save()
            return Response(
                {"message": f"{quantity} copies of '{book.title}' ordered successfully."},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Not enough stock available."},
                status=status.HTTP_400_BAD_REQUEST
            )
    except Books.DoesNotExist:
        return Response(
            {"error": "Book not found."},
            status=status.HTTP_404_NOT_FOUND
        )

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

# 책 삭제
@api_view(['DELETE'])
def delete_book_by_id(request, id):
   try:
       book = Books.objects.get(id=id)
       book.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   except Books.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)


