from django.db import models
from users.models import Users  # users 모델 가져오기
from book.models import Books  # books 모델 가져오기

class Orders(models.Model):
   user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='User')
   book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='Book')
   address = models.CharField(max_length=255, verbose_name='Address')
   quantity = models.PositiveIntegerField(default= 1, verbose_name='Quantity') # 주문 수량
   total_price = models.IntegerField(verbose_name="Total_Price")
   created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")  # 주문 생성 시간

   def __str__(self):
       return f"Order: {self.user.name} ordered '{self.book.title}' for {self.total_price} at {self.created_at}"

   def save(self, *args, **kwargs):
       # total_price 자동 계산
       self.total_price = self.book.price * self.quantity
       super().save(*args, **kwargs)

   class Meta:
       db_table = 'orders'  # 테이블 이름을 명시적으로 'orders'로 설정
       ordering = ['-created_at']  # 최신 주문이 먼저 보이도록 설정