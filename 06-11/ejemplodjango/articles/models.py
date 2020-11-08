from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def addComment(self):
        self.comments = self.comments + 1
        return self

    def addComments(self, count):
        self.comments = self.comments + count
        return self
