# Generated by Django 3.1.3 on 2020-12-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=200),
        ),
    ]
