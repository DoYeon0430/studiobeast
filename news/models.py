from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    subject = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = HTMLField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject