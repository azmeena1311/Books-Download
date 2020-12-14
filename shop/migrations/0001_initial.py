# Generated by Django 3.1.3 on 2020-12-13 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('discount', models.IntegerField(default=0)),
                ('file', models.FileField(blank=True, upload_to='uploads/files')),
                ('thumbnail', models.ImageField(upload_to='uploads/thumbnails')),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('fileSize', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='uploads/images')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_request_id', models.CharField(max_length=200, unique=True)),
                ('payment_id', models.CharField(max_length=200, unique=True)),
                ('status', models.CharField(default='Failed', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
        ),
    ]
