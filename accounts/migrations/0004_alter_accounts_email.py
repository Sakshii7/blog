# Generated by Django 4.0.5 on 2022-06-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accounts_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
