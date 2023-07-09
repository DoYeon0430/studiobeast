from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    subject = models.CharField(max_length=100, verbose_name='제목')
    author = models.CharField(max_length=50, verbose_name='글쓴이')
    content = HTMLField(verbose_name='내용')
    create_date = models.DateTimeField(verbose_name='작성일')

    def __str__(self):
        return self.subject