from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product

# 확장성을 위해 custom user 모델 작성
class User(AbstractUser):
    following = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False #팔로워는 대칭 관계가 아님.
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="created_by")
    # like_products = models.ManyToManyField(Product, related_name="liked_by")