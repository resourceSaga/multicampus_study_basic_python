from django.db import models
from django.utils import timezone

class Post(models.Model):
    # author
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # title
    title = models.CharField(max_length=200)
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