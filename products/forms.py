from django import forms

from products.models import Product, Hashtag
# from products.models import Comment
#model form은 모델을 참고하여 모델 필드를 보고 form을 생성한다.
#product:제목, 내용, 생성시간, 바뀐시간 -> form: 제목, 내용 
class ProductForm(forms.ModelForm):
    hashtags = forms.CharField(max_length=20, help_text='#을 입력 후 한 칸을 띄고 입력하세요. 입력 예시: #해시태그 #해시')

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("author","like_users","views","hashtags",)

    def clean_hashtags(self):
        # 해시태그 유효성 검사
        hashtags = self.cleaned_data.get('hashtags').split(' ')
        seen = set()
        for name in hashtags:
            name = name.strip()
            if ' ' in name or any(char in '!@$%^&*()[]{};:,.<>?/~`"' for char in name):
                raise forms.ValidationError("해시태그는 띄어쓰기와 특수문자가 허용되지 않습니다.")
            if name[0] != '#':
                raise forms.ValidationError("해시태그는 #으로 시작해야 합니다.")
            if name in seen:
                raise forms.ValidationError("해시태그는 중복될 수 없습니다.")
            seen.add(name)
        return hashtags
    
#그냥 위 productform에다가 합쳐버릴수는 없나...?
# class HashtagForm(forms.ModelForm):
#     class Meta:
#         Model = Hashtag
#         fields = "__all__"
    
#     def clean_hashtag(self):
#         name = self.cleaned_data.get('name') #cleaned_data: 적절한 데이터로 판명될 시 name에 저장

#         if Hashtag.objects.filter(name=name).exists():
#             raise forms.ValidationError("각 게시물은 중복된 해시태그를 설정할 수 없습니다.")

#         if ' ' in name or any(char in '!@#$%^&*()[]{};:,.<>?/~`"' for char in name):
#             raise forms.ValidationError("해시태그는 띄어쓰기와 특수문자가 허용되지 않습니다.")

#         return name

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = "__all__"
#         exclude = ("product","user",)