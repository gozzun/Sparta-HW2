from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product

# 확장성을 위해 custom user 모델 작성
class User(AbstractUser):
    following = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False #팔로워는 대칭 관계가 아님.
    )
    image = models.ImageField(upload_to="images/", blank=True) #이미지 추가
    created_at = models.DateTimeField(auto_now_add=True)
