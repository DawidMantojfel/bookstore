# Generated by Django 3.1.5 on 2021-01-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0011_auto_20210122_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]