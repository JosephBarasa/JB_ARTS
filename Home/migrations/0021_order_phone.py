# Generated by Django 5.0.6 on 2024-07-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0020_alter_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]

