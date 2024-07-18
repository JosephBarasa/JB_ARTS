# Generated by Django 5.0.6 on 2024-07-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0019_delete_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottles',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='size',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
