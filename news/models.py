from django.db import models

class News(models.Model):
    subject = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject