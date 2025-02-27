from django.db import models
from users.models import Users # users 모델 가져오기
from book.models import Books # books 모델 가져오기

class Orders(models.Model): # 상속 : models.Model
   user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='User')
   book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='Book')
   address = models.CharField(max_length=255, verbose_name='Address')
   price = models.IntegerField(verbose_name="Price")

   def __str__(self):
       return f"Order: {self.user.name} -> {self.book.title}"

   class Meta:
       db_table = 'Orders'  # 테이블 이름을 'Orders'로 설정
