from django import forms

from products.models import Product, Hashtag
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
    