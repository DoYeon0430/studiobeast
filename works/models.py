from django.db import models

class Works(models.Model):
    CONDITION_CHOICES = [
        ('continue_ott', 'Continue_ott'),
        ('continue_movie', 'Continue_movie'),
        ('contents', 'Contents'),
    ]

    subject = models.CharField(max_length=100)
    number = models.IntegerField()
    making = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    produce = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    create_date = models.CharField(max_length=100)
    content = models.CharField(max_length=130)
    photo = models.ImageField(upload_to='works/')
    condition = models.CharField(max_length=100, choices=CONDITION_CHOICES)

    def __str__(self):
        return self.subject
