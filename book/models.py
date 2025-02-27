from django.db import models

class Books(models.Model): # 상속 : models.Model
   title = models.CharField(max_length=100, verbose_name='Title')
   author = models.CharField(max_length=50, verbose_name='Author')
   publisher = models.CharField(max_length=50, verbose_name='Publisher')
   price = models.IntegerField(verbose_name="Price")

   def __str__(self):
       return self.title

   class Meta:
       db_table = 'Books'  # 테이블 이름을 'Books'로 설정
