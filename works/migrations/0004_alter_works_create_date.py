# Generated by Django 4.2.2 on 2023-06-30 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_works_produce_alter_works_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='create_date',
            field=models.CharField(max_length=100),
        ),
    ]
