# Generated by Django 3.1.7 on 2021-02-22 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_productadvert_advert_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]