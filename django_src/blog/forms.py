from django import forms
from .models import Post, Comment

# Validator 함수 정의
# title 입력필드의 길이 체크 < 3
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('title은 3글자 이상 입력해 주세요!')

# PostForm class declaration
class PostForm(forms.Form):
    # title = forms.CharField()
    title = forms.CharField(validators=[min_length_3_validator])
    text = forms.CharField(widget=forms.Textarea)

# ModelForm을 상속받는 PostModelForm class declaration
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', )

# ModelForm을 상속받는 CommentModelForm class declaration
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', )