# Generated by Django 3.1.6 on 2021-02-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='account',
            field=models.CharField(max_length=50),
        ),
    ]
