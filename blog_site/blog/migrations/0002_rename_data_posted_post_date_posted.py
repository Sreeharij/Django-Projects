# Generated by Django 4.2.2 on 2023-07-12 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]
