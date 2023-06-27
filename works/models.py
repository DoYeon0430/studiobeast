from django.db import models

class Works(models.Model):
    subject = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    produce = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    content = models.CharField(max_length=130)
    photo = models.ImageField(upload_to='works/')

    def __str__(self):
        return self.subject