# Generated by Django 2.1.3 on 2020-05-31 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-created_at']},
        ),
    ]
