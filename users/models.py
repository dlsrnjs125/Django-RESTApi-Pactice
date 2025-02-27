from django.db import models

class Users(models.Model):
   name = models.CharField(max_length=50, verbose_name='User Name')
   email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
   age = models.IntegerField(verbose_name='Age')

   def __str__(self):
       return self.name
   class Meta:
       db_table = 'users' # 테이블 이름을 'users'로 설정