# Generated by Django 4.2.8 on 2024-01-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='url')),
                ('content', models.TextField(verbose_name='Контент')),
                ('image', models.ImageField(upload_to='material/', verbose_name='изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('publication', models.CharField(default=True, verbose_name='признак публикации')),
                ('count', models.IntegerField(default=0, verbose_name='кол-во просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блог',
                'ordering': ('title',),
            },
        ),
    ]