# Generated by Django 3.1.7 on 2021-02-21 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(choices=[('FASHION_BEAUTY', 'Fashion & Beauty'), ('KIDS_CLOTHES', 'Kids & Babies Clothes'), ('MEN_WOMEN_CLOTHES', 'Men & Women Clothes'), ('GADGET_ACCESSORIES', 'Gadgets & Accessories'), ('GADGET_ACCESSORIES', 'Electronics & Accessories')], max_length=100, null=True)),
                ('review_percentage', models.IntegerField(blank=True, null=True)),
                ('sold', models.IntegerField(default=0)),
                ('featured', models.BooleanField(default=False)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('detail', models.CharField(blank=True, max_length=150, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(blank=True, max_length=150, null=True)),
                ('reviewer_email', models.EmailField(blank=True, max_length=150, null=True)),
                ('review_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('review_rating', models.IntegerField(blank=True, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('default', models.BooleanField(default=False)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAdvert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='advert_banners/')),
                ('advert_description', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_duration', models.CharField(choices=[('DAILY', 'One(1) Day - ???1,000'), ('MONTHLY', 'One(1) Month - ???25,000'), ('YEARLY', 'One(1) Year - ???1,000')], default='DAILY', max_length=100)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
