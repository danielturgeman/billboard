from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField()


    def __str__(self):
        return "{0} - {1}".format(self.title, self.id)
