from django.urls import path

from apis import views


urlpatterns = [
    path('', views.BookAPIView.as_view(), name='book_list'),
]