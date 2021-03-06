# Generated by Django 4.0.2 on 2022-02-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('devfolio_link', models.URLField()),
                ('codebase_link', models.URLField()),
                ('team_name', models.CharField(max_length=30)),
                ('member_name', models.CharField(max_length=30)),
                ('member_email', models.EmailField(max_length=254)),
                ('member_phone', models.CharField(max_length=13)),
            ],
        ),
    ]
