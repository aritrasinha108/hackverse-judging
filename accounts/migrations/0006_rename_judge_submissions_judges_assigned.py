# Generated by Django 4.0.2 on 2022-02-18 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_submissions_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submissions',
            old_name='judge',
            new_name='judges_assigned',
        ),
    ]
