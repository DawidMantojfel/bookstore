# Generated by Django 3.1.5 on 2021-01-10 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('rate', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('condition', models.CharField(choices=[('bad', 'bad'), ('used', 'used'), ('new', 'new')], max_length=4)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sold', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.CharField(max_length=2000)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Market.book')),
            ],
        ),
    ]
