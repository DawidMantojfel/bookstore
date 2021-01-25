# Generated by Django 3.1.5 on 2021-01-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0008_auto_20210120_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='book',
        ),
        migrations.AddField(
            model_name='market',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='image',
            field=models.ImageField(default='static/images/default.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='market',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]