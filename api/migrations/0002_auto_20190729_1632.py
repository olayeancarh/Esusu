# Generated by Django 2.2.3 on 2019-07-29 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userssavingsgroup',
            unique_together={('user', 'savings_group')},
        ),
    ]
