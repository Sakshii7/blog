# Generated by Django 4.0.5 on 2022-06-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_testimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='image',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
