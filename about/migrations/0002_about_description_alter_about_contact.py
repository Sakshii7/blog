# Generated by Django 4.0.5 on 2022-06-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
