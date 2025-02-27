from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('books/', include('book.urls')),
   path('users/', include('users.urls')),
   path('orders/', include('orders.urls')),
]
