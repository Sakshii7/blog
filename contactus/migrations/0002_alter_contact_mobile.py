# Generated by Django 4.0.5 on 2022-06-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
