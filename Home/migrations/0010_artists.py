# Generated by Django 5.0.6 on 2024-06-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='artistpics')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
