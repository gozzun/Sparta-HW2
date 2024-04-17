from django.db import models
from django.conf import settings

class Hashtag(models.Model):
    name = models.CharField(max_length=20, unique=True) #중복은 허용되지 않음.

class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_products")
    views = models.IntegerField(default=0)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    
    def __str__(self):
        return self.title
    
    def increment_views(self):
        self.views += 1
        self.save()

# class Comment(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
#     )
#     content = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.content
    