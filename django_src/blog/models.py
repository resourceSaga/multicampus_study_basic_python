from django.db import models
from django.utils import timezone
from django import forms

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('제목은 3글자 이상 입력해 주세요!')


class Post(models.Model):
    # author
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # title
    title = models.CharField(max_length=200, validators=[min_length_3_validator])
    # detail
    text = models.TextField()
    # write day
    created_data = models.DateTimeField(default=timezone.now)
    # publish day
    published_date = models.DateTimeField(blank=True, null=True)
    # tmp field
    # test = models.TextField()

    # current time set publish date
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # return title instead obj address
    def __str__(self):
        return self.title