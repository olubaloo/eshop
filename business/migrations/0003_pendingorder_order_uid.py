# Generated by Django 3.1.7 on 2021-03-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20210301_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingorder',
            name='order_uid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]