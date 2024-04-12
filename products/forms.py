from django import forms

from products.models import Product
# from products.models import Comment
#model form은 모델을 참고하여 모델 필드를 보고 form을 생성한다.
#product:제목, 내용, 생성시간, 바뀐시간 -> form: 제목, 내용 
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("author","like_users",)

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = "__all__"
#         exclude = ("product","user",)