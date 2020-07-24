from django.urls import path

from .views import (
    LikeProductView
)

urlpatterns = [
    path('/like-product', LikeProductView.as_view()),
]