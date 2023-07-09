from django.db import models

class Works(models.Model):
    CONDITION_CHOICES = [
        ('continue_ott', 'Continue_ott'),
        ('continue_movie', 'Continue_movie'),
        ('contents', 'Contents'),
    ]

    subject = models.CharField(max_length=100, verbose_name='제목')
    making = models.CharField(max_length=100, verbose_name='기획 / 제작')
    director = models.CharField(max_length=100, verbose_name='감독')
    produce = models.CharField(max_length=100, verbose_name='프로듀서')
    actor = models.CharField(max_length=100, verbose_name='주연')
    create_date = models.CharField(max_length=100, verbose_name='개봉일')
    content = models.CharField(max_length=130, verbose_name='줄거리')
    photo = models.ImageField(upload_to='works/', verbose_name='포스터')
    condition = models.CharField(max_length=100, choices=CONDITION_CHOICES, verbose_name='장르')
    number = models.IntegerField(verbose_name='배치 순서')

    def __str__(self):
        return self.subject

