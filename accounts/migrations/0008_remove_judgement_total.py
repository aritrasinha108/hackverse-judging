# Generated by Django 4.0.2 on 2022-02-19 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_judgement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judgement',
            name='total',
        ),
    ]
