# Generated by Django 3.1.7 on 2021-03-01 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='authorization_code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
