# Generated by Django 3.1.5 on 2021-01-21 23:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Market', '0010_auto_20210121_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(default='static/images/default.jpg', upload_to='')),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('price', models.FloatField()),
                ('condition', models.CharField(choices=[('bad', 'bad'), ('used', 'used'), ('new', 'new')], max_length=4)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('sold', models.BooleanField(default=False)),
                ('rate', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='market',
            name='user',
        ),
        migrations.RemoveField(
            model_name='opinion',
            name='book',
        ),
        migrations.RemoveField(
            model_name='order',
            name='book',
        ),
        migrations.AddField(
            model_name='opinion',
            name='content',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Market',
        ),
        migrations.AddField(
            model_name='opinion',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Market.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.product'),
        ),
    ]