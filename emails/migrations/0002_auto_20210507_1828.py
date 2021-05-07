# Generated by Django 3.2.1 on 2021-05-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='publications',
        ),
        migrations.AddField(
            model_name='email',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, to='groups.Group'),
        ),
    ]
