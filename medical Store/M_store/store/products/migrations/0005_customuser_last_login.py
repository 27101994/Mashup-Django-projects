# Generated by Django 4.2.6 on 2023-11-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
